import networkx as nx
import matplotlib.pyplot as plt


# Function to manually assign edges to create three connected components from the degree sequence
def create_multigraph_three_components():
    # Define three graphs for three components
    G1 = nx.MultiGraph()
    G2 = nx.MultiGraph()
    G3 = nx.MultiGraph()

    # Nodes for each component
    nodes_G1 = [0, 1]  # Component 1
    nodes_G2 = [2, 3, 4, 5]  # Component 2
    nodes_G3 = [6, 7]  # Component 3

    # Adding nodes to each component
    G1.add_nodes_from(nodes_G1)
    G2.add_nodes_from(nodes_G2)
    G3.add_nodes_from(nodes_G3)

    # Manually adding edges
    # Component 1 (total degrees: 7, 2)
    edges_G1 = [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)]  # Total: 7, 7

    # Component 2 (total degrees: 5, 5, 5, 3)
    edges_G2 = [(2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (2, 3), (2, 4)]  # Total: 5, 5, 5, 3

    # Component 3 (total degrees: 3, 2)
    edges_G3 = [(6, 7), (6, 7), (6, 7)]  # Total: 3, 3

    # Add edges to graphs
    G1.add_edges_from(edges_G1)
    G2.add_edges_from(edges_G2)
    G3.add_edges_from(edges_G3)

    # Combine all three components into a single graph
    G = nx.disjoint_union(G1, G2)
    G = nx.disjoint_union(G, G3)

    return G


# Generate and draw the multigraph with 3 connected components
multigraph_3c = create_multigraph_three_components()

# Plot the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(multigraph_3c, seed=42)  # Consistent layout for nodes
nx.draw_networkx(multigraph_3c, pos, with_labels=True, node_color='cyan', font_weight='bold', node_size=700,
                 font_size=10)
plt.title('Multigraph with 3 Connected Components')
plt.show()
