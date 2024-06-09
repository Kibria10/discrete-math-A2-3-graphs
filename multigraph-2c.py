import networkx as nx
import matplotlib.pyplot as plt


# Function to manually assign edges based on provided degree sequences to form two connected components
def create_manual_multigraph_two_components():
    # Create two separate graphs as components
    G1 = nx.MultiGraph()
    G2 = nx.MultiGraph()

    # Add nodes for each component
    nodes_G1 = [0, 1, 2, 3]  # Component 1
    nodes_G2 = [4, 5, 6, 7]  # Component 2

    G1.add_nodes_from(nodes_G1)
    G2.add_nodes_from(nodes_G2)

    # Manually add edges to satisfy the degree sequence within each component
    # Component 1 edges (total degree sequence: 7, 5, 3, 2)
    edges_G1 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1)]  # Total: 7, 3, 3, 2
    G1.add_edges_from(edges_G1)

    # Adjusting to get exact degree match
    G1.add_edge(2, 1)  # Now 7, 5, 3, 2

    # Component 2 edges (total degree sequence: 7, 5, 5, 3)
    edges_G2 = [(4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7), (4, 5), (4, 6)]  # Total: 7, 3, 3, 2
    G2.add_edges_from(edges_G2)

    # Adjusting to get exact degree match
    G2.add_edge(5, 6)  # Now 7, 5, 5, 3

    # Combine both components into one graph
    G = nx.disjoint_union(G1, G2)

    return G


# Create and draw the graph
multigraph_2c = create_manual_multigraph_two_components()

# Plot the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(multigraph_2c, seed=42)  # Consistent layout
nx.draw_networkx(multigraph_2c, pos, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700,
                 font_size=10)
plt.title('Multigraph with 2 Connected Components')
plt.show()
