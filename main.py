from display import *
from draw import *
from parser_1 import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file('script.txt', edges, transform, screen, color)
