# pip install PyOpenGL PyOpenGL_accelerate
import pygame
from pygame.locals import*

from OpenGL.GL import*
from OpenGL.GLU import*
#graficamos el cubo
def Bresenham3D(x1, y1, z1, x2, y2, z2): 
    ListOfPoints = [] 
    ListOfPoints.append((x1/200, y1/200, z1/200)) 
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
            ListOfPoints.append((x1/200, y1/200, z1/200)) 
  
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
            ListOfPoints.append((x1/200, y1/200, z1/200)) 
  
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
            ListOfPoints.append((x1/500, y1/500, z1/500)) 
    return ListOfPoints 
  
  
def Obtenervertices(x1,y1,z1,x2,y2,z2): 
    ListOfPoints = Bresenham3D(x1, y1, z1, x2, y2, z2) 
    return ListOfPoints


def Cube(vertices, edges, R, G, B, size):
    #arista 1
    puntos=Obtenervertices(0,0,5,0,5,0)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 255/255, 0/255, 0/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 2
    puntos=Obtenervertices(0,5,5,5,5,0)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 3
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 4
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 5
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 6
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 7
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 8
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])

    #arista 9
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 10
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 11
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])
    #arista 12
    puntos=Obtenervertices(20,0,10,0,10,30)
    
    for x in range(len(puntos)):
        set_pixel(puntos[x][0], puntos[x][1], puntos[x][2], 1/255, 255/255, 1/255, 1)
        print(puntos[x][0], puntos[x][1], puntos[x][2])
		#print(vertices[vertex])

def set_pixel(x, y, z, R, G, B, size):
	glColor3f(R, G, B)
	glPointSize(size)
	glBegin(GL_POINTS)
	glVertex3f(x, y, z)
	glEnd()
	# pygame.display.flip()
	#pygame.time.wait(100)




def main():
	pygame.init()
	display = (800, 800)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	gluPerspective(45, (display[0]/display[1]), 0.1,50)

	glTranslatef(0.0, 0.0, -10)
	# glTranslatef(1, 1, 1)

	# Main
	set_pixel(0, 0, 0, 255/255, 255/255, 255/255, 1)

	vertices = (
		(1, 1, 1),
		(1, 1, -1),
		(1, -1, -1),
		(1, -1, 1),
		(-1, 1, 1),
		(-1, -1, -1),
		(-1, -1, 1),
		(-1, 1, -1)
	)

    #X ES HACIA LA DERECHA
    #-X ES HACIA LA DERECHA
    #Y ES HACIA ARRIBA
    #-Y ES HACIA ABAJO
    #Z ES HACIA LA CAMARA
    #-Z FONDO
	edges = (
		(0, 1),
		(0, 3),
		(0, 4),
		(1, 2),
		(1, 7),
		(2, 5),
		(2, 3),
		(3, 6),
		(4, 6),
		(4, 7),
		(5, 6),
		(5, 7)
	)
	#GraficarEjes(255/255, 0/255, 0/255, 1)
	#pygame.display.flip()
	Cube(vertices, edges, 255/255, 0/255, 0/255, 1)
	pygame.display.flip()
	
	x = 0
	y = 0
	z = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		

#if _name_ == "_main_":
main()
