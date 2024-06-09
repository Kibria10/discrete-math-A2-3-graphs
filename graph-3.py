import networkx as nx
import matplotlib.pyplot as plt
from sympy import isprime

# Define a function to generate a graph based on the prime sum rule
def generate_prime_graph(num_vertices):
    G = nx.Graph()
    G.add_nodes_from(range(num_vertices))
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if isprime(i + j):
                G.add_edge(i, j)
    return G

# Generate the graph G10
G10 = generate_prime_graph(11)

# Plot G10
plt.figure(figsize=(10, 7))
nx.draw_networkx(G10, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700, font_size=9)
plt.title('Graph G10')
plt.show()

# Check if G10 is connected
is_connected_G10 = nx.is_connected(G10)

# Generate the graph G11
G11 = generate_prime_graph(12)

# Plot G11
plt.figure(figsize=(10, 7))
nx.draw_networkx(G11, with_labels=True, node_color='lightgreen', font_weight='bold', node_size=700, font_size=9)
plt.title('Graph G11')
plt.show()

# Output results for connectedness and Eulerian properties
is_connected_G11 = nx.is_connected(G11)
is_eulerian_G10, is_eulerian_G11 = nx.is_eulerian(G10), nx.is_eulerian(G11)
is_connected_G10, is_eulerian_G10, is_connected_G11, is_eulerian_G11
