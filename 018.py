source = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".split('\n')[1:-1]

class Node(object):

    # class variable used to store the max value of a node
    maximum = 0

    def __init__(self, value):
        self.value = value

    # transorming the problem -> shortest path (cost) from top to bottom
    @property
    def cost(self):
        return Node.maximum - self.value

# transforming the source into an list of list of nodes
nodes = []
for line in source:
    level = []
    for i in line.split(' '):
        level.append(Node(int(i)))
        Node.maximum = int(i) if int(i) > Node.maximum else Node.maximum
    nodes.append(level)

# giving each nodes its descendant (left, right)
for level,line in enumerate(nodes):
    try:
        next_ = nodes[level + 1]
    except IndexError:
        break
    for index, node in enumerate(line):
        node.left = next_[index]
        node.right = next_[index+1]

# starting from the top SEARCH for the shortest path
top = nodes[0][0]
# on the frontier we store nodes with the accumulated cost (total)
frontier = [(top, top.cost)]

def expand_frontier():
    # find the node with the lowest total on the frontier
    minimum, total = min(frontier, key=lambda node: node[1])
    # add its descendants and respective accumulated costs
    frontier.append( (minimum.left, minimum.left.cost + total) )
    frontier.append( (minimum.right, minimum.right.cost + total) )
    # remove the minimal node from the frontier
    frontier.remove((minimum, total))

# expand the frontier until we reach the bottom i.e. a leaf node
while True:
    try:
        expand_frontier()
    except AttributeError:
        bottom, total = min(frontier, key=lambda node: node[1])
        # computing the max sum
        print Node.maximum * len(nodes) - total
        break
