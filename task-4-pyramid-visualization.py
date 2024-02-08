import uuid
import heapq
import random
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


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
    print(f"Task 4 - Pyramid visualization | Arbitrary list: {heap}")

    heapq.heapify(heap)
    print(f"Task 4 - Pyramid visualization | Binary heap: {heap}")

    tree_root = build_tree_from_heap(heap)
    draw_tree(tree_root)


if __name__ == "__main__":
    main()
