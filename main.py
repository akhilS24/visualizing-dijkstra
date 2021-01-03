#dijkstra algorithm for single source shortest path

import pygame as pg
import func
from graph import *
import math
import threading
from dijkstra import *


pg.init()


screen_height = 800
screen_width = 800

pg.display.set_caption('dijkstra')

Global_Font = pg.font.SysFont('arial', 30)


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
			self.nodes.append(Node_(self.graph.nodes[i] ,round(self.cell_width/4), (round(((2*coordinate[1]+1)/2)*self.cell_width), round(((2*coordinate[0]+1)/2)*self.cell_height)), (0, 255, 0), i, False))

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


	def find_active_node(self):
		mouse_x, mouse_y = pg.mouse.get_pos()
		for node in self.nodes:
			if (mouse_x > node.position[0]-node.radius and mouse_x < node.position[0]+node.radius) and (mouse_y > node.position[1]-node.radius and mouse_y < node.position[1]+node.radius):
				return node





class Node_:
	def __init__(self, node, radius, position, color, index, is_source_dest):
		self.radius = radius
		self.node = node
		self.position = position
		self.color = color
		self.index = index
		self.fontColor = (0, 0, 255)
		self.Font = [pg.font.SysFont('impact', self.radius), pg.font.SysFont('arial', round(self.radius/2), italic=True)]
		self.is_source_dest = is_source_dest

	def draw(self, window):
		pg.draw.circle(window, self.color, self.position, self.radius)
		txt1 = self.Font[0].render(f'{self.index}', True, self.fontColor)
		window.blit(txt1, (self.position[0]-txt1.get_width()/2, self.position[1]-txt1.get_height()/2))

		mouse_x, mouse_y = pg.mouse.get_pos()
		if (mouse_x > self.position[0]-self.radius and mouse_x < self.position[0]+self.radius) and (mouse_y > self.position[1]-self.radius and mouse_y < self.position[1]+self.radius) or self.is_source_dest:
			# pg.draw.circle(window, [0, 0, 255], self.position, self.radius, 2)
			self.color = (255, 255, 255)
		else:
			self.color = (0, 255, 0)

		txt2 = self.Font[1].render(f'{self.node.node_dist}', True, (255, 255, 255))
		window.blit(txt2, (self.position[0], self.position[1]-self.radius*(3/2)))

	def make_source_dest(self):
		self.is_source_dest = True




class Edge_:
	def __init__(self, edge, start, stop, color, radius):
		self.radius = radius
		self.edge = edge
		self.start_coordinate = start
		self.stop_coordinate = stop
		self.Font1 = pg.font.SysFont('arial', round(self.radius/2), italic=True)
		self.color = color
	def draw(self, window):
		pg.draw.circle(window, self.color[1], self.start_coordinate, self.radius, 3)
		pg.draw.line(window, self.color[0], self.start_coordinate, self.stop_coordinate, 1)
		pg.draw.circle(window, self.color[1], self.stop_coordinate, self.radius, 3)
		txt = self.Font1.render(f'{self.edge.edge_weight}', True, (255, 255, 255))
		window.blit(txt, ((self.start_coordinate[0]+self.stop_coordinate[0])/2, (self.start_coordinate[1]+self.stop_coordinate[1])/2))

def draw_process(window, node_list, spt_set, edge_list, grid):
	for node in spt_set:
		node.draw(window)

	for edge in edge_list:
		edge.draw(window)



def draw_commands(window, source_dest):
	if len(source_dest) == 0:
		command = 'Choose source'
	elif len(source_dest) == 1:
		command = 'Choose destination'
	elif len(source_dest) == 2:
		command = 'Press Enter'

	txt = Global_Font.render(command, True, (255, 255, 255))
	window.blit(txt, (round((screen_width - txt.get_width())/2), screen_height - txt.get_height()))

	


def main():

	graph = Graph()

	node_cnt = int(input('enter no of nodes: '))
	for x in range(node_cnt):
		graph.add_node(math.inf)

	edge = int(input('Enter no of edges: '))


	print('Node numbering starts from 0\n')

	for x in range(edge):
		
		print(f'edge{x}: ')
		print('~~~~~')
		node_index1 = int(input(f'start_node: '))
		node_index2 = int(input(f'end_node: '))
		edge_weight = int(input(f'edge_weight: '))
		print('')
		assert(type(node_index1) == int and type(node_index2) == int and type(edge_weight) == int)
		graph.add_edge(node_index1, node_index2, edge_weight)



	#pygame window

	
	WINDOW  = pg.display.set_mode((screen_width, screen_height))	

	grid = Grid(graph)

	_selected = False
	run = True
	alg_start = False

	source_dest = []
	spt_set = []
	node_list = []
	edge_list = []


	while run:

		WINDOW.fill((0,0,0))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False 
				pg.quit()
			
			if event.type == pg.MOUSEBUTTONDOWN:
				if not _selected:
					active_node = grid.find_active_node()
					if len(source_dest) < 2:
						source_dest.append(active_node)
						active_node.make_source_dest()

						if len(source_dest) == 2:
							_selected = True
						

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RETURN:
					if _selected and not alg_start:
						thread = threading.Thread(target=dijkstra, daemon=True, args = (grid, source_dest[0], spt_set, node_list, edge_list))
						thread.start()
						alg_start = True


		if not alg_start:
			grid.draw(WINDOW)
			draw_commands(WINDOW, source_dest)
		if _selected and alg_start:
			draw_process(WINDOW, node_list, spt_set, edge_list, grid)

		pg.display.update()


if __name__ == "__main__":
	main()