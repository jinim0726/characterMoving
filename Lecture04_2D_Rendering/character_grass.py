from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    x = 400
    y = 90
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)

    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)

    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)

    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)
    x = 400
    y = 90
    r = 270
    while(r < 360):
        clear_canvas_now()
        grass.draw_now(400,30)
        y = math.sin(r / 360 * 2 * math.pi) * 250 + 300 
        x = math.cos(r / 360 * 2 * math.pi) * 380 + 400
        character.draw_now(x,y)
        delay(0.01)
        r = r + 1
    r = 0
    while(r < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        y = math.sin(r / 360 * 2 * math.pi) * 250 + 300 
        x = math.cos(r / 360 * 2 * math.pi) * 380 + 400
        character.draw_now(x,y)
        delay(0.01)
        r = r + 1

close_canvas()
