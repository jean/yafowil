from yafowil.base import factory
from yafowil.utils import (
    cssclasses,
    css_managed_props,
    managedprops,
)


@managedprops('id', *css_managed_props)
def table_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
    }
    return data.tag('table', data.rendered, **attrs)


factory.register(
    'table',
    extractors=factory.extractors('compound'),
    edit_renderers=factory.edit_renderers('compound') + [table_renderer])

factory.doc['widget']['table'] = """\
``<table>`` compound widget for table creation.
"""


def thead_renderer(widget, data):
    return data.tag('thead', data.rendered)


factory.register(
    'thead',
    extractors=factory.extractors('compound'),
    edit_renderers=factory.edit_renderers('compound') + [thead_renderer])

factory.doc['widget']['thead'] = """\
``<thead>`` compound widget for table creation.
"""


def tbody_renderer(widget, data):
    return data.tag('tbody', data.rendered)


factory.register(
    'tbody',
    extractors=factory.extractors('compound'),
    edit_renderers=factory.edit_renderers('compound') + [tbody_renderer])

factory.doc['widget']['tbody'] = """\
``<tbody>`` compound widget for table creation.
"""


@managedprops('id', *css_managed_props)
def tr_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
    }
    return data.tag('tr', data.rendered, **attrs)


factory.register(
    'tr',
    extractors=factory.extractors('compound'),
    edit_renderers=factory.edit_renderers('compound') + [tr_renderer])

factory.doc['widget']['tr'] = """\
``<tr>`` compound widget for table creation.
"""


@managedprops('id', 'rowspan', 'colspan', 'label', *css_managed_props)
def th_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
        'colspan': widget.attrs.get('colspan'),
        'rowspan': widget.attrs.get('rowspan'),
    }
    contents = widget.attrs.get('label')
    if not contents:
        contents = data.rendered
    return data.tag('th', contents, **attrs)


factory.register(
    'th',
    edit_renderers=[th_renderer])

factory.doc['widget']['th'] = """\
``<th>`` compound widget for table creation.
"""


@managedprops('id', 'rowspan', 'colspan', *css_managed_props)
def td_renderer(widget, data):
    attrs = {
        'id': widget.attrs.get('id'),
        'class_': cssclasses(widget, data),
        'colspan': widget.attrs.get('colspan'),
        'rowspan': widget.attrs.get('rowspan'),
    }
    return data.tag('td', data.rendered, **attrs)


factory.register(
    'td',
    edit_renderers=[td_renderer])

factory.doc['widget']['td'] = """\
``<td>`` compound widget for table creation.
"""