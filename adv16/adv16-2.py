from aocd import get_data
import numpy as np

input = get_data(year=2021,day=16).split("\n")[0]

HEX_TO_BINARY_CONVERSION_TABLE = {
                              '0': '0000',

                              '1': '0001',

                              '2': '0010',

                              '3': '0011',

                              '4': '0100',

                              '5': '0101',

                              '6': '0110',

                              '7': '0111',

                              '8': '1000',

                              '9': '1001',

                              'A': '1010',

                              'B': '1011',

                              'C': '1100',

                              'D': '1101',

                              'E': '1110',

                              'F': '1111'}

def hex_to_binary(hex_string):
    binary_string = ""
    for character in hex_string:
        binary_string += HEX_TO_BINARY_CONVERSION_TABLE[character]
    return binary_string

class Packet:

    def __init__(self, bin_string):
        self.bits = bin_string
        self.version = int(self.bits[0:3], 2)
        self.typeID =  int(self.bits[3:6], 2)
        self.literal_value = None
        self.length_typeID = None
        self.child_array = []
        self.extra_bits = ""
        self.parse(self.bits[6:])
        self.value = self.get_value()

    def parse(self, bin_string):

        if(self.typeID == 4):
            self.parse_literal(bin_string)
        else:
            self.length_typeID = int(bin_string[0])

            if(self.length_typeID == 0):
                self.parse_lengthbits_operator(bin_string[1:])
            else:
                self.parse_numpackets_operator(bin_string[1:])


    def parse_literal(self, bin_string):
        literal_string = ""
        index = 0
        prefix = "1"

        while (prefix == "1"):
            prefix = bin_string[index]
            literal_string += bin_string[index+1:index+5]
            index += 5

        self.literal_value = int(literal_string, 2)
        self.extra_bits = bin_string[index:]

    def parse_lengthbits_operator(self, bin_string):
        num_bits = int(bin_string[:15], 2)
        child_packets_string = bin_string[15:15+num_bits]

        while(len(child_packets_string) != 0 and "1" in child_packets_string):
            new_child = Packet(child_packets_string)
            self.child_array.append(new_child)
            child_packets_string = new_child.extra_bits

        self.extra_bits = bin_string[15+num_bits:]

    def parse_numpackets_operator(self, bin_string):
        num_packets = int(bin_string[:11], 2)
        child_packets_string = bin_string[11:]

        for i in range(1, num_packets + 1):
            new_child = Packet(child_packets_string)
            self.child_array.append(new_child)
            child_packets_string = new_child.extra_bits

        self.extra_bits = child_packets_string

    def total_version(self):
        total_v = self.version
        total_v += sum([x.total_version() for x in self.child_array])
        return total_v

    def get_value(self):

        if(self.typeID == 0):
            return sum([x.value for x in self.child_array])

        elif(self.typeID == 1):
            return np.prod([x.value for x in self.child_array])

        elif(self.typeID == 2):
            return min([x.value for x in self.child_array])

        elif(self.typeID == 3):
            return max([x.value for x in self.child_array])

        elif(self.typeID == 4):
            return self.literal_value

        elif(self.typeID == 5):
            return int(self.child_array[0].value > self.child_array[1].value)

        elif(self.typeID == 6):
            return int(self.child_array[0].value < self.child_array[1].value)

        elif(self.typeID == 7):
            return int(self.child_array[0].value == self.child_array[1].value)

binary_input = hex_to_binary(input)
p = Packet(binary_input)
print(p.value)
