from random import randint, choice
import yed

y = yed.Graph()

nodes = []
for i in range(100):
    color = "#" + ("%02x" % randint(100, 255)) * 3
    nodes.append(y.node(text=i, fill_color=color))

for n in nodes:
    y.edge(n, choice(nodes))

y.save("test.graphml")
