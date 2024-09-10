def solve_context_free_grammar(grammar_dict, commands, chain=None, tree=None, step=0):
    # Если команды закончились, выходим из рекурсии
    if step >= len(commands):
        yield (True, chain, tree)
    else:
        # Инициализация цепочки, дерева
        if not chain:
            chain = "S"
            tree = "S"

        # Определяем доступные грамматики
        available_grammars = []
        for i in range(0, len(grammar_dict)):
            grammar = grammar_dict[i]
            if grammar[0] in chain:
                available_grammars.append((i, grammar))

        # Если команды нет в доступных грамматиках, возвращаем False
        if commands[step] not in [available_grammar[0] for available_grammar in available_grammars]:
            pass
        else:
            # Иначе пытаемся выполнить команду для всех возможных нетерминальных символов по-очереди
            grammar = grammar_dict[commands[step]]
            splitted_chain = chain.split(grammar[0])
            splitted_tree = tree.replace(f"{grammar[0]}(", "*").split(grammar[0])

            for i in range(0, len(splitted_chain) - 1):
                # Проивзодим замену для цепочки
                new_chain = grammar[0].join(splitted_chain[:i+1]) + grammar[1] + grammar[0].join(splitted_chain[i+1:])

                # Производим замену для дерева
                new_tree = (grammar[0].join(splitted_tree[:i+1]) +
                            grammar[0] + "(" + grammar[1] + ")" +
                            grammar[0].join(splitted_tree[i+1:])).replace("*", f"{grammar[0]}(")

                # Вызываем рекурентно преобразования для следующей команды
                yield from solve_context_free_grammar(grammar_dict, commands, new_chain, new_tree, step + 1)
