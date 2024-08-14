from __future__ import annotations

import collections.abc as c
import typing as t

import pygments
from bs4 import BeautifulSoup
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
    tokens: c.Sequence[Token],
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
    tokens: c.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]
    href = t.cast(str | None, token.attrs.get("href"))
    href = _rewrite_link(href, env["content_dir"], True)

    if href is not None:
        token.attrs["href"] = href

    return renderer.renderToken(tokens, index, options, env)


def render_image(
    renderer: RendererHTML,
    tokens: c.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]
    src = t.cast(str | None, token.attrs.get("src"))
    src = _rewrite_link(src, env["content_dir"])

    if src is not None:
        token.attrs["src"] = src

    return renderer.renderToken(tokens, index, options, env)


def render_html_block(
    renderer: RendererHTML,
    tokens: c.Sequence[Token],
    index: int,
    options: OptionsDict,
    env: dict[str, t.Any],
) -> str:
    token = tokens[index]
    # TODO handle partial html blocks wrapping markdown
    soup = BeautifulSoup(token.content, "lxml")

    for attr, page in (("href", True), ("src", False)):
        for tag in soup.find_all(**{attr: True}):
            ref = t.cast(str | None, tag[attr])
            ref = _rewrite_link(ref, env["content_dir"], page)

            if ref is not None:
                tag[attr] = ref

    assert soup.html is not None
    soup.html.unwrap()
    assert soup.body is not None
    soup.body.unwrap()
    token.content = str(soup)
    return renderer.html_block(tokens, index, options, env)


def _rewrite_link(
    ref: str | None, content_dir: str, allow_page: bool = False
) -> str | None:
    if ref is None:
        return None

    if ref and ref[0] != "/" and ":" not in ref:
        # rewrite relative links to be served by app views
        if (
            allow_page
            and (page_ref := ref.removesuffix(".md").removesuffix(".toml")) != ref
        ):
            # remove .md and .toml extensions in links to other pages
            return f"{content_dir}/{page_ref}".removeprefix("/")
        else:
            # other files are served by static content view
            parts = ["/static/content"]

            if content_dir:
                parts.append(content_dir)

            parts.append(ref)
            return "/".join(parts)

    return ref


md = MarkdownIt(options_update={"highlight": highlight})
md.add_render_rule("fence", render_fence)
md.add_render_rule("link_open", render_link_open)
md.add_render_rule("image", render_image)
md.add_render_rule("html_block", render_html_block)


def render_content(src: str, path: str) -> str:
    return t.cast(str, md.render(src, {"content_dir": path}))
