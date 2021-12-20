from aocd import get_data

input = get_data(year=2021,day=19).split("\n\n")
#input = open("input.txt").read().split("\n\n")

def distance_vector(l1, l2):
    return [ abs(l1[0] - l2[0]), abs(l1[1] - l2[1]), abs(l1[2] - l2[2])]


def diff_vector(l1, l2):
    return [l1[0] - l2[0], l1[1] - l2[1], l1[2] - l2[2]]

def add_vector(l1, l2):
    return [l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2]]

def get_list_rotations(l):
    rotated_lists = []

    for i in range(0, 24):
        rotated_lists.append([])

    for p in l:
        x, y, z = p

        trs = [[x, y, z], [x, z, -y], [-z, x, -y], [-x, -z, -y],
            [z, -x, -y], [z, -y, x], [y, z, x],
            [-z, y, x], [-y, -z, x], [-y, x, z],
            [-x, -y, z], [y, -x, z],
            [-z, -x, y], [x, -z, y], [z, x, y],
            [-x, z, y], [-x, y, -z], [-y, -x, -z],
            [x, -y, -z], [y, x, -z], [y, -z, -x],
            [z, y, -x], [-y, z, -x], [-z, -y, -x]]

        for i in range(0, 24):
            rotated_lists[i].append(trs[i])

    return rotated_lists


def get_pt_rotations(pt):
    rotated_pts = []

    x, y, z = pt

    trs = [[x, y, z], [x, z, -y], [-z, x, -y], [-x, -z, -y],
            [z, -x, -y], [z, -y, x], [y, z, x],
            [-z, y, x], [-y, -z, x], [-y, x, z],
            [-x, -y, z], [y, -x, z],
            [-z, -x, y], [x, -z, y], [z, x, y],
            [-x, z, y], [-x, y, -z], [-y, -x, -z],
            [x, -y, -z], [y, x, -z], [y, -z, -x],
            [z, y, -x], [-y, z, -x], [-z, -y, -x]]

    return trs

def get_beacon_distances_lists(l):
    beacon_distances_lists = []

    for i in range(0, len(l)):
        current_beacon = l[i]
        beacon_distances_list = []

        for j in range(0, len(l)):
            other_beacon = l[j]
            beacon_distances_list.append(diff_vector(current_beacon, other_beacon))

        beacon_distances_lists.append([l[i], beacon_distances_list])

    return beacon_distances_lists

class Scanner:

    def __init__(self, number, pt_list):
        self.number = number
        self.pt_list = pt_list
        self.relative0_vector = None

    def get_rotations(self):
        return get_list_rotations(self.pt_list)

    def get_beacon_distances(self):
        return [get_beacon_distances_lists(x) for x in self.get_rotations()]

scanners = []

for i in range(0, len(input)):

    if(i == len(input) - 1):
        number = int(input[i].split("\n")[0].split(" ")[2])
        pt_string_list = input[i].split("\n")[1:]
        pt_list = [list(map(int, x.split(","))) for x in pt_string_list]
        scanners.append(Scanner(number, pt_list))

    else:
        number = int(input[i].split("\n")[0].split(" ")[2])
        pt_string_list = input[i].split("\n")[1:]
        pt_list = [list(map(int, x.split(","))) for x in pt_string_list]
        scanners.append(Scanner(number, pt_list))

beacon_distances_zero =  scanners[0].get_beacon_distances()


found_list = [0]

while(len(found_list) < len(scanners)):
    print("length:", len(scanners) - len(found_list))
    #print(len(scanners[0].pt_list))
    for i in range(0, len(scanners)):

        if(i not in found_list):
            print("i: ", i)
            #print(i / (len(scanners) - len(found_list)))
            scanner = scanners[i]
            #print(scanner.number)
            #print(scanner.pt_list)
            #print("a\n\n")
            #beacon_distances_zero =  scanners[0].get_beacon_distances()
            beacon_distances_current = scanner.get_beacon_distances()
            diff = None
            rot_index = None

            for j in range(0, len(beacon_distances_current)):

                rotation = beacon_distances_current[j]
                for o in range(0, len(rotation)):
                    elem = rotation[o]
                    distance_list_to_check = elem[1]
                    #if(distance_list_to_check matches some distance list in 0):
                    #for k in range(0, 1):
                    other_rotation = beacon_distances_zero[0]

                    for other_elem in other_rotation:
                        other_distance_list_to_check = other_elem[1]
                        count = 0

                        for m in range(0, len(other_distance_list_to_check)):

                            for n in range(0, len(distance_list_to_check)):

                                if(other_distance_list_to_check[m] == distance_list_to_check[n]):
                                    count += 1
                            #if(i == 4):
                            #    print("b", i, count)
                        if(count >= 12 and other_elem[0] in scanners[0].pt_list):
                                #print(j, other_elem[0], elem[0])
                                #print(diff_vector(other_elem[0], elem[0]))
                            if(diff == None and rot_index == None):
                                diff = diff_vector(other_elem[0], elem[0])
                                rot_index = j

                                #print("\n\n")
                                #break
            if(rot_index != None and diff != None):
                found_list.append(i)
                for pt in scanner.pt_list:
                    pt_rotation = get_pt_rotations(pt)[rot_index]

                    #print(pt_rotation, diff,  diff_vector(pt_rotation, diff))
                    diff_vec = add_vector(pt_rotation, diff)
                    if diff_vec not in scanners[0].pt_list:
                        scanners[0].pt_list.append(diff_vec)

                beacon_distances_zero =  scanners[0].get_beacon_distances()
                        #print(diff_vec)
            #print(pt_rotation, diff,  diff_vec)

count = 0
for x in list(sorted(scanners[0].pt_list)):
    #print(x)
    count += 1
print(count)
