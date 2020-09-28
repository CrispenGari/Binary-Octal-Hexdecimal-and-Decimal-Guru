

class HexConvertor:
    def __init__(self):
        return
    def hex_to_decimal(self, number):
        return
    def dec_to_hex(self, number):
        hex_turples = [(number, 'pass')]
        while number > 0:
            _ = divmod(number, 16)
            hex_turples.append(_)
            number = int(number / 16)
        return hex_turples