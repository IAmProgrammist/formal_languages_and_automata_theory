MESSAGES = {
    -1: "Отвергнуть, невалидный входной символ",
    0:  "Отвергнуть, цепочка не содержит 1 на одной из двух последних позиций",
    1:  "Допустить",
    2:  "Допустить"
}


def l3_validator(l3_input):
    original_input = l3_input
    s = 0
    while len(l3_input) > 0 and s >= 0:
        current_symbol = l3_input[0]
        if s == 0:
            if current_symbol == "1":
                s = 1
            elif current_symbol == "0":
                s = 0
            else:
                s = -1
                break
        elif s == 1:
            if current_symbol == "1":
                s = 1
            elif current_symbol == "0":
                s = 2
            else:
                s = -1
                break
        elif s == 2:
            if current_symbol == "1":
                s = 1
            elif current_symbol == "0":
                s = 0
            else:
                s = -1
                break

        l3_input = l3_input[1:]

    print(original_input, MESSAGES[s])
    return s


# Тестовые данные для всех переходов
assert l3_validator("0110100") == 0
assert l3_validator("21") == -1

# Тестовые данные для всех состояний
assert l3_validator("") == 0
assert l3_validator("1") == 1
assert l3_validator("10") == 2
assert l3_validator("21") == -1
