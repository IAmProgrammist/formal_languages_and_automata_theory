def solve_context_free_grammar_rec(grammar_dict, recursion_depth, required, chain = None, tree = None):
    if recursion_depth == -1:
        return
    if required == chain:
        print("Place a debug point here and trace recursion stack to get modifications")
    if not chain:
        # Инициализация цепочки, дерева
        chain = "S"
        tree = "S"

    # Пока в цепочке есть нетерминальные символы и пул команд непустой
    if any([v.isupper() for v in chain]):
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

        for available_grammar in available_grammars:
            # Иначе производим замену для цепочки
            grammar = available_grammar[1]
            splitted_chain = chain.split(grammar[0])
            chain_new = splitted_chain[0] + grammar[1] + grammar[0].join(splitted_chain[1:])

            # Производим замену для дерева
            splitted_tree = tree.replace(f"{grammar[0]}(", "*").split(grammar[0])
            tree_new = (splitted_tree[0] + grammar[0] + "(" + grammar[1] + ")" + grammar[0].join(splitted_tree[1:])).replace(
                "*", f"{grammar[0]}(")
            new_rec = recursion_depth - 1
            solve_context_free_grammar_rec(grammar_dict, new_rec, required, chain_new, tree_new)
    elif required == chain:
        print("Place a debug point here and trace recursion stack to get modifications")