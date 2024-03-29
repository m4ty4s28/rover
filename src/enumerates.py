from enum import Enum

class Points(str, Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class Movs(str, Enum):
    FORWARD = "f"
    BACK = "b"
    LEFT = "l"
    RIGTH = "r"

class Steps(int, Enum):
    FORWARD = 1
    BACK = -1