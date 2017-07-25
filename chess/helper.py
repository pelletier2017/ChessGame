def decode_inpt(inpt_str):
    """
    Converts given chess piece string from form "a1" to integers row, col
    :param inpt_str: string of length 2
    :return: integers row, col
    """
    letter, num = list(inpt_str)
    row = int(num) - 1
    col = ord(letter) - ord("a")
    return row, col


def encode_inpt(row, col):
    """
    Converts integers row, col to chess piece string in form "a1"
    :param row: int
    :param col: int
    :return: string in form "a1"
    """
    num = str(row + 1)
    letter = chr(col + ord("a"))
    return letter + num
