from copy import deepcopy

HALLWAY = list("...........")
A_room = ["A", "B"]
B_room = ["D", "C"]
C_room = ["B", "D"]
D_room = ["C", "A"]
MOVE_COSTS = {"A": 1,"B": 10, "C": 100, "D": 1000}
INIT_STATE = ({"A": A_room,"B": B_room, "C": C_room, "D": D_room}, HALLWAY)
DP = {}


def pretty_print(state):

    rooms = state[0]
    hallway = state[1]
    print("#############")
    hallway_str = "#"
    for i in range(0, len(hallway)):
        hallway_str += hallway[i]
    hallway_str += "#"
    print(hallway_str)
    first_depth = "###"
    for key in rooms:
        first_depth += rooms[key][0] + "#"
    first_depth += "##"
    print(first_depth)
    second_depth = " ##"
    for key in rooms:
        second_depth += rooms[key][1] + "#"
    second_depth += "# "
    print(second_depth)
    print(" ########### \n")



def contains_only(occupant, rooms):
    for e in rooms[occupant]:
        if(e != occupant and e != "."):
            return False
    return True

def should_move_0(room, rooms):
    for i in range(0, 2):
        if(rooms[room][i] != room and rooms[room][i] != "."):
            return True
    return False

def can_move_into_room(hallway, room, occupant, hall_index):
    room_col = 2*(ord(occupant)-64)

    for e in room:
        if(e != occupant and e != "."):
            return None

    if(room_col < hall_index):
        for index in range(hall_index - 1, room_col - 1, -1):
            if(hallway[index] != "."):
                return None

    elif(room_col > hall_index):
        for index in range(hall_index + 1, room_col + 1, 1):
            if(hallway[index] != "."):
                return None

    if(room[0] == "." and room[1] == occupant):

        distance = abs(hall_index - room_col) + 1
        return distance, 0

    elif(room[0] == "." and room[1] == "."):
        distance = abs(hall_index - room_col) + 2
        return distance, 1

    else:
        return None

def is_done(state):

    rooms = state[0]
    hallway = state[1]

    for key in rooms:

        for element in rooms[key]:

            if(element != key or element == "."):
                return False

    for element in hallway:
        if(element != "."):
            return False
    return True


