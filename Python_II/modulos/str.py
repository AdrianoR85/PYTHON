def inverse(string, space=False):
    if space: string = "".join(string.split())
    return string[::-1]


def even_char(string, space=False):
    if space: string = "".join(string.split())
    return string[::2]


def odd_char(string, space=False):
    if space: string = "".join(string.split())
    return string[1::2]
