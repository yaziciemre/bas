import matplotlib.pyplot as plt

import networkx as nx
G = nx.Graph()

G.add_node(1)
G.add_nodes_from([2, 3])

G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

G.add_edge(1, 2)
G.add_edge(1, 7)
G.add_edge(1, 8)
G.add_edge(1, 9)
G.add_edge(1, 11)

G.add_edge(11, 12)
G.add_edge(11, 13)
G.add_edge(11, 14)

G.add_edge(14, 15)
G.add_edge(14, 16)
G.add_edge(14, 17)
G.add_edge(14, 18)

G.add_edge(14, 1)


G.add_edge(19, 20)
G.add_edge(19, 21)
G.add_edge(19, 22)
G.add_edge(19, 23)
G.add_edge(19, 11)


G.add_edge(40, 12)
G.add_edge(41, 12)
G.add_edge(42, 12)

G.add_edge(43, 42)
G.add_edge(43, 1)
G.add_edge(44, 1)
G.add_edge(45, 1)
G.add_edge(46, 44)
G.add_edge(13, 21)
G.add_edge(16, 19)
G.add_edge(16, 21)
G.add_edge(16, 22)


G.add_edge(3, 46)
G.add_edge(2, 46)
G.add_edge(7, 3)

e = (2, 3)
G.add_edge(*e)  # unpack edge tuple


# G = nx.petersen_graph()
nx.draw(G, with_labels=True, font_weight='bold', font_color='white')
print(nx.degree_centrality(G))


def draw_communities(G, membership, pos):
	"""Draws the nodes to a plot with assigned colors for each individual cluster
	Parameters
	----------
	G : networkx graph
	membership : list
		A list where the position is the student and the value at the position is the student club membership.
		E.g. `print(membership[8]) --> 1` means that student #8 is a member of club 1.
	pos : positioning as a networkx spring layout
		E.g. nx.spring_layout(G)
	"""
	fig, ax = plt.subplots(figsize=(16, 9))

	# Convert membership list to a dict where key=club, value=list of students in club
	club_dict = defaultdict(list)
	for student, club in enumerate(membership):
		club_dict[club].append(student)

	# Normalize number of clubs for choosing a color
	norm = colors.Normalize(vmin=0, vmax=len(club_dict.keys()))

	for club, members in club_dict.items():
		nx.draw_networkx_nodes(G, pos,
							   nodelist=members,
							   node_color=cm.jet(norm(club)),
							   node_size=500,
							   alpha=0.8,
							   ax=ax)

	# Draw edges (social connections) and show final plot
	plt.title("Zachary's Karate Club")
	nx.draw_networkx_edges(G, pos, alpha=0.5, ax=ax)

p = nx.shortest_path(G, source=46)  # target not specified
print(p)



plt.show()