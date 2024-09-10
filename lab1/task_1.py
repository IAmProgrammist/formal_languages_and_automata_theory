from libs.lab1 import solve_context_free_grammar_left, get_available_grammars_left

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    print("Левый вывод: ")
    i = 1
    commands = []
    result = (False, "S", "S")
    while not result[0]:
        print(f"Шаг {i}")
        print(f"Промежуточная цепочка: {result[1]}")
        print(f"Можно применить:")
        available_grammars = get_available_grammars_left(grammar_dict, result[1])
        for available_grammar in available_grammars:
            print(f"{available_grammar[0] + 1}. {available_grammar[1][0]} -> {available_grammar[1][1]}")
        while (apply_index := int(input("Введите правило: "))) not in (grammar[0] + 1 for grammar in available_grammars):
            print("Команда не подходит")
        commands.append(apply_index)
        result = solve_context_free_grammar_left(grammar_dict, [apply_index - 1], result[1], result[2])

    print(f"\nТерминальная цепочка: {result[1]}")
    print(f"Последовательность правил: {' '.join((str(command) for command in commands))}")
    print(f"ЛСФ ДВ: {result[2]}")


