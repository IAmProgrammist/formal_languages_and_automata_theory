from libs.lab1 import task1

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    commands = [int(v) - 1 for v in input("Введите команды: ").split()]

    result = task1.solve_context_free_grammar_left(grammar_dict, commands)
    print(f"Заданную последовательность правил применить {'можно' if result[0] else 'нельзя'}")
