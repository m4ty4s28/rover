
from src.enumerates import Points, Movs

class Rover():
    def __init__(self, x, y, direction, rocks=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.rocks = rocks

    def move(self, movimientos: list):
        for mov in movimientos:
            if mov == Movs.FORWARD:
                self.next_position(Movs.FORWARD)
            elif mov == Movs.BACK:
                self.next_position(Movs.BACK)
            elif mov == Movs.LEFT:
                self.left()
            elif mov == Movs.RIGTH:
                self.rigth()

    def check_position(self):
        if self.rocks != None:
            if [self.x, self.y] in self.rocks:
                return True
        return False

    def next_position(self, next_mov):
        rock = False
        if next_mov == Movs.FORWARD and self.forward() and self.check_position():
            self.back()
            rock = True
        elif next_mov == Movs.BACK and self.back() and self.check_position():
            self.forward()
            rock = True
        if rock:
            raise Exception('Rock')

    def forward(self):
        if self.direction == Points.NORTH:
            self.y += 1
        elif self.direction == Points.SOUTH:
            self.y -= 1
        elif self.direction == Points.EAST:
            self.x += 1
        elif self.direction == Points.WEST:
            self.x -= 1
        return True

    def back(self):
        if self.direction == Points.NORTH:
            self.y -= 1
        elif self.direction == Points.SOUTH:
            self.y += 1
        elif self.direction == Points.EAST:
            self.x -= 1
        elif self.direction == Points.WEST:
            self.x += 1
        return True

    def left(self):
        if self.direction == Points.NORTH:
            self.direction = Points.WEST
        elif self.direction == Points.SOUTH:
            self.direction = Points.EAST
        elif self.direction == Points.EAST:
            self.direction = Points.NORTH
        elif self.direction == Points.WEST:
            self.direction = Points.SOUTH

    def rigth(self):
        if self.direction == Points.NORTH:
            self.direction = Points.EAST
        elif self.direction == Points.SOUTH:
            self.direction = Points.WEST
        elif self.direction == Points.EAST:
            self.direction = Points.SOUTH
        elif self.direction == Points.WEST:
            self.direction = Points.NORTH
