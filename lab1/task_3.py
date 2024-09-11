from libs.lab1 import solve_context_free_grammar_left

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    commands = [int(v) - 1 for v in input("Введите последовательность правил: ").split()]

    result = solve_context_free_grammar_left(grammar_dict, commands)
    if result[0]:
        print("Заданную последовательность правил при левом выводе применить можно.")
    else:
        print("Заданную последовательность правил при левом выводе применить нелзя.")
        print(f"В промежуточной цепочке {result[1]} нельзя применить "
              f"правило {commands[result[3]] + 1}. {grammar_dict[commands[result[3]]][0]} -> {grammar_dict[commands[result[3]]][1]} "
              f"под шагом {result[3] + 1}.")
