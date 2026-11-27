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
MEDIA_ORIGIN: str = _CONFIG["media"]["origin"]
IMAGE_ORIGIN: str = _CONFIG["media"]["image_origin"]
MEDIA_ROUTE: str = _CONFIG["media"]["landing_route"]
FLASH_ROUTE: str = _CONFIG["media"]["flash_route"]
PODCAST_ROUTE: str = _CONFIG["media"]["podcast_route"]
FLASH_SCRIPT = "flash-player.js"


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
    flash_player: bool = False,
    flash_puzzle: bool = False,
    **context: object,
) -> str:
    """Render a page with its title, security policy, and report link."""
    path = route(path)
    home_title = _CONFIG["home"]["title"]
    browser_title = (
        f"{SITE_NAME} · {home_title}" if path == "/" else f"{title} · {SITE_NAME}"
    )
    policy: str = _CONFIG["security"]["content_security_policy"]
    if path.startswith((f"{VIDEO_ROUTE}/", f"{PODCAST_ROUTE}/")):
        policy += f"; media-src 'self' {MEDIA_ORIGIN}"
    if flash_player:
        # Ruffle fetches movies and injects its own shadow styles and icons.
        origins = f"{MEDIA_ORIGIN} {IMAGE_ORIGIN}" if flash_puzzle else MEDIA_ORIGIN
        directives = [directive.strip() for directive in policy.split(";")]
        for index, directive in enumerate(directives):
            if directive.startswith("img-src "):
                directives[index] = f"{directive} data:"
            elif directive.startswith("connect-src "):
                directives[index] = f"{directive} {origins}"
        directives.append("style-src-elem 'self' 'unsafe-inline'")
        policy = "; ".join(directives)
    section_path = (
        MEDIA_ROUTE
        if path in (VIDEO_ROUTE, FLASH_ROUTE, PODCAST_ROUTE)
        or path.startswith((f"{VIDEO_ROUTE}/", f"{FLASH_ROUTE}/", f"{PODCAST_ROUTE}/"))
        else path
    )
    # Apostrophes can appear as-is inside a double-quoted attribute.
    attribute_value = Markup(escape(policy, quote=False).replace('"', "&quot;"))
    return render_template(
        template,
        title=title,
        browser_title=browser_title,
        path=path,
        section_path=section_path,
        lang=lang,
        policy=attribute_value,
        script=script,
        flash_script=f"/assets/{FLASH_SCRIPT}" if flash_player else "",
        report_url=_report_url(path),
        **context,
    )
