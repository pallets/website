from marko import Markdown
from marko.block import LinkRefDef
from marko.inline import Link
from marko.inline import Image


class RelativeLink(Link):
    pass


class RelativeLinkRefDef(LinkRefDef):
    pass


class RelativeImage(Image):
    pass


markdown = Markdown(extensions=["codehilite"])
