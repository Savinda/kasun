from docutils import nodes
from docutils.parsers.rst import Directive


class RedSection(Directive):

    def run(self):
        red_node = nodes.paragraph()
        return [red_node]


def setup(app):
    app.add_directive("redsection", RedSection)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
