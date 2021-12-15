from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=15).split("\n")

#Dijkstra's algorithm
dist = {}
prev = {}
length = {}
Q = []

for y in range(0, len(input)):

    for x in range(0, len(input[0])):
        v = (x,y)
        dist[v] = 1000
        Q.append(v)
        n1 = (x+1, y)
        n2 = (x, y+1)
        n3 = (x-1, y)
        n4 = (x, y-1)

        if(x+1 < len(input[y])):
            length[(v,n1)] = int(input[y][x+1])

        if(y+1 < len(input)):
            length[(v,n2)] = int(input[y+1][x])

        if(x-1 >= 0):
            length[(v,n3)] = int(input[y][x-1])

        if(y-1 >= 0):
            length[(v,n4)] = int(input[y-1][x])


source = (0,0)
dist[source] = 0

while (len(Q) > 0):
    L = [(x, dist[x]) for x in Q]
    min_val = 1000
    min_element = None

    for y in L:

        if (y[1] < min_val):
            min_val = y[1]
            min_element = y[0]
    u = min_element
    Q.remove(u)
    u_x = u[0]
    u_y = u[1]
    neighbors = []

    n1 = (u_x+1, u_y)
    n2 = (u_x, u_y+1)
    n3 = (u_x - 1, u_y)
    n4 = (u_x, u_y - 1)

    if(u_x+1 < len(input[u_y])):
        neighbors.append(n1)

    if(u_y+1 < len(input)):
        neighbors.append(n2)

    if(u_x - 1 >= 0):
        neighbors.append(n3)

    if(u_y - 1>= 0):
        neighbors.append(n4)

    for v in neighbors:

        if(v in Q):
            alt = dist[u] + length[(u,v)]

            if (alt < dist[v]):
                dist[v] = alt
                prev[v] = u

S = []
u = (len(input[0]) - 1, len(input) - 1)

if (u in prev or u == source):

    while (u in prev):
        S.append(u)
        u = prev[u]

S.append(source)
path = list(reversed(S))
path_length = 0

for i in range(0, len(path) - 1):
    curr = path[i]
    next = path[i+1]
    path_length += length[(curr, next)]

print(path_length)
