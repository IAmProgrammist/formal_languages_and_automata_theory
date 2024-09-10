from libs.lab1 import solve_context_free_grammar_left

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    commands = [int(v) - 1 for v in input("Введите команды: ").split()]

    result = solve_context_free_grammar_left(grammar_dict, commands)
    print(f"Цепочка: {result[1]}, дерево: {result[2]}")


