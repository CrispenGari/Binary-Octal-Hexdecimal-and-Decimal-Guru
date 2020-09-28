

class OctCoversion:
    def __init__(self):
        return
    def oct_to_decimal(self, number):
        return
    def dec_to_oct(self, number):
        octal_turples = [(number, 'pass')]
        while number > 0:
            _ = divmod(number, 8)
            octal_turples.append(_)
            number = int(number / 8)
        return octal_turples