def get_cost(state):
    rooms = state[0]
    hallway = state[1]
    key = (tuple((k, tuple(v)) for k,v in rooms.items()), tuple(hallway))

    if(is_done(state)):
        DP[key] = 0
        return 0

    if(key in DP):
       return DP[key]

    else:
        for i in range(0, len(hallway)):

            if(hallway[i] != "."):
                occupant = hallway[i]
                occupant_col =  2*(ord(occupant)-64)
                result = can_move_into_room(hallway, rooms[occupant], occupant, i)

                if(result != None):
                    distance, depth = result
                    new_hallway = list(hallway)
                    updated_room = list(rooms[occupant])
                    new_rooms = deepcopy(rooms)
                    updated_room[depth] = occupant
                    new_hallway[i] = "."
                    new_rooms[occupant] = updated_room
                    answer = (MOVE_COSTS[occupant] * result[0]) + get_cost((new_rooms, new_hallway))
                    DP[key] = answer
                    return answer

        min_cost = int(1e9)
        for room in rooms:

            if(rooms[room][0] != "." and should_move_0(room, rooms) ):
                occupant = rooms[room][0]
                room_col = 2*(ord(room)-64)
                occupant_col = 2*(ord(occupant)-64)

                places_can_move_to = []

                for index in range(room_col, len(hallway)):

                    if(hallway[index] != "."):
                        break

                    elif(index == occupant_col):
                        if(rooms[occupant][0] == "." and rooms[occupant][1] == occupant):
                            distance = 2 + abs(index - room_col)
                            places_can_move_to.append([-1, distance])

                        elif(rooms[occupant][0] == "." and rooms[occupant][1] == "."):
                            distance = 3 + abs(index - room_col)
                            places_can_move_to.append([-2, distance])

                if(len(places_can_move_to) >= 0):

                    for index in range(room_col, -1, -1):

                        if(hallway[index] != "."):
                            break

                        elif(index == occupant_col):
                            if(rooms[occupant][0] == "." and rooms[occupant][1] == occupant):
                                distance = 2 + abs(index - room_col)
                                places_can_move_to.append([-1, distance])

                            elif(rooms[occupant][0] == "." and rooms[occupant][1] == "."):
                                distance = 3 + abs(index - room_col)
                                places_can_move_to.append([-2, distance])

                places_can_move_to.sort()

                for p in places_can_move_to:

                    depth = -1*p[0] - 1
                    new_rooms = deepcopy(rooms)
                    new_hallway = list(hallway)
                    new_rooms[occupant][depth] = occupant
                    new_rooms[room][0] = "."
                    min_cost = min(min_cost, (MOVE_COSTS[occupant] * p[1]) + get_cost((new_rooms, new_hallway)))
                    DP[key] = min_cost
                    return min_cost

            elif(rooms[room][0] == "." and rooms[room][1] != "."  and should_move_0(room, rooms)):
                occupant = rooms[room][0]
                room_col = 2*(ord(room)-64)
                occupant_col = 2*(ord(occupant)-64)

                places_can_move_to = []

                for index in range(room_col, len(hallway)):

                    if(hallway[index] != "."):
                        break

                    elif(index == occupant_col):
                        if(rooms[occupant][0] == "." and rooms[occupant][1] == occupant):
                            distance = 2 + abs(index - room_col)
                            places_can_move_to.append([-1, distance])

                        elif(rooms[occupant][0] == "." and rooms[occupant][1] == "."):
                            distance = 3 + abs(index - room_col)
                            places_can_move_to.append([-2, distance])

                if(len(places_can_move_to) == 0):

                    for index in range(room_col, -1, -1):

                        if(hallway[index] != "."):
                            break

                        elif(index == occupant_col):

                            if(rooms[occupant][0] == "." and rooms[occupant][1] == occupant):
                                distance = 2 + abs(index - room_col)
                                places_can_move_to.append([-1, distance])


                            elif(rooms[occupant][0] == "." and rooms[occupant][1] == "."):
                                distance = 3 + abs(index - room_col)
                                places_can_move_to.append([-2, distance])


                places_can_move_to.sort()

                for p in places_can_move_to:

                    depth = -1*p[0] - 1
                    new_rooms = deepcopy(rooms)
                    new_hallway = list(hallway)
                    new_rooms[occupant][depth] = occupant
                    new_rooms[room][1] = "."
                    min_cost = min(min_cost, (MOVE_COSTS[occupant] * p[1]) + get_cost((new_rooms, new_hallway)))
                    DP[key] = min_cost
                    return min_cost

        min_cost = int(1e9)

        for room in rooms:

            if(rooms[room][0] != "." and should_move_0(room, rooms) ):
                occupant = rooms[room][0]
                room_col = 2*(ord(room)-64)
                occupant_col = 2*(ord(occupant)-64)

                places_can_move_to = []

                for index in range(room_col, len(hallway)):

                    if(hallway[index] != "."):
                        break

                    else:
                        distance = 1 + abs(index - room_col)
                        if(index not in [2,4,6,8]):
                            places_can_move_to.append([distance, index])

                for index in range(room_col, -1, -1):

                    if(hallway[index] != "."):
                        break

                    else:
                        distance = 1 + abs(index - room_col)
                        if(index not in [2,4,6,8]):
                            places_can_move_to.append([distance, index])

                places_can_move_to.sort()

                for p in places_can_move_to:

                    new_rooms = deepcopy(rooms)
                    new_hallway = list(hallway)
                    new_hallway[p[1]] = occupant
                    new_rooms[room][0] = "."
                    min_cost = min(min_cost, (MOVE_COSTS[occupant] * p[0]) + get_cost((new_rooms, new_hallway)))


            elif(rooms[room][0] == "." and rooms[room][1] != "."  and should_move_0(room, rooms)):
                occupant = rooms[room][1]
                occupant_col = 2*(ord(occupant)-64)
                room_col = 2*(ord(room)-64)
                places_can_move_to = []

                for index in range(room_col, len(hallway)):

                    if(hallway[index] != "."):
                        break

                    else:
                        distance = 2 + abs(index - room_col)
                        if(index not in [2,4,6,8]):
                            places_can_move_to.append([distance, index])

                for index in range(room_col, -1, -1):

                    if(hallway[index] != "."):
                        break

                    else:
                        distance = 2 + abs(index - room_col)
                        if(index not in [2,4,6,8]):
                            places_can_move_to.append([distance, index])

                places_can_move_to.sort()

                for p in places_can_move_to:
                    new_rooms = deepcopy(rooms)
                    new_hallway  = list(hallway)
                    new_hallway[p[1]] = occupant
                    new_rooms[room][1] = "."
                    min_cost = min(min_cost, (MOVE_COSTS[occupant] * p[0]) + get_cost((new_rooms, new_hallway)))

        DP[key] = min_cost
        return min_cost

print(get_cost(INIT_STATE))
