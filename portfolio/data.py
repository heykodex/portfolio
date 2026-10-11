"""All site content lives here. Edit this file to change what the portfolio says."""

PROFILE = {
    "name": "Kodex",
    "studio": "Paper Engine",
    "github": "heykodex",
    "twitter": "heykodexy",
    "description": (
        "Kodex is a solo developer and the founder of Paper Engine, a software studio "
        "building developer tools and polished, GitHub-ready projects."
    ),
}

NAV = [
    {"label": "Projects", "url_name": "projects"},
    {"label": "Stack & socials", "url_name": "stack"},
]

SOCIALS = [
    {
        "name": "GitHub",
        "handle": "heykodex",
        "url": "https://github.com/heykodex",
        "note": "Source, releases and the projects below.",
    },
    {
        "name": "X",
        "handle": "@heykodexy",
        "url": "https://x.com/heykodexy",
        "note": "Updates, experiments and the best place to message me.",
    },
]

PRINCIPLES = [
    {
        "title": "Design stays simple",
        "body": "Interfaces get out of the way so the work itself can do the talking.",
    },
    {
        "title": "Function leads",
        "body": "Every project starts from what it must do, then gets the quietest design that serves it.",
    },
    {
        "title": "Shipped means tested",
        "body": "CI, real test suites and docs that name the limits as clearly as the highlights.",
    },
]

KINDS = ["Language", "Simulation", "Web", "Apps", "Bots"]

PROJECTS = [
    {
        "slug": "vellum",
        "name": "Vellum",
        "kind": "Language",
        "featured": True,
        "summary": "A configuration language that is typed, computed and modular: a stricter alternative to JSON.",
        "tags": ["Language design", "Config"],
        "highlights": [
            "Typed values instead of loose strings",
            "Computed fields, so config can derive from config",
            "Modular files that compose cleanly",
        ],
    },
    {
        "slug": "horizon",
        "name": "Horizon",
        "kind": "Simulation",
        "featured": True,
        "summary": "A black hole N-body simulator with a Python physics engine and a Three.js viewer in the browser.",
        "tags": ["Python", "Three.js", "N-body"],
        "highlights": [
            "Physics engine and viewer are separate pieces",
            "Interactive 3D view of orbits around a black hole",
        ],
    },
    {
        "slug": "unsaid",
        "name": "Unsaid",
        "kind": "Web",
        "featured": True,
        "summary": "A privacy-first social platform where you choose how visible you are.",
        "tags": ["Django", "DRF", "React", "Vite"],
        "highlights": [
            "Ghost, Shadow and Open anonymous identity modes",
            "Direct messaging",
            "Staff moderation tools",
        ],
    },
    {
        "slug": "dropgrid",
        "name": "DropGrid",
        "kind": "Apps",
        "featured": True,
        "summary": "A privacy-first file transfer app for devices on the same local network.",
        "tags": ["Local network", "Privacy"],
        "highlights": [
            "OAddress identity instead of accounts",
            "Pair by QR code, Nearby or OAddress",
            "Trust that expires, and sending to several devices at once",
        ],
    },
    {
        "slug": "library-shelf",
        "name": "Library Shelf",
        "kind": "Apps",
        "featured": False,
        "summary": "A desktop package manager for Python, with a companion VS Code extension.",
        "tags": ["Python", "tkinter", "VS Code"],
        "highlights": ["Desktop app built with tkinter", "Extension brings it into the editor"],
    },
    {
        "slug": "no-github-for-now",
        "name": "No GitHub for Now",
        "kind": "Web",
        "featured": False,
        "summary": "A temporary place to share code for review, with a web app and a VS Code extension.",
        "tags": ["Django", "VS Code"],
        "highlights": [
            "Line comments without creating an account",
            "10 MB upload limit and 15-day expiry",
        ],
    },
    {
        "slug": "easyrecords",
        "name": "EasyRecords",
        "kind": "Apps",
        "featured": False,
        "summary": "A desktop app for shops to keep customer sale records, synced to Google Sheets and Drive.",
        "tags": ["Electron", "Apps Script", "Google Sheets"],
        "highlights": ["Electron desktop client", "Sync handled through Google Apps Script"],
    },
    {
        "slug": "jk-computers",
        "name": "JK Computers",
        "kind": "Web",
        "featured": False,
        "summary": "A Django website for a local laptop and computer shop.",
        "tags": ["Django"],
        "highlights": [
            "Catalog, sales and wishlist",
            "Find My Laptop guided search",
            "WhatsApp checkout",
        ],
    },
    {
        "slug": "tae-staff",
        "name": "TAE Staff",
        "kind": "Web",
        "featured": False,
        "summary": "An internal management system for an academy: students, fees, marks and results.",
        "tags": ["Django"],
        "highlights": ["Fees and marks tracking", "Printable papers and result sheets"],
    },
    {
        "slug": "kodexity",
        "name": "Kodexity",
        "kind": "Bots",
        "featured": False,
        "summary": "A public Discord moderation bot built on discord.py.",
        "tags": ["Python", "discord.py"],
        "highlights": [
            "Global slash commands",
            "Mod logs routed across servers to one central place",
            "Bans and mutes of 5+ days add an appeal link to the DM",
        ],
    },
    {
        "slug": "event-banner-generator",
        "name": "Event Banner Generator",
        "kind": "Web",
        "featured": False,
        "summary": "A small web app that generates event banners on demand.",
        "tags": ["Flask", "Pillow"],
        "highlights": ["Images composed server-side with Pillow", "Deployed on PythonAnywhere"],
        "link": "https://github.com/heykodex/cobannergenerator",
    },
    {
        "slug": "black-hole-sim",
        "name": "Pygame black hole sim",
        "kind": "Simulation",
        "featured": False,
        "summary": "The first black hole simulation: gravity you can throw things into.",
        "tags": ["Python", "Pygame"],
        "highlights": [
            "Velocity Verlet integration",
            "Mergers that conserve momentum, tidal spaghettification and a slingshot mechanic",
            "Shift-click to spawn a body on a circular orbit",
        ],
    },
    {
        "slug": "kodex-log",
        "name": "kodex.log",
        "kind": "Web",
        "featured": False,
        "summary": "A personal Django blog with a soft palette and a kaomoji habit. :3",
        "tags": ["Django", "Markdown"],
        "highlights": [
            "Markdown rendering through a custom template filter",
            "Newsletter with token-based unsubscribe",
            "Cover images generated with Pillow",
        ],
    },
    {
        "slug": "blackmail",
        "name": "BlackMail",
        "kind": "Web",
        "featured": False,
        "summary": "An email client that runs entirely in the browser, with no framework and no backend.",
        "tags": ["HTML", "CSS", "JavaScript"],
        "highlights": ["Three-column layout", "Separate database, protocol and UI controller layers"],
    },
]

