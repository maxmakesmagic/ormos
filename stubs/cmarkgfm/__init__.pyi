"""Type information for the cmarkgfm API used by Ormos."""

from typing import ClassVar

class Options:
    """Flags for the Markdown renderer."""

    CMARK_OPT_UNSAFE: ClassVar[int]

def github_flavored_markdown_to_html(text: str, options: int = ...) -> str:
    """Render GitHub-flavored Markdown as HTML."""
