import pygame as pg
import sys
import os

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

class Player(pg.sprite.Sprite):
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
        self.ataque = 10

class Button(pg.sprite.Sprite):
    def __init__(self, spriteDir, x,y):
        super().__init__()
        # Cargar sprite
        self.spriteDir = spriteDir
        self.image = pg.image.load(self.spriteDir)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Crear un grupo de sprites
Sprites = pg.sprite.Group()

# Crear un objeto tipo player
newplayer = Player()
# Objeto boton
attackButton = Button(ruta_boton_ataque, 200, 200)

# Agregar mi objeto al grupo de sprites
Sprites.add(newplayer)
Sprites.add(attackButton)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Dibujar en la pantalla
    window.fill((255,255,255))
    Sprites.draw(window)

    # Actualizar pantalla
    pg.display.flip()