STACK = [
    {
        "group": "Languages",
        "blurb": "Python for almost everything, JavaScript where the browser demands it.",
        "items": [
            {"name": "Python", "note": "Backends, simulations, bots and desktop tools."},
            {"name": "JavaScript", "note": "Interfaces, Electron and VS Code extensions."},
            {"name": "HTML & CSS", "note": "Hand-written, no UI kit."},
        ],
    },
    {
        "group": "Backend",
        "blurb": "Batteries-included web frameworks and the bots that live beside them.",
        "items": [
            {"name": "Django", "note": "Sites, internal tools and platforms."},
            {"name": "Django REST Framework", "note": "APIs behind React front ends."},
            {"name": "Flask", "note": "Small services and generators."},
            {"name": "discord.py", "note": "Moderation and community bots."},
        ],
    },
    {
        "group": "Frontend & graphics",
        "blurb": "Fast interfaces and physics you can look at.",
        "items": [
            {"name": "React", "note": "Application front ends."},
            {"name": "Vite", "note": "Build tooling."},
            {"name": "Three.js", "note": "3D viewers, such as Horizon."},
            {"name": "Pygame", "note": "Quick physics prototypes."},
        ],
    },
    {
        "group": "Desktop & tooling",
        "blurb": "Software that lives on a laptop and inside an editor.",
        "items": [
            {"name": "Electron", "note": "Cross-platform desktop apps."},
            {"name": "tkinter", "note": "Lightweight Python GUIs."},
            {"name": "VS Code extensions", "note": "Bringing tools into the editor."},
            {"name": "Google Apps Script", "note": "Sheets and Drive sync."},
            {"name": "Pillow", "note": "Generated images."},
        ],
    },
]

PRACTICE = [
    {
        "title": "Sketch the spec",
        "body": "Write down what the project must do and what it will not do before any code exists.",
    },
    {
        "title": "Build the core",
        "body": "Get the smallest working version running end to end, then widen it.",
    },
    {
        "title": "Test it for real",
        "body": "A proper suite that fails when behaviour breaks, not placeholders to raise a coverage number.",
    },
    {
        "title": "Automate with CI",
        "body": "Every push runs the checks, so a green build means something.",
    },
    {
        "title": "Document honestly",
        "body": "A README that says how to run it, what it does well and where it falls short.",
    },
    {
        "title": "Publish on GitHub",
        "body": "Tagged, tidy and ready for someone else to open on a first visit.",
    },
]

SNIPPETS = [
    {
        "id": "kodex",
        "file": "kodex.py",
        "code": r'''
from dataclasses import dataclass


@dataclass
class Kodex:
    studio: str = "Paper Engine"
    role: str = "solo developer"
    builds: tuple = ("languages", "simulators", "apps")
    ships: tuple = ("tests", "CI", "honest docs")


# Simple design. Functionality drives.
print(Kodex())
''',
    },
    {
        "id": "horizon",
        "file": "horizon.py",
        "code": r'''
def step(bodies, dt):
    # Velocity Verlet: advance positions, then blend old and new acceleration
    for b in bodies:
        b.pos += b.vel * dt + 0.5 * b.acc * dt * dt
    new_acc = [gravity(b, bodies) for b in bodies]
    for b, a in zip(bodies, new_acc):
        b.vel += 0.5 * (b.acc + a) * dt
        b.acc = a
''',
    },
    {
        "id": "stack",
        "file": "stack.py",
        "code": r'''
STACK = {
    "web": ["Django", "DRF", "React", "Vite"],
    "graphics": ["Three.js", "Pygame"],
    "desktop": ["Electron", "tkinter"],
    "bots": ["discord.py"],
}

# Python first. Reach for the rest when the job asks.
''',
    },
]
