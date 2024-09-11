def solve_context_free_grammar(grammar_dict, rules, chain=None, tree=None, step=0):
    """
    Рекурсивная проверка последовательности правил в грамматике

    1. Если в последовательности правил больше не осталось шагов, выходим из рекурсии.
    2. Для всех нетерминальных символов в промежуточной цепочке находим правила, которые можно применить.
    3. Если правила на текущем шаге не окажется в полученном списке правил, значит выходим из рекурсии.
    4. Иначе получим непосредственный вывод для правила для каждого нетерминала в промежуточной цепочке и перейдём к сдедующему шагу рекурсии.
    Например для промежуточной цепочки aSbScSi и правила S -> h будут получены следующие непосредтвенные выводы:
    * aSbScSi => ahbScSi => (рекурсивный вызов)
    * aSbScSi => aSbhcSi => (рекурсивный вызов)
    * aSbScSi => aSbSchi => (рекурсивный вызов)
    """

    # Если в последовательности правил больше не осталось шагов, выходим из рекурсии
    if step >= len(rules):
        yield (True, chain, tree)
    else:
        # Инициализация цепочки, дерева
        if not chain:
            chain = "S"
            tree = "S"

        # Для всех нетерминальных символов в промежуточной цепочке находим правила, которые можно применить
        available_rules = []
        for i in range(0, len(grammar_dict)):
            grammar = grammar_dict[i]
            if grammar[0] in chain:
                available_rules.append((i, grammar))

        # Если правила на текущем шаге не окажется в полученном списке правил, значит выходим из рекурсии
        if rules[step] not in [available_grammar[0] for available_grammar in available_rules]:
            pass
        else:
            # Иначе получим непосредственный вывод для правила для каждого нетерминала в промежуточной цепочке и перейдём к сдедующему шагу рекурсии
            grammar = grammar_dict[rules[step]]
            splitted_chain = chain.split(grammar[0])
            splitted_tree = tree.replace(f"{grammar[0]}(", "*").split(grammar[0])

            for i in range(0, len(splitted_chain) - 1):
                # Применяем правило для цепочки
                new_chain = grammar[0].join(splitted_chain[:i+1]) + grammar[1] + grammar[0].join(splitted_chain[i+1:])

                # Применяем правило для дерева
                new_tree = (grammar[0].join(splitted_tree[:i+1]) +
                            grammar[0] + "(" + grammar[1] + ")" +
                            grammar[0].join(splitted_tree[i+1:])).replace("*", f"{grammar[0]}(")

                # Вызываем рекурентно функцию для обработки следующего шага
                yield from solve_context_free_grammar(grammar_dict, rules, new_chain, new_tree, step + 1)
