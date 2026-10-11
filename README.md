# Kodex · Paper Engine portfolio

A minimal, modern portfolio in Django, styled in the spirit of zed.dev, supabase and gemini.com:
a blueprint-grid hero, a live-looking code editor, big quiet type and light/dark themes that follow
the system setting.

## Pages

| URL | What's on it |
| --- | --- |
| `/` | Hero + editor, principles, featured projects, stack, socials, contact |
| `/projects/` | All 14 past projects with a kind filter |
| `/stack/` | Stack in detail, how a project ships, socials |

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
export DJANGO_DEBUG=1
python manage.py runserver
```

Tests and lint (the same commands CI runs):

```bash
export DJANGO_SECRET_KEY=local-test-key
ruff check .
python manage.py test
```

## Edit the content

Everything lives in `portfolio/data.py`: profile, socials, projects, stack, principles and the
editor snippets. Set `"featured": True` on exactly four projects for the home page (a test enforces
this). Colours and type are CSS variables at the top of `portfolio/static/portfolio/css/site.css`.

## Deploy

Set these environment variables on your host, then run `collectstatic` and serve with gunicorn
(`Procfile` included; static files are served by WhiteNoise):

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Required when `DJANGO_DEBUG` is not `1` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames, e.g. `kodex.dev,www.kodex.dev` |
| `DJANGO_FORCE_HTTPS` | `1` to enable HTTPS redirect, HSTS and secure cookies |

## Honest notes

- No database or admin: content is a Python file, so changing it means a commit and a redeploy.
- Fonts (Hanken Grotesk, JetBrains Mono) load from Google Fonts, with system fallbacks if blocked.
- The editor demo works without JavaScript but only shows the first file; tabs need JS.
- Tests cover routes, content integrity, the syntax-highlighting filter and security headers.
  They don't cover visual layout, so check it in a browser after changing the CSS.
- Only GitHub and X are listed as socials. Add more entries to `SOCIALS` in `data.py`.
- Project descriptions are short summaries. Add repo links with a `"link"` key per project.
