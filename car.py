import math


class car:
    def __init__(self, x, y, v, angle):
        self.x = x
        self.y = y
        self.v = v
        self.angle = angle

    def move(self, step):
        self.x += self.v * math.cos(self.angle)*step
        self.y -= self.v * math.sin(self.angle)*step

    def turnleft(self, phi=math.pi/72.0):
        self.angle += phi
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

    def turnright(self, phi=math.pi/72.0):
        self.angle -= phi
        if self.angle < 0:
            self.angle += 2 * math.pi

    def respawn(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle