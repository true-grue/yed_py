# Author: Peter Sovietov

import html

NODE_STYLE = dict(
    text="",
    x=0,
    y=0,
    width=50,
    height=50,
    fill_color="#ffffff",
    border_color="#000000",
    has_border_color="true",
    border_width="1",
    font_family="Arial",
    font_size="12",
    text_color="#000000",
    shape="circle"
)


EDGE_STYLE = dict(
    text="",
    directed="true",
    line_color="#000000",
    line_width="1",
    source_arrow="none",
    target_arrow="delta",
    font_family="Arial",
    font_size="12",
    text_color="#000000"
)


GRAPH_XML = """\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
<key for="node" id="d0" yfiles.type="nodegraphics"/>
<key for="edge" id="d1" yfiles.type="edgegraphics"/>
<graph id="G" edgedefault="directed">
%(graph)s</graph>
</graphml>
"""

NODE_XML = """\
<node id="%(id)s">
<data key="d0">
<y:ShapeNode>
<y:Geometry x="%(x)s" y="%(y)s" width="%(width)s" height="%(height)s"/>
<y:Fill color="%(fill_color)s"/>
<y:BorderStyle color="%(border_color)s" width="%(border_width)s" hasColor="%(has_border_color)s"/>
<y:NodeLabel fontFamily="%(font_family)s" fontSize="%(font_size)s" alignment="center" textColor="%(text_color)s">%(text)s</y:NodeLabel>
<y:Shape type="%(shape)s"/>
</y:ShapeNode>
</data>
</node>
"""

EDGE_XML = """\
<edge directed="%(directed)s" source="%(source)s" target="%(target)s">
<data key="d1">
<y:PolyLineEdge>
<y:LineStyle color="%(line_color)s" type="line" width="%(line_width)s"/>
<y:Arrows source="%(source_arrow)s" target="%(target_arrow)s"/>
<y:EdgeLabel fontFamily="%(font_family)s" fontSize="%(font_size)s" alignment="center" textColor="%(text_color)s">%(text)s</y:EdgeLabel>
</y:PolyLineEdge>
</data>
</edge>
"""


class Graph:
    def __init__(self):
        self.node_id = 0
        self.items = []

    def node(self, **style):
        d = dict(NODE_STYLE, id=self.node_id)
        for k in style:
            d[k] = html.escape(str(style[k]))
        self.items.append(NODE_XML % d)
        self.node_id += 1
        return d

    def edge(self, n1, n2, **style):
        d = dict(EDGE_STYLE, source=n1["id"], target=n2["id"])
        for k in style:
            d[k] = html.escape(str(style[k]))
        self.items.append(EDGE_XML % d)
        return n1

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(GRAPH_XML % dict(graph="".join(self.items)))
