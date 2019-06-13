from graphics import *
from WallFollowerMR import WallFollowerMR
from RandomMR import RandomMR
from EvolvableMR import EvolvableMR
from Population import Population


# TO Do: label groups of MRs that get drawn to the screen with the number of MR
# at that position, generations with really low average fitnesses tend to be really spread out

# This can also save time by not undrawing and re-drawing MRs to the same location,
# we can keep a record of which spots have MRs draw on them and then only draw one
# MR to each space and not have to undraw all the MRs on the same space

# Make a maze here where you put W for the walls and O for the path, and E at
# the end of the maze

import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from time import sleep
import random

# Define size and amount of obstacles
mazeSize = 40
obstaclePercentage = 0.2

maze = [[] for i in range(mazeSize)]
i = 0
j = 0

for i in range(mazeSize):
    for j in range(mazeSize):
        maze[i].append(0)
        j += 1
    i += 1

obstacleAmount = int(mazeSize**2 * obstaclePercentage)

def getRandom():
    return random.randint(0,mazeSize-1)

def createMaze():
    for i in range(obstacleAmount):
        setObstacle(getRandom(),getRandom())

def setObstacle(x, y):
    if maze[x][y] == 0:
        maze[x][y] = 1
        return "true"
    else:
        setObstacle(getRandom(), getRandom())

createMaze()

# save maze to file for a* and djikstra comparison
np.savetxt('maze.txt', maze, fmt='%s')

# add boundaries to maze to avoid breaking algorithm
mazeBoundaries = [[] for i in range(mazeSize+2)]
for i in range(mazeSize+2):
    for j in range(mazeSize+2):
        if(i == 0):
            mazeBoundaries[i].append(1)
        elif(j == 0):
            mazeBoundaries[i].append(1)
        elif(i == mazeSize+1):
            mazeBoundaries[i].append(1)
        elif(j == mazeSize+1):
            mazeBoundaries[i].append(1)
        else:
            mazeBoundaries[i].append(maze[i-1][j-1])
        j += 1
    i += 1


mazeBoundaries[mazeSize][mazeSize] = 2

# make window and draw the maze
win = GraphWin("Genetic Algorithm", 840, 840)

for j in range(len(mazeBoundaries)):
    for i in range(len(mazeBoundaries[j])):
        if (mazeBoundaries[j][i] == 1):
            mazeBoundaries[j][i] = 'W'

for j in range(len(mazeBoundaries)):
    for i in range(len(mazeBoundaries[j])):
        if (mazeBoundaries[j][i] == 0):
            mazeBoundaries[j][i] = 'O'

for j in range(len(mazeBoundaries)):
    for i in range(len(mazeBoundaries[j])):
        if (mazeBoundaries[j][i] == 2):
            mazeBoundaries[j][i] = 'E'

for j in range(len(mazeBoundaries)):
    for i in range(len(mazeBoundaries[j])):
        r = Rectangle(Point(20*i,20*j), Point(20*i + 20,20*j + 20))
        if (mazeBoundaries[j][i] == "W"):
            r.setFill("black")
        if (mazeBoundaries[j][i] == "E"):
            r.setFill("red")
        r.draw(win)

# make a new population
# Population(windo'W', maze, starting X pos, starting Y pos, starting direction, end X pos, end Y pos, mazeSize)
population = Population(win, mazeBoundaries, 1, 1, 0, mazeSize, mazeSize+1, mazeSize+1)

# run the simulation for 100 generations
population.advance(100)
