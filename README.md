# Solving Pathfinding Problems with Genetic Algorithms, A* and Dijkstra

## Requirements
* Python 2.7.x
* Numpy
* Matplotlib

## Usage
Edit Main.py (line 26/27) to set the size and amount of obstacle
```
mazeSize = 50
obstaclePercentage = 0.2
```
Edit astar.py and dijkstra.py (line 25) and set to goal (normally maze size -1)
```
goal = (49, 49)
```
* Run Main.py (maze.txt will be created which represents the grid with obstacles. This file will be imported into astar.py and dijkstra.py as grid).
* When "Goal found!" appears the first chromosome reached the goal and can be interrupted with Ctrl+C.
* The used time to find the goal will be written into garesult.txt.
* Run astar.py (after the run, dijkstra.py will be started automatically).
* Results will be saved into astarresults.txt and dijkstrareslts.txt

## Contributing
Special thanks to A. Jones for the implementation of A* [analytics-link.com](https://www.analytics-link.com/single-post/2018/09/14/Applying-the-A-Path-Finding-Algorithm-in-Python-Part-1-2D-square-grid) and to LOEller [github.com/LOEller/Maze](https://github.com/LOEller/Maze) for the Genetic Algorithm.
