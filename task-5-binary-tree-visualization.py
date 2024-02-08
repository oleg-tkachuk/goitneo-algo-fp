import uuid
import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def insert_into_tree(arr, i, n):
    if i < n:
        node = Node(arr[i])
        node.left = insert_into_tree(arr, 2 * i + 1, n)
        node.right = insert_into_tree(arr, 2 * i + 2, n)
        return node
    return None


def draw_tree(tree_root, colors, title=""):
    tree = nx.DiGraph()
    pos = {}
    labels = {}

    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            pos[node.id] = (x, y)
            labels[node.id] = node.val
            tree.add_node(node.id)
            if node.left:
                tree.add_edge(node.id, node.left.id)
                add_edges(node.left, x - 1 / 2 ** layer, y - 1, layer + 1)
            if node.right:
                tree.add_edge(node.id, node.right.id)
                add_edges(node.right, x + 1 / 2 ** layer, y - 1, layer + 1)

    add_edges(tree_root)
    plt.figure(figsize=(12, 8))
    plt.title(title)
    nx.draw(tree, pos, labels=labels, with_labels=True, arrows=False, node_size=2000,
            node_color=[colors.get(node, "#FFFFFF") for node in tree.nodes()],
            font_weight='bold', font_size=12)
    plt.show()


def generate_color(step, total_steps):
    base_intensity = 230
    intensity = base_intensity - \
        int((base_intensity - 100) * (step / total_steps))
    return f"#{intensity:02x}{intensity:02x}FF"


def dfs(node, colors, step=0, total_steps=0):
    if node:
        colors[node.id] = generate_color(step, total_steps)
        step += 1
        step = dfs(node.left, colors, step, total_steps)
        step = dfs(node.right, colors, step, total_steps)
    return step


def bfs(root, colors, total_steps=0):
    queue = [root]
    step = 0
    while queue:
        node = queue.pop(0)
        if node:
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def insert_into_tree(arr, i, n):
    if i < n:
        node = Node(arr[i])
        node.left = insert_into_tree(arr, 2 * i + 1, n)
        node.right = insert_into_tree(arr, 2 * i + 2, n)
        return node
    return None


def build_tree_from_heap(arr):
    n = len(arr)
    return insert_into_tree(arr, 0, n)


def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


def main():
    print(f"*** GoIT Neo Algo Final Project ***")

    heap = generate_random_list(15, 0, 100)
    print(f"Task 5 - Binary Tree Visualization | Arbitrary list: {heap}")

    heapq.heapify(heap)
    print(f"Task 5 - Binary Tree Visualization | Binary heap: {heap}")

    tree_root = build_tree_from_heap(heap)

    # DFS
    colors = {}
    title_text_dfs = "Depth First Search"
    dfs(tree_root, colors, 0, len(heap))
    draw_tree(tree_root, colors, title_text_dfs)

    # BFS
    colors = {}
    title_text_bfs = "Breadth First Search"
    bfs(tree_root, colors, len(heap))
    draw_tree(tree_root, colors, title_text_bfs)


if __name__ == "__main__":
    main()
