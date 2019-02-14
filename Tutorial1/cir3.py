import arcade
from random import randint

class Circle:
    def __init__(self, x, y, vx, vy, r=20):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
 
    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x > SCREEN_WIDTH - self.r  \
                or self.x < self.r : 
            self.vx *= -1
        if self.y > SCREEN_HEIGHT - self.r \
                or self.y < self.r :
            self.vy *= -1
        
    def draw(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   self.r, arcade.color.BLACK)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

circles = []
n = 10
 
def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),
                        randint(100, SCREEN_HEIGHT-100),
                        randint(-5,5),
                        randint(-5,5),
                        randint(10,20))
        circles.append(circle)

def on_draw(delta_time):
    arcade.start_render()
 
    for c in circles:
        c.move()
        c.draw()

def main():
    initialize()
 
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)
 
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()

if __name__ == '__main__':
    main()

