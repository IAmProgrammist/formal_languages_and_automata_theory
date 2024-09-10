from libs.lab1 import task2

if __name__ == '__main__':
    grammar_dict = []
    print("Введите КС-грамматику:")
    while len(grammar := input()):
        splitted_grammar = grammar.split(" -> ")
        grammar_dict.append((splitted_grammar[0], splitted_grammar[1]))
    required = input("Введите ожидаемую строку: ")

    result = task2.solve_context_free_grammar_rec(grammar_dict, 13, required)
