import pygame as pg
import random

class Cuadrao:
    def __init__(self, x, y, w=25, h=25, color = (255, 255, 255)):
        self.x = x                         #"x" e "y" son las coordinadas de posición en las que empezamos
        self.y = x
        self.w = w                          #w y h dimensiones del cuadrao
        self.h = h 
        self.color = color 

        self.vx = 0                          #velocidades
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx        
        self.vy = vy 
    
    def mover(self, xmax, ymax):              #los dos últimos parámetros serán para indicar el tamaño de la pantalla
        self.x += self.vx                     #cambio la posición del cuadrado en función de la velocidad
        self.y += self.vy                     #al añadirle vx a x cambiará la c.posición (se moverá)
        
        if self.x <= 0 or self.x >= xmax - self.w:               #cuando llegué al límite de la pantalla - el ancho de el cuadrado para que no se hunda
            self.vx *= -1                           #a la velocidad le cambio de signo para que se mueva en la otra dirección
        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1


pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Cuadraicos rebotando")

cuadrao = Cuadrao(400, 300, color = (255, 255, 0))
cuadrao.velocidad(5, 5)
cuadrao2 = Cuadrao(300, 300, 35, 35, color = (0, 255, 0))
cuadrao2.velocidad(random.randint(-10, 10), random.randint(-10, 10))

game_over = False

#bucle presentación de pantalla
while not game_over: 
    lista_eventos = pg.event.get()
    for evento in lista_eventos:       
      if evento.type == pg.QUIT:        
        game_over = True
    
    pantalla_principal.fill((0, 0, 255))   
    
    cuadrao.mover(800, 600)
    cuadrao2.mover(800, 600)

    pg.draw.rect(pantalla_principal, cuadrao.color, (cuadrao.x, cuadrao.y, cuadrao.w, cuadrao.h))      #para pintar los cuadraos en la pantalla
    pg.draw.rect(pantalla_principal, cuadrao2.color, (cuadrao2.x, cuadrao2.y, cuadrao2.w, cuadrao2.h))


    pg.display.flip()                                   #para mandarla al monitor

pg.quit()                                #que tumbe todos los sistemas que hemos levantado 

