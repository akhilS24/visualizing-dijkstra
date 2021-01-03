import math
from graph import *
import time

#DIJKSTRA ALGO
def dijkstra(grid, root, spt_set, node_list, edge_list):
	

	for node in grid.nodes:
		node_list.append(node)

	root.node.node_dist = 0

	spt_set.append(root)
	node_list.remove(root)
	update_neighbours(grid.graph, root.node)

	time.sleep(1)

	while len(node_list)!=0:
		u = select_min_dist_node(node_list)
		spt_set.append(u)
		node_list.remove(u)
		add_edges(grid, spt_set, edge_list, u)
		update_neighbours(grid.graph, u.node)

		time.sleep(1)


	print_graph(grid.graph)


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
		if min_val_node.node.node_dist > node_list[i].node.node_dist:
			min_val_node = node_list[i]

	return min_val_node



def add_edges(grid, spt_set, edge_list, u):
	for node_ in spt_set:
		for edge_ in grid.edges:
			if (edge_.edge.start_node == u.node and edge_.edge.end_node == node_.node) or (edge_.edge.start_node == node_.node and edge_.edge.end_node == u.node):
				edge_list.append(edge_)



		