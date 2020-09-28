
import struct
class BinConvetor:
    def __init__(self):
        return
    def from_binary_to_dec(self, number):
        decimal = 0
        for digit in str(number):
            decimal = decimal * 2 + int(digit)
        return decimal
    def from_dec_to_binary(self, number):
        binary_turples = [(number, 'pass')]
        while number>0:
            _ = divmod(number, 2)
            binary_turples.append(_)
            number = int(number/2)
        return binary_turples



