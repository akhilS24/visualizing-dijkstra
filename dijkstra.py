import math
from graph import *

#DIJKSTRA ALGO
def dijkstra(graph, root_index, spt_set, node_list):
	

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
		graph.add_node(math.inf)

	edge = int(input('Enter no of edges: '))

	with open('data.txt', mode="r") as f: 
		for each_line in f:
			data_list = each_line.split(' ')
			for i in range(len(data_list)):
				data_list[i] = int(data_list[i])
			assert(data_list[0]<node_cnt and data_list[1]<node_cnt)
			graph.add_edge(data_list[0], data_list[1], data_list[2])


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



		