import jsgf

class Book_NLU: #Natural Language Understanding
    """
    Moduł odpowiedzialny za analizę tekstu. W wyniku jego działania tekstowa reprezentacja wypowiedzi użytkownika zostaje zamieniona na jej reprezentację semantyczną, najczęściej w postaci ramy.

    Wejście: Tekst

    Wyjście: Akt użytkownika (rama)
    """
    def __init__(self, book_grammar):
        self.book_grammar = book_grammar
        
    def get_dialog_act(self, rule):
        slots = []
        self.get_slots(rule.expansion, slots)
        return {'act': rule.grammar.name, 'slots': slots}

    def get_slots(self, expansion, slots):
        if expansion.tag != '':
            slots.append((expansion.tag, expansion.current_match))
            return

        for child in expansion.children:
            self.get_slots(child, slots)

        if not expansion.children and isinstance(expansion, jsgf.NamedRuleRef):
            self.get_slots(expansion.referenced_rule.expansion, slots)

    def analyze(self, text): 
        """
        Analiza Tekstu wprowadzonego przez użytkownika i zamiana na akt (rama)
        """
        print("Analiza Tekstu: " + text)
        act = "(greetings()&request(name))"
        print("Akt to: " + act)
        #przerobienie na wektor
        act_vector = [[0],[1,0]] #1 wektor to greetings, a 2 wektor to request z argumentem "name"
        print("Zamiana na: ")
        print(act_vector)
        return act_vector 

    def test_nlu(self, utterance):
        matched = self.book_grammar.find_matching_rules(utterance)
        print(matched)

        if matched:
            return self.get_dialog_act(matched[0])
            
        else:
            return {'act': 'null', 'slots': []}