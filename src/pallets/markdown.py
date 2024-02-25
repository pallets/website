from __future__ import annotations

import collections.abc as cabc
import posixpath
import typing as t

import pygments
from markdown_it import MarkdownIt
from markdown_it.renderer import RendererHTML
from markdown_it.token import Token
from markdown_it.utils import OptionsDict
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

_pygments_html_formatter = HtmlFormatter(nowrap=True)


def highlight(content: str, langName: str, langAttrs: str) -> str | None:
    # use pygments to highlight fenced code blocks with language info
    try:
        lexer = get_lexer_by_name(langName)
    except ValueError:
        # no highlighting, the renderer will escape the content
        return None

    # the pygments formatter handles escaping the content
    return pygments.highlight(content, lexer, _pygments_html_formatter)


def render_fence(
    renderer: RendererHTML,
    tokens: cabc.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]

    if token.info:
        # add the highlight class for pygments
        token.attrJoin("class", "highlight")

    return renderer.fence(tokens, index, options, env)


def render_link_open(
    renderer: RendererHTML,
    tokens: cabc.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]
    ref: str | None = token.attrs.get("href")

    if ref and ref[0] != "/" and ":" not in ref:
        # rewrite relative links to be served by app views
        if (page_ref := ref.removesuffix(".md").removesuffix(".toml")) != ref:
            # remove .md and .toml extensions in links to other pages
            token.attrs["href"] = f"{env["content_dir"]}/{page_ref}".removeprefix("/")
        else:
            # other files are served by static content view
            token.attrs["href"] = f"/static/content/{env["content_dir"]}/{ref}"

    return renderer.renderToken(tokens, index, options, env)


def render_image(
    renderer: RendererHTML,
    tokens: cabc.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]
    ref: str | None = token.attrs.get("src")

    if ref and ref[0] != "/" and ":" not in ref:
        # files are served by static content view
        token.attrs["src"] = posixpath.normpath(
            f"/static/content/{env["content_dir"]}/{ref}"
        )

    return renderer.renderToken(tokens, index, options, env)


md = MarkdownIt(options_update={"highlight": highlight})
md.add_render_rule("fence", render_fence)
md.add_render_rule("link_open", render_link_open)
md.add_render_rule("image", render_image)


def render_content(src: str, path: str) -> str:
    return md.render(src, {"content_dir": path})
