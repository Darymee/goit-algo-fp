import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#87CEEB"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color_gradient(n, start_color="#003366", end_color="#99ccff"):
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    start_rgb = hex_to_rgb(start_color)
    end_rgb = hex_to_rgb(end_color)

    gradient = []
    for i in range(n):
        interp = [
            int(start_rgb[j] + (end_rgb[j] - start_rgb[j]) * i / (n - 1))
            for j in range(3)
        ]
        gradient.append(rgb_to_hex(tuple(interp)))
    return gradient


def bfs_visualize(root):
    queue = deque([root])
    visited = []
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    colors = generate_color_gradient(len(order))
    for idx, node in enumerate(order):
        node.color = colors[idx]
        draw_tree(root)


def dfs_visualize(root):
    stack = [root]
    visited = []
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    colors = generate_color_gradient(len(order))
    for idx, node in enumerate(order):
        node.color = colors[idx]
        draw_tree(root)


def build_heap_tree(array):
    if not array:
        return None

    nodes = [Node(val) for val in array]
    n = len(nodes)

    for i in range(n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        if right_idx < n:
            nodes[i].right = nodes[right_idx]

    return nodes[0]

heap_array = [10, 9, 8, 7, 6, 5, 4]
heap_root_bfs = build_heap_tree(heap_array)
heap_root_dfs = build_heap_tree(heap_array)

print("BFS (Обхід у ширину):")
bfs_visualize(heap_root_bfs)

print("DFS (Обхід у глибину):")
dfs_visualize(heap_root_dfs)
