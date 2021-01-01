from main import *
import math
from graph import *
import threading

def main():
	

	graph = Graph()

	with open('data.txt', mode="r") as f: 
		node_cnt = int(f.readline())
		edge_cnt = int(f.readline())

		for x in range(node_cnt):
			graph.add_node(math.inf)

		for each_line in f:
			data_list = each_line.split(' ')
			for i in range(len(data_list)):
				data_list[i] = int(data_list[i])
			assert(data_list[0]<node_cnt and data_list[1]<node_cnt)
			graph.add_edge(data_list[0], data_list[1], data_list[2])



	#pygame window

	

	WINDOW  = pg.display.set_mode((screen_width, screen_height))	

	grid = Grid(graph)

	_selected = False
	run = True
	alg_start = False

	source_dest = []
	spt_set = []
	node_list = []



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
						thread = threading.Thread(target=dijkstra, daemon=True, args = (grid, source_dest[0], spt_set, node_list))
						thread.start()
						alg_start = True


		if not alg_start:
			grid.draw(WINDOW)
			draw_commands(WINDOW, source_dest)
		if _selected and alg_start:
			draw_process(WINDOW, node_list, spt_set, grid)

		pg.display.update()


if __name__ == "__main__":
	main()