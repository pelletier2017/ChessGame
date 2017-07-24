def decode_inpt(inpt_str):
    """
    Converts given input string to row, col
    params: inpt_str is a chess input, ex: "a1"
    returns: tuple with integers row, col
    precondition: letters are lower case between a-h, numbers are 1-8
    """
    letter, num = list(inpt_str)
    row = int(num) - 1
    col = ord(letter) - ord("a")
    return row, col


def encode_inpt(row, col):
    """
    Converts row, col to chess input, ex "a1"
    params: row, col are integers
    returns 2 char string for chess move with letter, number
    """
    num = str(row + 1)
    letter = chr(col + ord("a"))
    return letter + num