# pip install PyOpenGL
# pip install pygame
# pip install pygame==2.0.0.dev6 (for python 3.8.x)
# pip install numpy
# Python 3.8

from utils import *

def main():
	scale = 1
	width, height = scale * 800, scale * 400

	pygame.init()
	pygame.display.set_caption('C.G. I')
	
	display_openGL(width, height, scale)
	# glColor3f(1.0, 0, 0)

	# -------
	# Point (pixel)
	# -------
	x = 0
	y = 0
	set_pixel(x, y, 255/255, 255/255, 255/255, scale)
	# set_pixel(1, 0, 1, 0, 0, scale)
	# set_pixel(1, 1, 0, 1, 0, scale)
	# set_pixel(0, 1, 0, 0, 1, scale)

	# -------
	# Line
	# -------

	# DDA(0, 0, 10, 0, 0/255, 255/255, 0/255, scale)
	# DDA(0, 0, 0, 10, 0/255, 255/255, 0/255, scale)
	# Bressennham(0, 0, 6, 7, 0, 1, 0, scale)

	# -------
	# Circle
	# -------
	# Circle2v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circle4v(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# Circulo4(0, 0, 100, 255/255, 0/255, 0/255, scale)
	# Circle8v(0, 0, 100, 255/255, 0/255, 0/255, scale)
	# Circle(0, 0, 50, 255/255, 0/255, 0/255, scale)
	# CirclePM(0, 0, 60, 255/255, 0/255, 0/255, scale)

	# -------
	# Filling
	# -------
	# vertices = [(0, 0), (0, 6), (5, 6), (5, 0)]
	# vertices = [(1, 1), (1, 5), (4, 5), (4, 1)]
	# vertices = [(1, 1), (1, 50), (40, 50), (40, 1)]
	# vertices = [(1, 1), (1, 50), (40, 50), (40, 1)]
	# vertices = [(1, 1), (25, 50), (50, 50)]
	# vertices = [(1, 1), (1, 50), (30, 50), (30, 30), (50, 30), (50, 1)]
	""" vertices = [
		(40, 20), (30, 20), (30, 30), (20, 30), (20, 40), 
		(-20, 40), (-20, 30), (-30, 30), (-30, 20), (-40, 20),
		(-40, -20), (-30, -20), (-30, -30), (-20, -30), (-20, -40),
		(20, -40), (20, -30), (30, -30), (30, -20), (40, -20)
	] """

	""" xi = 20
	yi = 25

	DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)

	SimpleSeedFill(width, height, scale, vertices, xi, yi, 255/255, 0/255, 0/255) """

	# rgb = glReadPixels(width/2 +x-1, height/2+y-1, scale, scale, GL_RGB, GL_UNSIGNED_BYTE, None)
	# print(list(rgb))

	# Fill Triangle
	# vertices = [(1, 1), (40, 40), (80, 1)]
	# FillTriangle(vertices, 255/255, 0/255, 0/255, scale)
	# DrawPolygon(vertices, 255/255, 0/255, 0/255, scale)

	# -------
	# Transformation
	# -------
	# vertices_p1 = [[0, 0, 1], [48, 0, 1], [48, 48, 1], [0, 48, 1]]
	# vertices_p1 = [[0, 0, 1], [30, 30, 1], [60, 0, 1]]
	# vertices_p1 = [[10, 10, 1], [40, 30, 1], [60, 0, 1]]

	vertices_p1 = [[20, 10, 1], [20, 30, 1], [60, 30, 1], [60, 10, 1]]

	DDA(0, 0, 60, 60, 255/255, 255/255, 255/255, scale)


	DrawPolygon_(vertices_p1, 255/255, 0/255, 0/255, 1)
	# DrawPolygon_(vertices_p1, 0/255, 255/255, 0/255, 2)
	# DrawPolygon_(vertices_p1, 0/255, 0/255, 255/255, 1)
	# print(vertices_p1)

	# Traslate
	""" tx = 30
	ty = 30
	vertices_p2 = Traslate(vertices_p1, tx, ty)
	print(vertices_p2)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale) """
	
	# Rotation
	""" angle = 180
	vertices_p2 = Rotation(vertices_p1, angle)
	print(vertices_p2)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale) """

	
	# Plus
	""" vertices_p1 = [[100, 0, 1], [0, 100, 1], [-100, 0, 1]]
	for angle in range(0, 360, 15):
		vertices_p2 = Rotation(vertices_p1, angle)
		# print(vertices_p2)
		r, g, b = floatRgb(angle, 0, 360)
		DrawPolygon_(vertices_p2, r, g, b, scale)
		print(r, g, b) """

	# Scaling
	""" sx = 2
	sy = 1
	
	vertices_p2 = Scaling(vertices_p1, sx, sy)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale) """

	# Reflection
	""" # vertices_p2 = ReflectionX(vertices_p1)
	vertices_p2 = ReflectionY(vertices_p1)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale) """

	# Deformation
	""" vertices_p2 = DeformationX(vertices_p1, 2)
	vertices_p2 = DeformationY(vertices_p1, 2)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale) """

	# Testing
	vertices_p2 = TransCVR(vertices_p1)
	DrawPolygon_(vertices_p2, 0/255, 255/255, 0/255, scale)
	print(vertices_p2)
	
	# GaMoster(0, 0)
	print("Finish...")
	glFlush()
	pygame.display.flip()
	 
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

if __name__ == '__main__':
	main()