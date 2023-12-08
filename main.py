import pygame as pg
import sys
import os
import time

pg.init()

# window config
win_width, win_height = 600,400
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Mi ventana")

# Centro de la pantalla
centro_x, centro_y = win_width//2, win_height//2

# Obtener la ruta del directorio actual del script
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa a la carpeta de imágenes
ruta_sprite_jugador = os.path.join(dir_actual, "sprites", "playerSprite.png")
ruta_boton_ataque = os.path.join(dir_actual, "sprites", "attackbuttonSprite.png")

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)

class Player():
    def __init__(self):
        #Stats
        self.vida = 100
        self.ataque = 10

class Monster(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar sprite
        self.image = pg.image.load(ruta_sprite_jugador)
        # Obtener rectangulo del sprite
        self.rect = self.image.get_rect()
        # Configurar la posición inicial del sprite
        self.rect.x = 100
        self.rect.y = 100

        # Stats
        self.vida = 100
        self.ataque = 5

class Button(pg.sprite.Sprite):
    def __init__(self, spriteDir, x,y):
        super().__init__()
        # Cargar sprite
        self.spriteDir = spriteDir
        self.image = pg.image.load(self.spriteDir)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Inicializar la fuente
font = pg.font.Font(None, 36)

# Funcion para mostrar texto
def displayText(text, x, y):
    rendered_text = font.render(text, True, black)
    window.blit(rendered_text,(x,y))

# Crear un grupo de sprites
Sprites = pg.sprite.Group()

# Crear un objeto tipo player
newPlayer = Player()
# Crear un objeto monster
newMonster = Monster()
# Objeto boton
attackButton = Button(ruta_boton_ataque, 200, 200)

# Agregar mi objeto al grupo de sprites
Sprites.add(newMonster)
Sprites.add(attackButton)

esMiTurno = True

#sistema turnos
def turnos():
    global esMiTurno
    if((esMiTurno == True) & (newMonster.vida > 0) & (newPlayer.vida > 0)):
        print("Es mi turno")
        print(str(esMiTurno) + str(newMonster.vida) + str(newPlayer.vida))
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                newMonster.vida -= newPlayer.ataque   
                esMiTurno = False
    elif((esMiTurno == False) & (newMonster.vida > 0) & (newPlayer.vida > 0)):
        print("Es turno del monstruo")
        print(str(esMiTurno) + str(newMonster.vida) + str(newPlayer.vida))
        newPlayer.vida -= newMonster.ataque
        esMiTurno = True
    else:
        print("Terminó la pelea")
        print(str(esMiTurno) + str(newMonster.vida) + str(newPlayer.vida))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        turnos()

    #Obtener valor de vida del personaje
    vidaMonster = newMonster.vida
    vidaPlayer = newPlayer.vida

    # Dibujar en la pantalla
    window.fill((white))
    Sprites.draw(window)
    displayText(f"Vida Enem.: {vidaMonster}", 10, 10)
    displayText(f"Vida: {vidaPlayer}", 300,10)
    # Actualizar pantalla
    pg.display.flip()
