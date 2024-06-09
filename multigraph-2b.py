import networkx as nx
import matplotlib.pyplot as plt

# Degree sequence provided
degrees = [7, 7, 5, 5, 5, 3, 2, 2]

# Function to create a multigraph from a degree sequence
def create_multigraph(degrees):
    G = nx.MultiGraph()
    G.add_nodes_from(range(len(degrees)))  # add vertices

    # Sort vertices by descending degree
    sorted_vertices = sorted((idx for idx in range(len(degrees))), key=lambda x: degrees[x], reverse=True)

    # Attempt to create edges respecting the multigraph properties (multiple edges allowed, no loops)
    while any(degrees):
        # Start with the vertex with the highest remaining degree
        for i in sorted_vertices:
            if degrees[i] == 0:
                continue
            for j in sorted_vertices:
                if i != j and degrees[i] > 0 and degrees[j] > 0:
                    G.add_edge(i, j)
                    degrees[i] -= 1
                    degrees[j] -= 1
                    if degrees[i] == 0:
                        break
    return G

# Generate the multigraph
multigraph = create_multigraph(degrees.copy())

# Plot the multigraph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(multigraph, seed=42)  # for consistent layout
nx.draw_networkx(multigraph, pos, with_labels=True, node_color='orange', font_weight='bold', node_size=700, font_size=10)
plt.title('Multigraph without Loop, 1 Connected Component')
plt.show()
