import pytest
from src.rover import Rover
from src.enumerates import Points

def test_mov_x():
    rover = Rover(0,0,Points.EAST)
    rover.forward()
    assert rover.x == 1

    rover = Rover(0,0,Points.WEST)
    rover.forward()
    assert rover.x == -1

    rover = Rover(1,1,Points.WEST)
    rover.forward()
    assert rover.x == 0

def test_mov_y():
    rover = Rover(0,0,Points.NORTH)
    rover.forward()
    assert rover.y == 1

def test_mov_r():
    rover = Rover(0,0,Points.NORTH)
    rover.left()
    assert rover.direction == Points.WEST

def test_mov_l():    
    rover = Rover(0,0,Points.NORTH)
    rover.rigth()
    assert rover.direction == Points.EAST

def test_mov():    
    rover = Rover(0,0,Points.NORTH)
    cadena = ["f","f","f","l","f"]
    rover.move(cadena)
    assert rover.x == -1
    assert rover.y == 3
    assert rover.direction == Points.WEST

def mov_rock_f():
    rover = Rover(0,0,Points.NORTH, [[0,2],])
    cadena = ["f","f",]
    rover.move(cadena)

def mov_rock_f2():
    rover = Rover(0,0,Points.WEST, [[-3,2],])
    cadena = ["f","f","f","r","f","f"]
    rover.move(cadena)

def mov_rock_b():
    rover = Rover(0,0,Points.NORTH, [[0,-3],])
    cadena = ["b","b","b"]
    rover.move(cadena)

def mov_rock_b2():
    rover = Rover(0,0,Points.EAST, [[-2,2],])
    cadena = ["b","b","l","f","f"]
    rover.move(cadena)

def test_mov_rock_f():
    with pytest.raises(Exception) as excinfo:   
        mov_rock_f()
    assert str(excinfo.value) == 'Rock'

def test_mov_rock_f2():
    with pytest.raises(Exception) as excinfo:   
        mov_rock_f2()
    assert str(excinfo.value) == 'Rock'

def test_mov_rock_b():
    with pytest.raises(Exception) as excinfo:   
        mov_rock_b()
    assert str(excinfo.value) == 'Rock'

def test_mov_rock_b2():
    with pytest.raises(Exception) as excinfo:   
        mov_rock_b2()
    assert str(excinfo.value) == 'Rock'