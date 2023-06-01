def generator(move: int) -> dict:
    """
    :param move: alphabet movement
    :return: new alphabet
    """
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    key1 = {}
    for elem in alphabet:
        pos = alphabet.find(elem)
        key1[alphabet[pos]] = alphabet[(pos + move) % 33]

    print(key1)
    with open('key.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(key1))
    return key1


if __name__ == '__main__':
    key = generator(7)
    with open("orig.txt", "r", encoding="utf-8") as f1:
        text = f1.read().upper()
        encrypted_text = text.translate(str.maketrans(key))

        with open("encrypted.txt", "w", encoding="utf-8") as f2:
            f2.write(encrypted_text)
