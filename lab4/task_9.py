InvalidStringError = ValueError("Invalid string detected")


def hold(data: str) -> str:
    return data


def next(data: str) -> str:
    return data[1:]


def replace(stack: str, value: str) -> str:
    return value[::-1] + stack[1:]


def pop(stack: str) -> str:
    return stack[1:] if stack != "∆" else stack


def print_step(data, stack, origin_data, rule):
    print(f"*********\n"
          f"Текущая цепочка: {origin_data[0:(len(origin_data) - len(data) + 1)]}{stack[:-1]}\n"
          f"Правило: {rule}\n\n")


def shift_reduce_parser(data):
    print(f"Трейсбек применяемых правил для {data}:")
    try:
        origin_data = data
        data += "┤"
        stack = "S∆"
        should_iter = -1
        while should_iter == -1:
            m = stack[0]
            x = data[0]
            if m == "∆" and data == "┤":
                if data == "┤":
                    should_iter = 1
                else:
                    raise InvalidStringError
            elif m == "S":
                stack, data = S(data, stack, origin_data)
            elif m == "O":
                stack, data = O(data, stack, origin_data)
            elif m == "E":
                stack, data = E(data, stack, origin_data)
            elif m == "T":
                stack, data = T(data, stack, origin_data)
            elif m == "P":
                stack, data = P(data, stack, origin_data)
            elif m == "A":
                stack, data = A(data, stack, origin_data)
            elif m == "B":
                stack, data = B(data, stack, origin_data)
            elif m == "C":
                stack, data = C(data, stack, origin_data)
            elif m == "D":
                stack, data = D(data, stack, origin_data)
            elif m == "F":
                stack, data = F(data, stack, origin_data)
            elif m == x:
                (stack, data) = (pop(stack), next(data))
            else:
                raise InvalidStringError
    except ValueError:
        print("Цепочка невалидна")
        raise InvalidStringError

    print("Цепочка валидна")

    return True


def S(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["a"]:
        print_step(data, stack, origin_data, "    1. S -> O;C")
        # 1
        return replace(stack, "C;O"), hold(data)

    raise InvalidStringError


def O(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["a"]:
        print_step(data, stack, origin_data, "    2. O -> aD")
        # 2
        return replace(stack, "D"), next(data)

    raise InvalidStringError


def E(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["(", "-", "a"]:
        print_step(data, stack, origin_data, "    3. E -> TA")
        # 3
        return replace(stack, "AT"), hold(data)

    raise InvalidStringError


def T(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["(", "-", "a"]:
        print_step(data, stack, origin_data, "    4. T -> PB")
        # 4
        return replace(stack, "BP"), hold(data)

    raise InvalidStringError


def P(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["("]:
        print_step(data, stack, origin_data, "    5. P -> (E)")
        # 5
        return replace(stack, ")E"), next(data)
    elif data[0] in ["-"]:
        print_step(data, stack, origin_data, "    6. P -> -(E)")
        # 6
        return replace(stack, ")E("), next(data)
    elif data[0] in ["a"]:
        print_step(data, stack, origin_data, "    7. P -> a")
        # 7
        return pop(stack), next(data)

    raise InvalidStringError


def A(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["+"]:
        print_step(data, stack, origin_data, "    8. A -> +TA")
        # 8
        return replace(stack, "AT"), next(data)
    elif data[0] in [")", ";"]:
        print_step(data, stack, origin_data, "    9. A -> ε")
        # 9
        return pop(stack), hold(data)

    raise InvalidStringError


def B(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["*"]:
        print_step(data, stack, origin_data, "    10. B -> *PB")
        # 10
        return replace(stack, "BP"), next(data)
    elif data[0] in ["+", ";", ")"]:
        print_step(data, stack, origin_data, "    11. B -> ε")
        # 9
        return pop(stack), hold(data)

    raise InvalidStringError


def C(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["a"]:
        print_step(data, stack, origin_data, "    12. C -> S")
        # 11
        return replace(stack, "S"), hold(data)
    elif data[0] in ["┤", "]"]:
        print_step(data, stack, origin_data, "    13. C -> ε")
        # 9
        return pop(stack), hold(data)

    raise InvalidStringError


def D(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["["]:
        print_step(data, stack, origin_data, "    14. D -> [S]F")
        # 12
        return replace(stack, "F]S"), next(data)
    elif data[0] in ["="]:
        print_step(data, stack, origin_data, "    15. D -> =E")
        # 13
        return replace(stack, "E"), next(data)

    raise InvalidStringError


def F(data: str, stack: str, origin_data: str) -> (str, str):
    if data[0] in ["["]:
        print_step(data, stack, origin_data, "    16. F -> [S]")
        # 14
        return replace(stack, "]S"), next(data)
    elif data[0] in [";"]:
        print_step(data, stack, origin_data, "    17. F -> ε")
        # 9
        return pop(stack), hold(data)

    raise InvalidStringError


if __name__ == "__main__":
    assert shift_reduce_parser("a[a=(a)*-(a)+a;];")
    assert shift_reduce_parser("a[a=a;][a=a;];")
    assert shift_reduce_parser("a=a;a=a;")
    try:
        shift_reduce_parser("a[a=(a)*-(a)+a+-(a);]")
        assert False
    except ValueError:
        assert True
    try:
        shift_reduce_parser("a=[];")
        assert False
    except ValueError:
        assert True
    try:
        shift_reduce_parser("a=[a=a;][a=a;][a=a;][a=a;];")
        assert False
    except ValueError:
        assert True
