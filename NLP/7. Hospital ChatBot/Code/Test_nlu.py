import jsgf

book_grammar = jsgf.parse_grammar_file('test_book.jsgf')
book_grammar

utterance = 'chciałbym zarezerwować stolik na jutro na godzinę dwunastą trzydzieści na cztery osoby'
matched = book_grammar.find_matching_rules(utterance)
matched

def get_dialog_act(rule):
    slots = []
    get_slots(rule.expansion, slots)
    return {'act': rule.grammar.name, 'slots': slots}

def get_slots(expansion, slots):
    if expansion.tag != '':
        slots.append((expansion.tag, expansion.current_match))
        return

    for child in expansion.children:
        get_slots(child, slots)

    if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
        get_slots(expansion.referenced_rule.expansion, slots)

get_dialog_act(matched[0])

def nlu(utterance):
    matched = book_grammar.find_matching_rules(utterance)

    if matched:
        return get_dialog_act(matched[0])
    else:
        return {'act': 'null', 'slots': []}

print(nlu('chciałbym zarezerwować stolik na jutro na godzinę dziesiątą dla trzech osób'))