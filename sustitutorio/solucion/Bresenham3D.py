# pip install PyOpenGL PyOpenGL_accelerate

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def set_pixel(x, y, z, R, G, B, size):
	glColor3f(R, G, B)
	glPointSize(size)

	glBegin(GL_POINTS)
	glVertex3f(x, y, z)
	glEnd()
	# pygame.display.flip()
	# pygame.time.wait(100)

def Bresenham3D(p1, p2):
	# Transformaciones para escalar los valores del algoritmo de Bresenham3D a la escala de OpenGL
	r = 100
	x1, y1, z1, x2, y2, z2 = r * p1[0], r * p1[1], r * p1[2], r * p2[0], r *p2[1], r *p2[2]
	
	ListOfPoints = [] 
	ListOfPoints.append((x1, y1, z1))
	set_pixel(x1/r, y1/r, z1/r, 255/255, 0/255, 0/255, 1) 
	dx = abs(x2 - x1) 
	dy = abs(y2 - y1) 
	dz = abs(z2 - z1) 
	if (x2 > x1): 
		xs = 1
	else: 
		xs = -1
	if (y2 > y1): 
		ys = 1
	else: 
		ys = -1
	if (z2 > z1): 
		zs = 1
	else: 
		zs = -1

	# Driving axis is X-axis" 
	if (dx >= dy and dx >= dz):		 
		p1 = 2 * dy - dx 
		p2 = 2 * dz - dx 
		while (x1 != x2): 
			x1 += xs 
			if (p1 >= 0): 
				y1 += ys 
				p1 -= 2 * dx 
			if (p2 >= 0): 
				z1 += zs 
				p2 -= 2 * dx 
			p1 += 2 * dy 
			p2 += 2 * dz 
			ListOfPoints.append((x1, y1, z1))
			set_pixel(x1/r, y1/r, z1/r, 255/255, 0/255, 0/255, 1) 

	# Driving axis is Y-axis" 
	elif (dy >= dx and dy >= dz):	 
		p1 = 2 * dx - dy 
		p2 = 2 * dz - dy 
		while (y1 != y2): 
			y1 += ys 
			if (p1 >= 0): 
				x1 += xs 
				p1 -= 2 * dy 
			if (p2 >= 0): 
				z1 += zs 
				p2 -= 2 * dy 
			p1 += 2 * dx 
			p2 += 2 * dz 
			ListOfPoints.append((x1, y1, z1))
			set_pixel(x1/r, y1/r, z1/r, 255/255, 0/255, 0/255, 1) 

	# Driving axis is Z-axis" 
	else:		 
		p1 = 2 * dy - dz 
		p2 = 2 * dx - dz 
		while (z1 != z2): 
			z1 += zs 
			if (p1 >= 0): 
				y1 += ys 
				p1 -= 2 * dz 
			if (p2 >= 0): 
				x1 += xs 
				p2 -= 2 * dz 
			p1 += 2 * dy 
			p2 += 2 * dx 
			ListOfPoints.append((x1, y1, z1)) 
			set_pixel(x1/r, y1/r, z1/r, 255/255, 0/255, 0/255, 1) 
	return ListOfPoints 

def Cube(vertices, edges, R, G, B, size):
	glColor3f(R, G, B)
	for edge in edges:
		Bresenham3D(vertices[edge[0]], vertices[edge[1]])

def main():
	pygame.init()
	display = (800, 800)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -12)
	# glTranslatef(1, 1, 1)

	# Main
	set_pixel(1, 1, 1, 255/255, 255/255, 255/255, 2)
	set_pixel(1, 0, 0, 255/255, 255/255, 255/255, 2)
	# set_pixel(2, 2, 2, 255/255, 255/255, 255/255, 4)


	vertices = [
		(0, 0, 0),
		(1, 0, 0),
		(1, 1, 0),
		(0, 1, 0),
		(0, 0, 1),
		(1, 0, 1),
		(1, 1, 1),
		(0, 1, 1)
	]
	edges = [
		(0, 1),
		(1, 2),
		(2, 3),
		(0, 3),

		(4, 5),
		(5, 6),
		(6, 7),
		(4, 7),

		(0, 4),
		(1, 5),
		(2, 6),
		(3, 7)
	]

	Cube(vertices, edges, 255/255, 255/255, 0/255, 1)

	# Bresenham3D((0, 0, 0), (1, 1, 1))
	# Bresenham3D((0, 0, 0), (1, 0, 0))

	pygame.display.flip()
	
	x = 0
	y = 0
	z = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				if event.key == pygame.K_LEFT :
					print("K_LEFT")
					y -= 0.1
					glRotatef(y, 0, 1, 0)
					Cube(vertices, edges, 255/255, 255/255, 0/255, 1)
				elif event.key == pygame.K_RIGHT:
					print("K_RIGHT")
					y += 0.1
					glRotatef(y, 0, 1, 0)
					Cube(vertices, edges, 255/255, 255/255, 0/255, 1)
				elif event.key == pygame.K_UP :
					print("K_UP")
					x -= 0.1
					glRotatef(x, 1, 0, 0)
					Cube(vertices, edges, 255/255, 255/255, 0/255, 1)
				elif event.key == pygame.K_DOWN :
					print("K_DOWN")
					x += 0.1
					glRotatef(x, 1, 0, 0)
					Cube(vertices, edges, 255/255, 255/255, 0/255, 1)
				pygame.display.flip()

if __name__ == "__main__":
	main()