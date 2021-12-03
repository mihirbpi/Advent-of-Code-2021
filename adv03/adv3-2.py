from aocd import get_data

list = get_data(day=3).split("\n")

def get_ox_rating_str(l, i):

    if(len(l) == 1):
        return l[0]

    ith_pos_bits = [x[i] for x in l]
    most = max(ith_pos_bits,key=lambda x: ith_pos_bits.count(x))
    least = min(ith_pos_bits ,key=lambda x: ith_pos_bits.count(x))

    if(most == least):
        most = "1"

    new_l = [x for x in l if (x[i] == most)]
    return get_ox_rating_str(new_l, i+1)

def get_co2_rating_str(l, i):

    if(len(l) == 1):
        return l[0]
    ith_pos_bits = [x[i] for x in l]
    most = max(ith_pos_bits,key=lambda x: ith_pos_bits.count(x))
    least = min(ith_pos_bits ,key=lambda x: ith_pos_bits.count(x))

    if(most == least):
        least = "0"

    new_l = [x for x in l if (x[i] == least)]
    return get_co2_rating_str(new_l, i+1)


ox_rating = int(get_ox_rating_str(list, 0), base=2)
co2_rating = int(get_co2_rating_str(list, 0), base=2)
print(ox_rating * co2_rating)
