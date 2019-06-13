##############################################################################
# import packages
# https://www.analytics-link.com/single-post/2018/09/14/Applying-the-A-Path-Finding-Algorithm-in-Python-Part-1-2D-square-grid
##############################################################################
import numpy as np
import heapq
import os
import matplotlib.pyplot as plt
import time

# load maze which was generated in Main.py
y = np.loadtxt('maze.txt', dtype=np.int)


##############################################################################
# plot grid
##############################################################################


grid = np.array(y)


# start point and goal
start = (0,0)
goal = (39, 39)


##############################################################################
# heuristic function for path scoring
##############################################################################
def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

##############################################################################
# path finding function
##############################################################################
start_time = time.time()
def astar(array, start, goal):

    # removed ,(1,1),(1,-1),(-1,1),(-1,-1) that it will not cross the edges
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

route = astar(grid, start, goal)
route = route + [start]
route = route[::-1]
runtime = (time.time() - start_time)
print("--- %s seconds ---" % runtime)
print(route)
astaroutput = open("astarresult.txt","a")
astaroutput.write(str(runtime) + ",\n")
astaroutput.close
os.system("dijkstra.py")

#extract x and y coordinates from route list
x_coords = []
y_coords = []

for i in (range(0,len(route))):
    x = route[i][0]
    y = route[i][1]
    x_coords.append(x)
    y_coords.append(y)

# plot map and path
fig, ax = plt.subplots(figsize=(20,20))
ax.imshow(grid, cmap=plt.cm.Set2)
ax.scatter(start[1],start[0], marker = "o", color = "yellow", s = 200)
ax.scatter(goal[1],goal[0], marker = "o", color = "red", s = 200)
ax.plot(y_coords,x_coords, color = "black")
plt.title('A* Result')
plt.show()