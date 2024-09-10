def solve_context_free_grammar_left(grammar_dict, commands):
    # Инициализация цепочки, дерева
    chain = "S"
    tree = "S"
    step = 0

    # Пока в цепочке есть нетерминальные символы и пул команд непустой
    while any([v.isupper() for v in chain]) and step < len(commands):
        # Определяем доступные грамматики
        available_grammars = []
        min_index = len(chain)
        for i in range(0, len(grammar_dict)):
            grammar = grammar_dict[i]
            if (index := chain.find(grammar[0])) != -1 and index < min_index:
                available_grammars = [(i, grammar)]
                min_index = index
            elif index == min_index:
                available_grammars.append((i, grammar))

        # Если команды нет в доступных грамматиках, возвращаем False
        if commands[step] not in [available_grammar[0] for available_grammar in available_grammars]:
            return (False, chain, tree)

        # Иначе производим замену для цепочки
        apply_index = commands[step]
        grammar = grammar_dict[apply_index]
        splitted_chain = chain.split(grammar[0])
        chain = splitted_chain[0] + grammar[1] + grammar[0].join(splitted_chain[1:])

        # Производим замену для дерева
        splitted_tree = tree.replace(f"{grammar[0]}(", "*").split(grammar[0])
        tree = (splitted_tree[0] + grammar[0] + "(" + grammar[1] + ")" + grammar[0].join(splitted_tree[1:])).replace(
            "*", f"{grammar[0]}(")

        step += 1

    # Если выполнены не все команды, выходим с ошибкой
    if len(commands) != step:
        return (False, chain, tree)

    return (True, chain, tree)