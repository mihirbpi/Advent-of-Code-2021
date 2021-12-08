from aocd import get_data
from collections import defaultdict

input = get_data(year=2021,day=8).split("\n")

def deduce(signal_to_digit, digit_to_signal, signals):

    for signal in [x for x in signals if len(x) == 6]:

        for letter in digit_to_signal["8"]:

            if(letter not in signal and letter in digit_to_signal["4"] and letter not in digit_to_signal["1"]):
                signal_to_digit[tuple(sorted(list(signal)))] = "0"
                digit_to_signal["0"] = tuple(sorted(list(signal)))

            elif(letter not in signal and letter in digit_to_signal["4"] and letter in digit_to_signal["1"]):
                signal_to_digit[tuple(sorted(list(signal)))] = "6"
                digit_to_signal["6"] = tuple(sorted(list(signal)))

            elif(letter not in signal and letter not in digit_to_signal["4"]):
                signal_to_digit[tuple(sorted(list(signal)))] = "9"
                digit_to_signal["9"] = tuple(sorted(list(signal)))

    for signal in [x for x in signals if len(x) == 5]:

        if(len(set(digit_to_signal["6"]) - set(signal)) == 1):
            signal_to_digit[tuple(sorted(list(signal)))] = "5"
            digit_to_signal["5"] = tuple(sorted(list(signal)))

        elif(len(set(digit_to_signal["9"]) - set(signal)) == 1):
            signal_to_digit[tuple(sorted(list(signal)))] = "3"
            digit_to_signal["3"] = tuple(sorted(list(signal)))

        else:
            signal_to_digit[tuple(sorted(list(signal)))] = "2"
            digit_to_signal["2"] = tuple(sorted(list(signal)))

total = 0
len_dict = defaultdict(lambda: "0")
len_dict.update({2: "1", 3: "7", 4: "4", 7: "8"})

for line in input:
    signal_to_digit, digit_to_signal = 2*[defaultdict(lambda: "-1")]
    signals, digits = [x.split(" ") for x in line.split(" | ")]

    for signal in signals:
        signal_to_digit[tuple(sorted(list(signal)))] = len_dict[len(signal)]
        digit_to_signal[len_dict[len(signal)]] = tuple(sorted(list(signal)))

    deduce(signal_to_digit, digit_to_signal, signals)
    total += int("".join([signal_to_digit[tuple(sorted(list(digit)))] for digit in digits]))

print(total)
