from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=8).split("\n")

def my_sort(l):
    L = l
    L.sort()
    return L

def deduce(signal_to_digit, digit_to_signal, signals):

    for signal in [x for x in signals if len(x) == 6]:

        for letter in digit_to_signal["8"]:

            if(letter not in signal):

                if(letter in digit_to_signal["4"] and letter not in digit_to_signal["1"]):
                    signal_to_digit[tuple(my_sort(list(signal)))] = "0"
                    digit_to_signal["0"] = tuple(my_sort(list(signal)))

                elif(letter in digit_to_signal["4"] and letter in digit_to_signal["1"]):
                    signal_to_digit[tuple(my_sort(list(signal)))] = "6"
                    digit_to_signal["6"] = tuple(my_sort(list(signal)))

                elif(letter not in digit_to_signal["4"]):
                    signal_to_digit[tuple(my_sort(list(signal)))] = "9"
                    digit_to_signal["9"] = tuple(my_sort(list(signal)))

    for signal in [x for x in signals if len(x) == 5]:

        if(len(set(digit_to_signal["6"]) - set(signal)) == 1):
            signal_to_digit[tuple(my_sort(list(signal)))] = "5"
            digit_to_signal["5"] = tuple(my_sort(list(signal)))

        elif(len(set(digit_to_signal["9"]) - set(signal)) == 1):
            signal_to_digit[tuple(my_sort(list(signal)))] = "3"
            digit_to_signal["3"] = tuple(my_sort(list(signal)))

        else:
            signal_to_digit[tuple(my_sort(list(signal)))] = "2"
            digit_to_signal["2"] = tuple(my_sort(list(signal)))

total = 0

for line in input:
    signal_to_digit = defaultdict(lambda: "-1")
    digit_to_signal = defaultdict(lambda: "-1")
    signals = line.strip("\n").split(" | ")[0].split(" ")
    digits = line.strip("\n").split(" | ")[1].split(" ")

    for signal in signals:

        if(len(signal) == 2):
            signal_to_digit[tuple(my_sort(list(signal)))] = "1"
            digit_to_signal["1"] = tuple(my_sort(list(signal)))

        elif(len(signal) == 4):
            signal_to_digit[tuple(my_sort(list(signal)))] = "4"
            digit_to_signal["4"] = tuple(my_sort(list(signal)))

        elif(len(signal) == 3):
            signal_to_digit[tuple(my_sort(list(signal)))] = "7"
            digit_to_signal["7"] = tuple(my_sort(list(signal)))

        elif(len(signal) == 7):
            signal_to_digit[tuple(my_sort(list(signal)))] = "8"
            digit_to_signal["8"] = tuple(my_sort(list(signal)))

    deduce(signal_to_digit, digit_to_signal, signals)
    total += int("".join([signal_to_digit[tuple(my_sort(list(digit)))] for digit in digits]))

print(total)
