import arcade
import math
from random import randint
from pyglet.window import key


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
                or self.x < self.r:
            self.vx *= -1
        if self.y > SCREEN_HEIGHT - self.r \
                or self.y < self.r:
            self.vy *= -1

    def stop(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   self.r, arcade.color.WHITE)

    def draw(self):
        arcade.draw_circle_outline(self.x, self.y,
                                   self.r, arcade.color.BLACK)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y,
                                  10, arcade.color.BLUE)

    def control(self, keys):
        if keys[key.LEFT]:
            self.x -= 5
        if keys[key.RIGHT]:
            self.x += 5
        if keys[key.UP]:
            self.y += 5
        if keys[key.DOWN]:
            self.y -= 5

    def restart(self):
        self.x = 0
        self.y = 0

    def is_hit(self, circle):
        a = self.x - circle.x
        b = self.y - circle.y
        c = math.sqrt(((a**2)+(b**2)))
        if c < 10+circle.r:
            return True
        return False


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

circles = []
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
n = 10

keys = key.KeyStateHandler()


def initialize():
    for i in range(n):
        circle = Circle(randint(100, SCREEN_WIDTH-100),
                        randint(100, SCREEN_HEIGHT-100),
                        randint(-5, 5),
                        randint(-5, 5),
                        randint(10, 20))
        circles.append(circle)


def on_draw(delta_time):
    arcade.start_render()

    for c in circles:
        c.move()
        c.draw()
        if player.is_hit(c):
            player.restart()

    player.control(keys)
    player.draw()


def main():
    initialize()

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                       "Circles")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.get_window().push_handlers(keys)

    arcade.schedule(on_draw, 1 / 80)
    arcade.run()


if __name__ == '__main__':
    main()
