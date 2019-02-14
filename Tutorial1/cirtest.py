import arcade
from random import randint
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
circle_size = 1
size_direction = 1
circle_xs = []
circle_ys = []
num_circles = 100
 
def random_locations():
    for i in range(num_circles):
        circle_xs.append(randint(10,SCREEN_WIDTH-10))
        circle_ys.append(randint(10,SCREEN_HEIGHT-10))
 
def on_draw(delta_time):
    global circle_size, size_direction
 
    circle_size += size_direction
    if circle_size > 50:
        size_direction = -1
    elif circle_size == 1:
        size_direction = 1
 
    arcade.start_render()
 
    for x,y in zip(circle_xs, circle_ys):
        arcade.draw_circle_outline(x, y, circle_size, arcade.color.BLACK)
 
 
def main():
    random_locations()
 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)
 
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
 
if __name__ == '__main__':
    main()
