import networkx as nx
import random

def check_isomorphism(G1, G2):
    # Check if the graphs are isomorphic
    if nx.is_isomorphic(G1, G2):
        print("Графи ізоморфні")
        # If isomorphic, remove a random edge from G2
        edge_to_remove = random.choice(list(G2.edges()))
        G2.remove_edge(*edge_to_remove)
        print(f"Кут {edge_to_remove} видалено з G2.")
    else:
        print("Графи не ізоморфні")
        # If not isomorphic, add a new node to G2 and connect it to all but one node
        new_node = max(G2.nodes()) + 1
        G2.add_node(new_node)
        neighbors = list(G2.nodes())[:-1]
        G2.add_edges_from([(new_node, neighbor) for neighbor in neighbors])
        print(f"Нова нода {new_node} була додана до G2.")


    if nx.is_isomorphic(G1, G2):
        print("Після модифікації графіки тепер ізоморфні!")
    else:
        print("Модифікація не була успішною для встановлення ізоморфізму.")

# Create two example graphs
G1 = nx.Graph()
G1.add_edges_from([(0, 2), (1, 6), (1, 4), (3, 4), (4, 5)])

G2 = nx.Graph()
G2.add_edges_from([(1, 2), (2, 3), (3, 2), (2, 1)])

# Check for isomorphism and modify the graphs if necessary
check_isomorphism(G1, G2)

# Print the updated graphs
print("G1: ", G1.edges())
print("G2: ", G2.edges())