from aocd import get_data
from collections import defaultdict
import heapdict

input = get_data(year=2021,day=15).split("\n")

#Dijkstra's algorithm
def get_risk(x, y, input):
    a = int(input[y % len(input)][x % len(input[0])]) + (x// len(input[0])) + (y // len(input))
    return (a - 1) % 9 + 1

dist = {}
prev = {}
source = (0,0)
dist[source] = 0
target = (5 * len(input[0]) - 1, 5 * len(input) - 1)
Q = heapdict.heapdict()

for y in range(0, 5*len(input)):

    for x in range(0, 5*len(input[0])):
        v = (x,y)
        if(v != source):
            dist[v] = 1000000
        Q[v] = dist[v]

while (len(Q) > 0):
    popped = Q.popitem()
    u = popped[0]

    if(u == target):
        break

    u_x = u[0]
    u_y = u[1]
    neighbors = []

    n1 = (u_x + 1, u_y)
    n2 = (u_x, u_y + 1)
    n3 = (u_x - 1, u_y)
    n4 = (u_x, u_y - 1)

    if(u_x+1 < 5*len(input[0])):
        neighbors.append(n1)

    if(u_y+1 < 5*len(input)):
        neighbors.append(n2)

    if(u_x - 1 >= 0):
        neighbors.append(n3)

    if(u_y - 1 >= 0):
        neighbors.append(n4)

    for v in neighbors:

        if(v in Q):
            alt = dist[u] + get_risk(v[0], v[1], input)

            if (alt < dist[v]):
                dist[v] = alt
                prev[v] = u
                Q[v] = alt

S = []
u = target

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
    path_length += get_risk(next[0], next[1], input)

print(path_length)
