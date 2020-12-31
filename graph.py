"""GRAPH DATA STRUCTURE"""

#Undirected graph
class Graph:
	def __init__(self):
		self.adj_matrix = []
		self.edges = []
		self.nodes = []
		self.node_num = 0
		self.edge_num = 0

	#adds a new edge - provide both new node indices and an edge weight
	def add_edge(self, node1_index, node2_index, edge_weight):

		node1 = self.nodes[node1_index]
		node2 = self.nodes[node2_index]
		self.edges.append(Edge(edge_weight, node1, node2))

		self.adj_matrix[node1_index][node2_index] = 1
		self.adj_matrix[node2_index][node1_index] = 1

		self.edge_num+=1

	#adds a new node into the graph
	def add_node(self, node_data):

		self.nodes.append(Node(self.node_num, node_data))

		for each in self.adj_matrix:
			each.append(0)

		new_list = []
		for i in range(self.node_num+1):
			new_list.append(0)
		self.adj_matrix.append(new_list)

		self.node_num+=1
		
	#finds and return an edge between two nodes if it exists
	def find_edge(self, node1, node2):
		for edge in self.edges:
			if (edge.start_node.node_index == node1.node_index and edge.end_node.node_index == node2.node_index) or (edge.start_node.node_index == node2.node_index and edge.end_node.node_index == node1.node_index):
				return edge


	#prints the adj matrix representation of the graph
	def print_adj_matrix(self):
		for each in self.adj_matrix:
			print(f'{each}')

	#print all the nodes 
	def print_all_nodes(self):
		for node in self.nodes:
			node.Print()

	#print all the edges
	def print_all_edges(self):
		for edge in self.edges:
			edge.Print()

#Node Class. An instance of this cls is used as a node representation in graph
class Node:
	def __init__(self, index, dist):
		self.node_index = index
		self.node_dist = dist

	def Print(self):
		print(f'node {self.node_index} : data : {self.node_dist}')

#Edge Class. An instance of this cls is used as a edge representation in graph
class Edge:
	def __init__(self, weight, node_start, node_end):
		self.edge_weight = weight
		self.start_node = node_start
		self.end_node = node_end

	def Print(self):
		print(f'edge connecting {self.start_node.node_index} and {self.end_node.node_index}; data: {self.edge_weight}')
