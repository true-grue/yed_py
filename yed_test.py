import random
import yed

N = 1000

y = yed.Graph()

nodes = []

for i in range(N):
  color = "%02x" % random.randint(100, 255)
  nodes.append(y.node(text=str(i), fill_color="#" + color * 3))

for i in range(len(nodes)):
  nodes[i].to(random.choice(nodes))

y.save("yed_test.graphml")
