from django.contrib.staticfiles import finders
from django.template import Context, Template
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils.html import escape

from .data import KINDS, PRACTICE, PROFILE, PROJECTS, SNIPPETS, SOCIALS, STACK


class PageTests(SimpleTestCase):
    def test_pages_render(self):
        for name, template in [
            ("home", "portfolio/home.html"),
            ("projects", "portfolio/projects.html"),
            ("stack", "portfolio/stack.html"),
        ]:
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)

    def test_home_has_every_requested_section(self):
        html = self.client.get(reverse("home")).content.decode()
        for anchor in ('id="projects"', 'id="stack"', 'id="socials"', 'id="contact"'):
            self.assertIn(anchor, html)

    def test_home_shows_only_featured_projects(self):
        html = self.client.get(reverse("home")).content.decode()
        for project in PROJECTS:
            if project["featured"]:
                self.assertIn(project["name"], html)
            else:
                self.assertNotIn(f'<h3>{project["name"]}</h3>', html)

    def test_projects_page_lists_every_project(self):
        html = self.client.get(reverse("projects")).content.decode()
        for project in PROJECTS:
            self.assertIn(project["summary"], html)

    def test_projects_page_has_a_filter_per_kind(self):
        html = self.client.get(reverse("projects")).content.decode()
        for kind in KINDS:
            self.assertIn(f'data-filter="{kind}"', html)

    def test_stack_page_has_stack_practice_and_socials(self):
        html = self.client.get(reverse("stack")).content.decode()
        for group in STACK:
            self.assertIn(escape(group["group"]), html)
        for step in PRACTICE:
            self.assertIn(step["title"], html)
        for social in SOCIALS:
            self.assertIn(social["url"], html)

    def test_nav_marks_current_page(self):
        html = self.client.get(reverse("projects")).content.decode()
        self.assertIn(f'href="{reverse("projects")}" aria-current="page"', html)

    def test_unknown_url_returns_404_page(self):
        response = self.client.get("/does-not-exist/")
        self.assertEqual(response.status_code, 404)

    def test_security_headers(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response["X-Frame-Options"], "DENY")
        self.assertEqual(response["X-Content-Type-Options"], "nosniff")

    def test_static_assets_are_found(self):
        for path in ("portfolio/css/site.css", "portfolio/js/site.js"):
            self.assertIsNotNone(finders.find(path), path)


class DataTests(SimpleTestCase):
    def test_project_slugs_are_unique(self):
        slugs = [p["slug"] for p in PROJECTS]
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_projects_have_required_fields_and_known_kind(self):
        for p in PROJECTS:
            with self.subTest(project=p["slug"]):
                for key in ("name", "kind", "summary", "tags", "highlights", "featured"):
                    self.assertIn(key, p)
                self.assertIn(p["kind"], KINDS)
                self.assertTrue(p["highlights"])

    def test_every_kind_is_used(self):
        self.assertEqual({p["kind"] for p in PROJECTS}, set(KINDS))

    def test_featured_count_fits_the_home_page(self):
        self.assertEqual(sum(p["featured"] for p in PROJECTS), 4)

    def test_external_links_use_https(self):
        urls = [s["url"] for s in SOCIALS] + [p["link"] for p in PROJECTS if "link" in p]
        for url in urls:
            self.assertTrue(url.startswith("https://"), url)

    def test_social_handles_match_profile(self):
        urls = " ".join(s["url"] for s in SOCIALS)
        self.assertIn(PROFILE["github"], urls)
        self.assertIn(PROFILE["twitter"], urls)

    def test_snippet_ids_are_unique(self):
        ids = [s["id"] for s in SNIPPETS]
        self.assertEqual(len(ids), len(set(ids)))


class CodeLinesFilterTests(SimpleTestCase):
    def render(self, source):
        template = Template("{% load portfolio_extras %}{{ s|code_lines }}")
        return template.render(Context({"s": source}))

    def test_one_span_per_line(self):
        self.assertEqual(self.render("a = 1\nb = 2").count('class="ln"'), 2)

    def test_tokens_are_classified(self):
        html = self.render('def run():  # go\n    return "x"')
        self.assertIn('<span class="t-k">def</span>', html)
        self.assertIn('<span class="t-f">run</span>', html)
        self.assertIn('<span class="t-c"># go</span>', html)
        self.assertIn('<span class="t-s">&quot;x&quot;</span>', html)

    def test_html_is_escaped(self):
        html = self.render("x = '<script>alert(1)</script>'")
        self.assertNotIn("<script>", html)
        self.assertIn("&lt;script&gt;", html)
