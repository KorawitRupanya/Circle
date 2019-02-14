import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
vx = 2
vy = 1
x = 300
y = 300
 
def on_draw(delta_time):
    arcade.start_render()
 
    global x, y, vx, vy
 
    x += vx
    y += vy

    if x > SCREEN_WIDTH - 20  \
        or x < 20 : 
      vx *= -1
    if y > SCREEN_HEIGHT - 20 \
        or y < 20 :
       vy *= -1

 
    arcade.draw_circle_outline(x, y, 20, arcade.color.BLACK) 
 
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)
 
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
 
if __name__ == '__main__':
    main()
