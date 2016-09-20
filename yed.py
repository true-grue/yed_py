# Making graphs for yEd
# Author: Peter Sovietov

import cgi

Graph_text = """\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
<key for="node" id="d0" yfiles.type="nodegraphics"/>
<key for="edge" id="d1" yfiles.type="edgegraphics"/>
<graph id="G" edgedefault="directed">
%(graph)s</graph>
</graphml>
"""

Node_text = """\
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

Edge_text = """\
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

class Node:
  def to(self, node, **kwargs):
    self.graph.edge(self, node, **kwargs)
    return self

  def __init__(self, graph):
    self.graph = graph
    self.id = graph.ids

class Graph:
  def edge(self, n1, n2, **kwargs):
    d = {
      "source": n1.id,
      "target": n2.id
    }
    d.update(self.edge_style)
    for k in kwargs:
      d[k] = cgi.escape(str(kwargs[k]))
    self.elements.append(Edge_text % d)

  def node(self, **kwargs):
    d = {
      "id": self.ids
    }
    d.update(self.node_style)
    for k in kwargs:
      d[k] = cgi.escape(str(kwargs[k]))
    self.elements.append(Node_text % d)
    n = Node(self)
    self.ids += 1
    return n

  def save(self, name):
    with open(name, "w") as f:
      f.write(Graph_text % {
        "graph": "".join(self.elements)
      })

  def __init__(self):
    self.node_style = {
      "text": "",
      "x": 0,
      "y": 0,
      "width": 50,
      "height": 50,
      "fill_color": "#ffffff",
      "border_color": "#000000",
      "has_border_color": "true",
      "border_width": "1",
      "font_family": "Arial",
      "font_size": "12",
      "text_color": "#000000",
      "shape": "circle"
    }
    self.edge_style = {
      "text": "",
      "directed": "true",
      "line_color": "#000000",
      "line_width": "1",
      "source_arrow": "none",
      "target_arrow": "delta",
      "font_family": "Arial",
      "font_size": "12",
      "text_color": "#000000"
    }
    self.elements = []
    self.ids = 0

def connect(n, m, **kwargs):
  if isinstance(n, list) and isinstance(m, list):
    for x in n:
      for y in m:
        x.to(y, **kwargs)
  elif isinstance(n, list):
    for x in n:
      x.to(m, **kwargs)
  elif isinstance(m, list):
    for x in m:
      n.to(x, **kwargs)
  else:
    n.to(m, **kwargs)
