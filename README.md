# Problema

You’re part of the team that explores Mars by sending remotely controlled vehicles to the surface of the planet.

Develop a Class that translates the commands sent from earth to instructions that are understood by the rover.

## Requirements

- You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
- The rover receives a character array of commands.
- Implement commands that move the rover forward/backward (f,b).
- Implement commands that turn the rover left/right (l,r).
- Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.

# Solución

This repository provides you with a convenient setup to tackle coding katas. You can choose to run it with Docker or without it, depending on your preference.

## Getting Started

### Using Docker 🐳

1. Build the Docker image:
   ```
   docker compose build
   ```

2. Run the tests:
   ```
   docker compose run kata pytest
   ```

### Without Docker 🚀

1. Install dependencies locally:
   ```
   pip install -r requirements.txt  
   ```

2. Run the tests:
   ```
   pytest
   ```

The solution is in the file [rover.py](https://github.com/m4ty4s28/rover/blob/main/src/rover.py) and the Tests in the file [test_mov.py](https://github.com/m4ty4s28/rover/blob/main/src/test/test_mov.py)
____________
