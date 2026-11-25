"""Render the shared HTML page layout."""

from html import escape
from importlib.resources import files
from urllib.parse import quote, urlencode

import tomli
from jinja2 import Environment, PackageLoader, StrictUndefined
from markupsafe import Markup

from .paths import route

with files("ormos").joinpath("config.toml").open("rb") as stream:
    _CONFIG = tomli.load(stream)

SITE_NAME: str = _CONFIG["site"]["name"]
PUBLIC_ARCHIVE_ORIGIN: str = _CONFIG["site"]["archive_origin"]
VIDEO_ROUTE: str = _CONFIG["media"]["route"]
VIDEO_ORIGIN: str = _CONFIG["media"]["origin"]


def _escape_html(value: str) -> Markup:
    # Keep the entity spellings used by the deployed archive.
    return Markup(escape(value))


_TEMPLATES = Environment(
    loader=PackageLoader("ormos"),
    autoescape=True,
    auto_reload=False,
    keep_trailing_newline=True,
    undefined=StrictUndefined,
)
_TEMPLATES.globals["config"] = _CONFIG
_TEMPLATES.filters["escape_html"] = _escape_html
_COMPONENTS = _TEMPLATES.get_template("components.html").module
_PAGE = _TEMPLATES.get_template("page.html")


def _component(name: str, *args: object) -> str:
    return str(getattr(_COMPONENTS, name)(*args))


def link(href: str, label: str, **attributes: str) -> str:
    """Render a link with escaped text and attribute values."""
    return _component("link", href, label, attributes)


def site_footer(path: str) -> str:
    """Render the footer with a report link for this page."""
    route(path)
    parameters = urlencode(
        {
            "subject": _CONFIG["footer"]["report_subject"],
            "body": f"{PUBLIC_ARCHIVE_ORIGIN}{path}\r\n\r\n",
        },
        quote_via=quote,
    )
    return _component(
        "footer", f"mailto:{_CONFIG['footer']['report_email']}?{parameters}"
    )


def layout(
    title: str, path: str, content: str, *, lang: str = "en", scripts: str = ""
) -> str:
    """Wrap page content in the shared HTML layout."""
    home_title = _CONFIG["home"]["title"]
    browser_title = (
        f"{SITE_NAME} · {home_title}" if path == "/" else f"{title} · {SITE_NAME}"
    )
    policy: str = _CONFIG["security"]["content_security_policy"]
    if path.startswith(f"{VIDEO_ROUTE}/"):
        policy += f"; media-src 'self' {VIDEO_ORIGIN}"
    # Apostrophes can appear as-is inside a double-quoted attribute.
    attribute_value = Markup(escape(policy, quote=False).replace('"', "&quot;"))
    return _PAGE.render(
        title=browser_title,
        path=path,
        lang=lang,
        policy=attribute_value,
        scripts=scripts,
        content=content,
        footer=site_footer(path),
    )


def home_description() -> str:
    """Render the introduction on the home page."""
    return _component("home_description")


def home_supporters() -> str:
    """Render the home page list of supporters."""
    return _component("home_supporters")
