import random
from yed import yEd

N = 1000

y = yEd()

nodes = []

for i in range(N):
  color = "%02x" % random.randint(100, 255)
  nodes.append(y.node(text=str(i), fill_color="#" + color * 3))

for i in range(len(nodes)):
  nodes[i].connect(random.choice(nodes))

y.save("yed_test.graphml")
