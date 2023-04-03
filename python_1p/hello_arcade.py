import arcade
import pyglet
import numpy as np

#Definicion de constantes
screen = pyglet.canvas.get_display().get_default_screen()
SCREEN_WIDTH = screen.width
SCREEN_HEIGHT = screen.height
SCREEN_TITLE = "hola arcade"

#crear nueva ventana
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT ,SCREEN_TITLE)

#cambia el color de fondo
arcade.set_background_color(arcade.color.AMAZON)

#iniciar render
arcade.start_render()

#funciones para dibujar

for i in range(12):
    angle = i * 30
    x = SCREEN_WIDTH/2 + 100 * np.sin(np.deg2rad(angle))
    y = SCREEN_HEIGHT/2 + 100 * np.cos(np.deg2rad(angle))
    arcade.draw_circle_filled(x, y, 20, arcade.color.YELLOW)

#cesped
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT/2, 0, arcade.color.GREEN)

"""
#dibujar la casa
arcade.draw_lrtb_rectangle_filled(150, 450, 400, 100, arcade.color.GRAY)
arcade.draw_triangle_filled(150, 400, 450, 400, 300, 550, arcade.color.ORANGE)
arcade.draw_rectangle_filled(225, 200, 50, 100, arcade.color.BROWN)
arcade.draw_rectangle_filled(375, 200, 50, 100, arcade.color.BROWN)
"""

#finalizar render
arcade.finish_render()

#correr el parograma
arcade.run()
