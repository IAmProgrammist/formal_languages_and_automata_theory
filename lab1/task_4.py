from libs.lab1 import solve_context_free_grammar_left, solve_context_free_grammar_right

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    commands = [int(v) - 1 for v in input("Введите последовательность правил: ").split()]

    result1 = solve_context_free_grammar_left(grammar_dict, commands)
    result2 = solve_context_free_grammar_right(grammar_dict, commands)
    print(f"Заданную последовательность правил применить {'можно при левом выводе' if result1[0] else 'можно при правом выводе' if result2[0] else 'нельзя'}")
