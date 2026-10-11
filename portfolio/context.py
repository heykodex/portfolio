from datetime import date

from .data import NAV, PROFILE, SOCIALS


def site(request):
    return {
        "nav": NAV,
        "profile": PROFILE,
        "socials": SOCIALS,
        "year": date.today().year,
    }
