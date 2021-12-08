from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=8).split("\n")

def my_sort(l):
    L = l
    L.sort()
    return L

count = 0

for line in input:
    signal_to_digits = defaultdict(lambda: -1)
    signals = line.strip("\n").split(" | ")[0].split(" ")
    digits = line.strip("\n").split(" | ")[1].split(" ")

    for signal in signals:

        if(len(signal) == 2):
            signal_to_digits[tuple(my_sort(list(signal)))] = 1

        elif(len(signal) == 4):
            signal_to_digits[tuple(my_sort(list(signal)))] = 4

        elif(len(signal) == 3):
            signal_to_digits[tuple(my_sort(list(signal)))] = 7

        elif(len(signal) == 7):
            signal_to_digits[tuple(my_sort(list(signal)))] = 8

    for digit in digits:

        if(signal_to_digits[tuple(my_sort(list(digit)))] in [1,4,7,8]):
            count += 1

print(count)
