import heapq
import networkx as nx
from tabulate import tabulate
import matplotlib.pyplot as plt

nodes = [
    "Kyiv",
    "Athens",
    "Berlin",
    "Copenhagen",
    "Lisbon",
    "Oslo",
    "Rome",
    "Stockholm",
    "Tallinn",
    "Warsaw"
]

edges = [
    ('Kyiv', 'Warsaw', {'weight': 800}),
    ('Kyiv', 'Berlin', {'weight': 1300}),
    ('Berlin', 'Oslo', {'weight': 1040}),
    ('Berlin', 'Tallinn', {'weight': 1549}),
    ('Copenhagen', 'Stockholm', {'weight': 660}),
    ('Athens', 'Rome', {'weight': 1261}),
    ('Kyiv', 'Rome', {'weight': 2351}),
    ('Stockholm', 'Warsaw', {'weight': 1559}),
    ('Copenhagen', 'Athens', {'weight': 2760}),
    ('Lisbon', 'Oslo', {'weight': 3427}),
    ('Tallinn', 'Lisbon', {'weight': 4309}),
    ('Tallinn', 'Oslo', {'weight': 772}),
    ('Kyiv', 'Copenhagen', {'weight': 1776}),
    ('Berlin', 'Rome', {'weight': 1517}),
    ('Oslo', 'Warsaw', {'weight': 1028}),
    ('Rome', 'Lisbon', {'weight': 2511}),
]


def dijkstra(G, source):
    V = G.number_of_nodes()
    dist = {v: float('inf') for v in G.nodes}
    dist[source] = 0
    pq = [(0, source)]
    prev = {v: -1 for v in G.nodes}

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        if current_dist > dist[current_vertex]:
            continue

        for neighbor, data in G[current_vertex].items():
            weight = data['weight']
            if dist[current_vertex] + weight < dist[neighbor]:
                dist[neighbor] = dist[current_vertex] + weight
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (dist[neighbor], neighbor))

    paths = {v: [] for v in G.nodes}
    for target in G.nodes:
        if dist[target] == float('inf'):
            continue
        path = []
        current = target
        while current != source:
            path.append(current)
            current = prev[current]
        path.append(source)
        paths[target] = path[::-1]

    return dist, paths


def draw_graph(G, paths, source):
    plt.title("Dijkstra's Shortest Path", fontsize=14,
              fontweight='bold', color='black', loc='left')
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)

    edge_labels = dict([((u, v,), f"{d['weight']}")
                       for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    for path in paths.values():
        if len(path) > 1:
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges, edge_color='orange', width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path,
                                   node_color='lightgreen', node_size=700)
            nx.draw_networkx_nodes(G, pos, nodelist=[source],
                                   node_color="red", node_size=700)

    plt.show()


def main():
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    source = "Kyiv"
    dist, paths = dijkstra(G, source)

    table = []
    for vertex, distance in dist.items():
        if vertex != source:
            route = " -> ".join(paths[vertex])
            table.append([vertex, route, distance])

    print(tabulate(table, headers=[
          "City", "Route", "Distance"], tablefmt="grid",))

    draw_graph(G, paths, source)


if __name__ == "__main__":
    main()
