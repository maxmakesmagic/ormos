"""Render archive templates with shared page metadata."""

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


def render_template(template: str, **context: object) -> str:
    """Render a Jinja2 template with its data."""
    return _TEMPLATES.get_template(template).render(**context)


def _report_url(path: str) -> str:
    parameters = urlencode(
        {
            "subject": _CONFIG["footer"]["report_subject"],
            "body": f"{PUBLIC_ARCHIVE_ORIGIN}{path}\r\n\r\n",
        },
        quote_via=quote,
    )
    return f"mailto:{_CONFIG['footer']['report_email']}?{parameters}"


def render_page(
    template: str,
    title: str,
    path: str,
    *,
    lang: str = "en",
    script: str = "",
    **context: object,
) -> str:
    """Render a page with its title, security policy, and report link."""
    path = route(path)
    home_title = _CONFIG["home"]["title"]
    browser_title = (
        f"{SITE_NAME} · {home_title}" if path == "/" else f"{title} · {SITE_NAME}"
    )
    policy: str = _CONFIG["security"]["content_security_policy"]
    if path.startswith(f"{VIDEO_ROUTE}/"):
        policy += f"; media-src 'self' {VIDEO_ORIGIN}"
    # Apostrophes can appear as-is inside a double-quoted attribute.
    attribute_value = Markup(escape(policy, quote=False).replace('"', "&quot;"))
    return render_template(
        template,
        title=title,
        browser_title=browser_title,
        path=path,
        lang=lang,
        policy=attribute_value,
        script=script,
        report_url=_report_url(path),
        **context,
    )
