MESSAGES = {
    0: "Отвергнуть, последовательность пуста",             # -1
    3: "Отвергнуть, невалидный входной символ",            # -2
    1: "Отвергнуть, слишком короткая цепочка",             # -3
    2: "Отвергнуть, последние два символа не содержат 1",  # -4
    4: "Допустить",                                       # 0
}

PERMITTING = [3, 4]

MATRIX = {
    "1": [1, 3, 3, 3, 3],
    "0": [2, 4, 2, 4, 2]
}

def L3validator(input):
    input_origin = input
    S = 0
    while len(input) > 0 and S >= 0:
        S = MATRIX[input[0]][S]
        input = input[1:]

    if S in PERMITTING:
        S = 4

    print(input_origin, MESSAGES[S])
    return S



# Тестовые данные для всех переходов
assert L3validator("10001101") == 4
assert L3validator("11") == 4
assert L3validator("01") == 4


# Тестовые данные для всех состояний
assert L3validator("") == 0
assert L3validator("1") == 1
assert L3validator("0") == 2
assert L3validator("11") == 4
assert L3validator("10") == 4