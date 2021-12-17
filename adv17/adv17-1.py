from aocd import get_data
import numpy as np

input = get_data(year=2021,day=17).split("\n")
target_xs = list(map(int, input[0].split(" ")[2:][0].split("=")[1].strip(",").split("..")))
target_ys = list(map(int, input[0].split(" ")[2:][1].split("=")[1].strip(",").split("..")))

def step(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]
    velocity[0] -= np.sign(velocity[0])
    velocity[1] -= 1

def in_target_area(position, target_xs, target_ys):
    x = position[0]
    y = position[1]
    tx1 = target_xs[0]
    tx2 = target_xs[1]
    ty1 = target_ys[0]
    ty2 = target_ys[1]

    return (x >= tx1 and x <= tx2) and (y >= ty1 and y <= ty2)

def simulate(init_pos, init_vel, target_xs, target_ys):
    max_y = init_pos[1]

    while(True):
        step(init_pos, init_vel)

        if(init_pos[1] >= max_y):
            max_y = init_pos[1]

        if(in_target_area(init_pos, target_xs, target_ys)):
            return [init_pos, init_vel, True, max_y]

        elif(init_pos[0] > target_xs[1] or init_pos[1] < target_ys[0]):
            return [init_pos, init_vel, False, max_y]

best_vel = []
y_test = abs(target_ys[0])
max_y = None
done = False

while (not done):

    for x in range(-100, 100):
        init_pos = [0,0]
        init_vel = [x,y_test]
        result = simulate(init_pos, init_vel, target_xs, target_ys)

        if(result[2]):
            max_y = result[3]
            best_vel = [x, y_test]
            done = True
            break

    if(not done):
        y_test -= 1

print(max_y)
