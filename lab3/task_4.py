MESSAGES = {
    -1: "Отвергнуть, последовательность пуста",
    -2: "Отвергнуть, невалидный входной символ",
    -3: "Отвергнуть, слишком короткая цепочка",
    -4: "Отвергнуть, последние два символа не содержат 1",
    0: "Допустить"
}

def S1(input):
    if len(input) == 0:
        return -1

    if input[0] == '1':
        return S2(input[1:])
    elif input[0] == '0':
        return S3(input[1:])
    else:
        return -2

def S2(input):
    if len(input) == 0:
        return -3

    if input[0] == '1':
        return S4(input[1:])
    elif input[0] == '0':
        return S5(input[1:])
    else:
        return -2

def S3(input):
    if len(input) == 0:
        return -4

    if input[0] == '1':
        return S4(input[1:])
    elif input[0] == '0':
        return S3(input[1:])
    else:
        return -2


def S4(input):
    if len(input) == 0:
        return 0

    if input[0] == '1':
        return S4(input[1:])
    elif input[0] == '0':
        return S5(input[1:])
    else:
        return -2


def S5(input):
    if len(input) == 0:
        return 0

    if input[0] == '1':
        return S4(input[1:])
    elif input[0] == '0':
        return S3(input[1:])
    else:
        return -2

def L3validator(input):
    result = S1(input)
    print(input, MESSAGES[result])
    return result


# Тестовые данные для всех переходов
assert L3validator("10001101") == 0
assert L3validator("11") == 0
assert L3validator("01") == 0


# Тестовые данные для всех состояний
assert L3validator("") == -1
assert L3validator("1") == -3
assert L3validator("0") == -4
assert L3validator("11") == 0
assert L3validator("10") == 0