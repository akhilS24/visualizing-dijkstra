import math

#Undirected graph
class Graph:
	def __init__(self):
		self.adj_matrix = []
		self.edges = []
		self.nodes = []
		self.node_num = 0
		self.edge_num = 0


	def add_edge(self, node1_index, node2_index, edge_weight):

		node1 = self.nodes[node1_index]
		node2 = self.nodes[node2_index]
		self.edges.append(Edge(edge_weight, node1, node2))

		self.adj_matrix[node1_index][node2_index] = 1
		self.adj_matrix[node2_index][node1_index] = 1

		self.edge_num+=1


	def add_vertex(self, node_data):

		self.nodes.append(Node(self.node_num, node_data))

		for each in self.adj_matrix:
			each.append(0)

		new_list = []
		for i in range(self.node_num+1):
			new_list.append(0)
		self.adj_matrix.append(new_list)

		self.node_num+=1
		

	def find_edge(self, node1, node2):
		for edge in self.edges:
			if (edge.start_node.node_index == node1.node_index and edge.end_node.node_index == node2.node_index) or (edge.start_node.node_index == node2.node_index and edge.end_node.node_index == node1.node_index):
				return edge



	def print_adj_matrix(self):
		for each in self.adj_matrix:
			print(f'{each}')

	def print_all_nodes(self):
		for node in self.nodes:
			node.Print()

	def print_all_edges(self):
		for edge in self.edges:
			edge.Print()


class Node:
	def __init__(self, index, dist):
		self.node_index = index
		self.node_dist = dist

	def Print(self):
		print(f'node {self.node_index} : data : {self.node_dist}')


class Edge:
	def __init__(self, weight, node_start, node_end):
		self.edge_weight = weight
		self.start_node = node_start
		self.end_node = node_end

	def Print(self):
		print(f'edge connecting {self.start_node.node_index} and {self.end_node.node_index}; data: {self.edge_weight}')



#DIJKSTRA ALGO
def dijkstra(graph, root_index):
	spt_set = []
	node_list = []

	for node in graph.nodes:
		node_list.append(node)

	root = graph.nodes[root_index]
	root.node_dist = 0

	spt_set.append(root)
	node_list.remove(root)
	update_neighbours(graph, root)

	while len(node_list)!=0:
		u = select_min_dist_node(node_list)
		spt_set.append(u)
		node_list.remove(u)
		update_neighbours(graph, u)

#this function will update the adjacent nodes of node 'u'
def update_neighbours(graph, u):
	for i in range(graph.node_num):

		if graph.adj_matrix[u.node_index][i] == 1:

			neighbour = graph.nodes[i]
			edge = graph.find_edge(u, neighbour)

			if neighbour.node_dist > u.node_dist + edge.edge_weight:
				neighbour.node_dist = u.node_dist + edge.edge_weight


#this function will select node with min distance value from a list of nodes
def select_min_dist_node(node_list):
	min_val_node = node_list[0]
	for i in range(1, len(node_list)):
		if min_val_node.node_dist > node_list[i].node_dist:
			min_val_node = node_list[i]

	return min_val_node


def main():
	graph = Graph()

	node_cnt = int(input('enter no of nodes: '))
	for x in range(node_cnt):
		graph.add_vertex(math.inf)

	edge = int(input('Enter no of edges: '))

	with open('data.txt', mode="r") as f: 
		for each_line in f:
			data_list = each_line.split(' ')
			for i in range(len(data_list)):
				data_list[i] = int(data_list[i])
			assert(data_list[0]<node_cnt and data_list[1]<node_cnt)
			graph.add_edge(data_list[0], data_list[1], data_list[2])



	# for i in range(edge):
	# 	x, y = input(f'edge {i}: ').split(sep=' ')
	# 	x, y = int(x), int(y)
	# 	assert(x<node_cnt and y<node_cnt)
	# 	val = int(input(f'enter the {i}th edge val: '))
	# 	graph.add_edge(x, y, val)


	graph.print_all_nodes()
	graph.print_all_edges()
	graph.print_adj_matrix()


	source = int(input(f'enter the source: '))
	assert(source<node_cnt)

	dijkstra(graph, source)

	graph.print_all_nodes()
	graph.print_all_edges()
	graph.print_adj_matrix()


	


if __name__ == "__main__":
	main()



		