from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""


def parse_file(fname, points, transform, screen, color):
    f = open(fname, "r")
    commands = f.readlines()
    curr = 0

    while curr < len(commands):
        command = commands[curr]
        if curr + 1 != len(commands):
            next = commands[curr + 1]

        #line
        if command == 'line\n':
            p = next.split()
            add_edge(points, int(p[0]), int(p[1]), int(p[2]), int(p[3]), int(p[4]), int(p[5]))

        #ident
        elif command == 'ident\n':
            ident(transform)

        #scale
        elif command == 'scale\n':
            p = next.split()
            matrix_mult(make_scale(int(p[0]), int(p[1]), int(p[2])), transform)

        #translate
        elif command == 'move\n':
            p = next.split()
            matrix_mult(make_translate(int(p[0]), int(p[1]), int(p[2])), transform)

        #rotate
        elif command == 'rotate\n':
            p = next.split()
            var = p[0]
            angle = int(p[1])
            if var == 'x':
                matrix_mult(make_rotX(angle), transform)
            elif var == 'y':
                matrix_mult(make_rotY(angle), transform)
            elif var == 'z':
                matrix_mult(make_rotZ(angle), transform)

        #apply
        elif command == 'apply\n':
            matrix_mult(transform, points)

        #display
        elif command == 'display\n':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        #save
        elif command == 'save\n':
            name = next.strip()
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, name)

        #quit
        elif command == 'quit\n':
            break

        curr += 1

    f.close()
