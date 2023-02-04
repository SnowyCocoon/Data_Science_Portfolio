import json

class Rules_DST(): #Dialogue State Tracker
    """
    Moduł odpowiedzialny za śledzenie stanu dialogu. Przechowuje informacje o tym jakie dane zostały uzyskane od użytkownika w toku prowadzonej konwersacji.

    Wejście: Akt użytkownika (rama)

    Wyjście: Reprezentacja stanu dialogu (rama)
    """
    def __init__(self):
        self.state = json.load(open('default_state.json'))

    def update_user(self, user_acts=None):
        for intent, domain, slot, value in user_acts:
            self.state["user_action"].append([intent, domain, slot, value])
            if domain in ['password', 'name', 'email', 'enter_email', 'enter_name']:
                return

            if 'appointment' in intent:
                if (slot == 'appointment'):
                    continue
                
                if(domain in slot):
                    slot.replace(domain + "/", '')

                domain_dic = self.state['belief_state'][domain]
                if slot in domain_dic:
                    self.state['belief_state'][domain][slot] = value
            
            if 'prescription' in intent:
                if (slot == 'prescription'):
                    continue
                
                if(domain in slot):
                    slot.replace(domain + "/", '')

                if domain not in self.state['request_state']:
                    self.state['request_state'][domain] = {}
                if slot not in self.state['request_state'][domain]:
                    self.state['request_state'][domain][slot] = value

            if 'request_information' in intent:
                if (slot == 'request_information'):
                    continue
                
                if(domain in slot):
                    slot.replace(domain + "/", '')

                if domain not in self.state['request_state']:
                    self.state['request_state'][domain] = {}
                if slot not in self.state['request_state'][domain]:
                    self.state['request_state'][domain][slot] = value

            elif intent == 'end_conversation':
                self.state = json.load(open('default_state.json'))
        return self.state