MESSAGES = {
    -1: "Отвергнуть, невалидный входной символ",
    0: "Отвергнуть, цепочка не содержит 1 на одной из двух последних позиций",
    1: "Допустить",
}

PERMITTING = [1, 2]

MATRIX = {
    "1": [1, 1, 1],
    "0": [0, 2, 0]
}


def l3_validator(l3_input):
    original_input = l3_input
    s = 0
    while len(l3_input) > 0 and s >= 0:
        current_symbol = l3_input[0]
        if current_symbol in MATRIX:
            s = MATRIX[l3_input[0]][s]
        else:
            s = -1
            break

        l3_input = l3_input[1:]

    if s in PERMITTING:
        s = 1

    print(original_input, MESSAGES[s])
    return s


# Тестовые данные для всех переходов
assert l3_validator("0110100") == 0
assert l3_validator("21") == -1

# Тестовые данные для всех состояний
assert l3_validator("") == 0
assert l3_validator("1") == 1
assert l3_validator("10") == 1
assert l3_validator("21") == -1
