import pyglet
import colorsys
from pyglet import resource
import math
import random
from pyglet import window
from pyglet import canvas
from pyglet.window import key
from GameObjects import GameObject, preload_image
from math import atan2,degrees
from GameWindow import GameWindow

platform = pyglet.window.get_platform()
display = platform.get_default_display()
default_screen = display.get_default_screen()

def update(dt):
	if window.window_exists == False:
		window.close()
		pyglet.app.exit()

window = GameWindow(default_screen.width,default_screen.height, "Game Final", resizable = False, style=window.Window.WINDOW_STYLE_BORDERLESS)
window.set_fullscreen()
pyglet.clock.schedule_interval(window.update, window.frame_rate)

pyglet.app.run()