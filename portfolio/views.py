from django.shortcuts import render

from .data import KINDS, PRACTICE, PRINCIPLES, PROJECTS, SNIPPETS, STACK


def home(request):
    return render(
        request,
        "portfolio/home.html",
        {
            "featured": [p for p in PROJECTS if p["featured"]],
            "project_count": len(PROJECTS),
            "principles": PRINCIPLES,
            "snippets": SNIPPETS,
            "stack": STACK,
        },
    )


def projects(request):
    return render(
        request,
        "portfolio/projects.html",
        {"projects": PROJECTS, "kinds": KINDS},
    )


def stack(request):
    return render(
        request,
        "portfolio/stack.html",
        {"stack": STACK, "practice": PRACTICE},
    )
