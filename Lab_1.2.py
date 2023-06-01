import ast

def counter(_str: str) -> None:
    """
    param _str: coded text
    :return: None
    """
    a = set(list(_str))
    b = []

    for i in a:
        b.append([_str.count(i) / len(_str), i])
        #print(i, str.count(i) / len(str))
    #print(a)
    #print(len(str))
    #print(len(a))
    #b.sort()
    #print(b)


def decoder(_str: str) -> str:
    with open("key-1.txt", "r", encoding="utf-8") as ff:
        key1 = ff.read()
    key1 = ast.literal_eval(key1)
    _str = _str.translate(str.maketrans(key1))
    print(_str)
    return _str


if __name__ == "__main__":
    with open("coded.txt", "r", encoding="utf-8") as f:
        text = f.read()

counter(text)

decoded = decoder(text)

with open("decoded.txt", "w", encoding="utf-8") as f1:
    f1.write(decoded)
