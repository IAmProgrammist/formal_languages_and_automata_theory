InvalidStringError = ValueError("Invalid string detected")


def process_terminal(data, terminal):
    if data[0] == terminal:
        data = data[1:]
    else:
        raise InvalidStringError

    return data


def S(data: str) -> str:
    if data[0] in ["a"]:
        print("    1. S -> O;C")
        data = O(data)
        data = process_terminal(data, ";")
        data = C(data)
    else:
        raise InvalidStringError

    return data


def O(data: str) -> str:
    if data[0] in ["a"]:
        print("    2. O -> aD")
        data = process_terminal(data, "a")
        data = D(data)
    else:
        raise InvalidStringError

    return data


def E(data: str) -> str:
    if data[0] in ["(", "-", "a"]:
        print("    3. E -> TA")
        data = T(data)
        data = A(data)
    else:
        raise InvalidStringError

    return data


def T(data: str) -> str:
    if data[0] in ["(", "-", "a"]:
        print("    4. T -> PB")
        data = P(data)
        data = B(data)
    else:
        raise InvalidStringError

    return data


def P(data: str) -> str:
    if data[0] in ["("]:
        print("    5. P -> (E)")
        data = process_terminal(data, "(")
        data = E(data)
        data = process_terminal(data, ")")
    elif data[0] in ["-"]:
        print("    6. P -> -(E)")
        data = process_terminal(data, "-")
        data = process_terminal(data, "(")
        data = E(data)
        data = process_terminal(data, ")")
    elif data[0] in ["a"]:
        print("    7. P -> a")
        data = process_terminal(data, "a")
    else:
        raise InvalidStringError

    return data


def A(data: str) -> str:
    if data[0] in ["+"]:
        print("    8. A -> +TA")
        data = process_terminal(data, "+")
        data = T(data)
        data = A(data)
    elif data[0] in [")", ";"]:
        print("    9. A -> ε")
        pass
    else:
        raise InvalidStringError

    return data


def B(data: str) -> str:
    if data[0] in ["*"]:
        print("    10. B -> *PB")
        data = process_terminal(data, "*")
        data = P(data)
        data = B(data)
    elif data[0] in ["+", ";", ")"]:
        print("    11. B -> ε")
        pass
    else:
        raise InvalidStringError

    return data


def C(data: str) -> str:
    if data[0] in ["a"]:
        print("    12. C -> S")
        data = S(data)
    elif data[0] in ["┤", "]"]:
        print("    13. C -> ε")
        pass
    else:
        raise InvalidStringError

    return data


def D(data: str) -> str:
    if data[0] in ["["]:
        print("    14. D -> [S]F")
        data = process_terminal(data, "[")
        data = S(data)
        data = process_terminal(data, "]")
        data = F(data)
    elif data[0] in ["="]:
        print("    15. D -> =E")
        data = process_terminal(data, "=")
        data = E(data)
    else:
        raise InvalidStringError

    return data


def F(data: str) -> str:
    if data[0] in ["["]:
        print("    16. F -> [S]")
        data = process_terminal(data, "[")
        data = S(data)
        data = process_terminal(data, "]")
    elif data[0] in [";"]:
        print("    17. F -> ε")
        pass
    else:
        raise InvalidStringError

    return data


def LL1(data):
    print(f"Трейсбек применяемых правил для {data}:")
    data += "┤"
    try:
        result = S(data)
    except ValueError:
        print("Цепочка невалидна")
        raise InvalidStringError

    if result == "┤":
        print("Цепочка валидна")
        return True
    else:
        print("Цепочка невалидна")
        raise InvalidStringError


def main():
    LL1(input())

if __name__ == "__main__":
    assert LL1("a[a=(a)*-(a)+a;];")
    assert LL1("a[a=a;][a=a;];")
    assert LL1("a=a;a=a;")
    try:
        LL1("a[a=(a)*-(a)+a+-(a);]")
        assert False
    except ValueError:
        assert True
    try:
        LL1("a=[];")
        assert False
    except ValueError:
        assert True
    try:
        LL1("a=[a=a;][a=a;][a=a;][a=a;];")
        assert False
    except ValueError:
        assert True
