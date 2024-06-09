import matplotlib.pyplot as plt
import networkx as nx

# Reinitialize the variables and graph to avoid scope issues
G = nx.DiGraph()
nodes = {
    "A1": (70, 80),
    "A2": (80, 75),
    "A3": (95, 80),
    "A4": (65, 85),
    "A5": (70, 55),
    "A6": (60, 60),
    "A7": (50, 50),
    "A8": (85, 90)
}
positions = {
    "A1": (2, 3),
    "A2": (3, 2),
    "A3": (3, 4),
    "A4": (1, 2),
    "A5": (2, 1),
    "A6": (1, 1),
    "A7": (0, 0),
    "A8": (4, 5)
}
labels = {node: f"{node}\n(P: {pr[0]}%, R: {pr[1]}%)" for node, pr in nodes.items()}
color_map = [(nodes[node][1] - 50) / (90 - 50) for node in nodes]  # Normalized based on recall values

# Add nodes and edges
G.add_nodes_from(nodes)
edges = [("A8", "A3"), ("A8", "A2"), ("A8", "A1"), ("A3", "A1"), ("A3", "A2"),
         ("A3", "A5"), ("A3", "A6"), ("A3", "A7"), ("A1", "A5"), ("A1", "A6"),
         ("A4", "A5"), ("A4", "A6"), ("A2", "A5"), ("A2", "A6"), ("A2", "A7"),
         ("A5", "A7"), ("A6", "A7")]
G.add_edges_from(edges)

# Draw the graph with labels adjusted below the nodes
plt.figure(figsize=(10, 10))
nx.draw(G, pos=positions, with_labels=False, node_color=color_map, cmap=plt.cm.coolwarm,
        node_size=3000, arrowstyle='-|>', arrowsize=20, font_size=12, font_weight='bold',
        edge_color="#888888")

# Adjust the label positions to be slightly lower
label_positions = {node: (pos[0], pos[1] - 0.1) for node, pos in positions.items()}
nx.draw_networkx_labels(G, label_positions, labels=labels, font_size=10)

plt.title("Hasse Diagram of AI Programs")
plt.show()
