from docutils import nodes
from docutils.parsers.rst import Directive


class RightQuote(Directive):

    def run(self):
        blockquote_node = nodes.block_quote("")
        return [blockquote_node]


def setup(app):
    app.add_directive("rightquote", RightQuote)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
