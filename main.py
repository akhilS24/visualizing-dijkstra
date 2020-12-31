#dijkstra algorithm for single source shortest path

import pygame as pg
import func
from graph import *
import math


pg.init()


screen_height = 600
screen_width = 600




class Grid:
	def __init__(self, graph):
	
		self.graph = graph
		self.order = func.find_min_order(self.graph.node_num)
		self.cell_width = round(screen_width/(self.order))
		self.cell_height = round(screen_height/(self.order))
		self.nodes = []
		self.node_count = self.graph.node_num
		self.edges = []
		self.edge_count = self.graph.edge_num
		self.grid_coordinates = func.create_grid_coordinates(self.order)


		
		for i in range(self.node_count):
			coordinate = func.get_cordinate(self.grid_coordinates)
			self.nodes.append(Node_(self.graph.nodes[i] ,round(self.cell_width/4), (round(((2*coordinate[1]+1)/2)*self.cell_width), round(((2*coordinate[0]+1)/2)*self.cell_height)), (0, 255, 0), i))

		for i in range(self.edge_count):
			edge = self.graph.edges[i]
			self.edges.append(Edge_(self.graph.edges[i], self.nodes[edge.start_node.node_index].position, self.nodes[edge.end_node.node_index].position, [(255, 255, 255), (255, 0, 0)], round(self.cell_width*(3/16))))


	def draw(self, window):
		for i in range(self.order):
			pg.draw.line(window, (255, 0, 0), (0, (i+1)*self.cell_height), (screen_width, (i+1)*self.cell_height), 1)
			pg.draw.line(window, (255, 0, 0), ((i+1)*self.cell_width, 0), ((i+1)*self.cell_width, screen_height), 1)

		for node in self.nodes:
			node.draw(window)

		for edge in self.edges:
			edge.draw(window)






class Node_:
	def __init__(self, node, radius, position, color, index):
		self.radius = radius
		self.node = node
		self.position = position
		self.color = color
		self.index = index
		self.fontColor = (0, 0, 255)
		self.Font1 = pg.font.SysFont('impact', self.radius)

	def draw(self, window):
		pg.draw.circle(window, self.color, self.position, self.radius)
		txt1 = self.Font1.render(f'{self.index}', True, self.fontColor)
		window.blit(txt1, (self.position[0]-txt1.get_width()/2, self.position[1]-txt1.get_height()/2))





class Edge_:
	def __init__(self, edge, start, stop, color, radius):
		self.radius = radius
		self.edge = edge
		self.start_coordinate = start
		self.stop_coordinate = stop
		self.color = color
	def draw(self, window):
		pg.draw.circle(window, self.color[1], self.start_coordinate, self.radius, 3)
		pg.draw.line(window, self.color[0], self.start_coordinate, self.stop_coordinate, 1)
		pg.draw.circle(window, self.color[1], self.stop_coordinate, self.radius, 3)

	


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


	graph.print_adj_matrix()
	graph.print_all_edges()
	graph.print_all_nodes()

	confirmation = input('Open pygame window?')

	#pygame window

	if confirmation == 'y' or confirmation == 'Y':

		WINDOW  = pg.display.set_mode((screen_width, screen_height))	

		grid = Grid(graph)

		run = True
		while run:

			WINDOW.fill((0,0,0))

			for event in pg.event.get():
				if event.type == pg.QUIT:
					run = false 
					pg.quit()

			grid.draw(WINDOW)

			pg.display.update()

	else:
		quit()


if __name__ == "__main__":
	main()