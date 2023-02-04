from collections import defaultdict

class DP():
    """
    Moduł decydujący o wyborze kolejnego aktu, który ma podjąć system prowadząc rozmowę.

    Wejście: Reprezentacja stanu dialogu (rama)

    Wyjście: Akt systemu (rama)
    """
    

    def predict(self, state):
        self.results = []
        system_action = defaultdict(dict)
        user_action = defaultdict(list)
        system_acts = []
        while len(state['user_action']) > 0:
            intent, domain, slot, value = state['user_action'].pop(0)
            user_action[(domain, intent)].append((slot, value))

        for user_act in user_action:
            system_acts.append(self.update_system_action(user_act, user_action, state, system_action))
        
        state['system_action'] = system_acts
        print(state)
        print("\n")
        return system_acts
            

        # # Reguła 3
        # if any(True for slots in user_action.values() for (slot, _) in slots if slot in ['Stay', 'Day', 'People']):
        #     if self.results:
        #         system_action = {('Booking', 'Book'): [["Ref", self.results[0].get('Ref', 'N/A')]]}

        # system_acts = [[intent, domain, slot, value] for (domain, intent), slots in system_action.items() for slot, value in slots]
        # state['system_action'] = system_acts
        # return system_acts

    def update_system_action(self, user_act, user_action, state, system_action):
        domain, intent = user_act

        # Reguła 1

        if domain == 'appointment':
            constraints = [(slot, value) for slot, value in state['belief_state'][domain.lower()].items() if value != '']
            if len(constraints) == 0:
                    system_action[(domain, 'NoOffer')] = []
            elif intent == 'appointment/create_appointment':
                for x in constraints:
                    if(x[0] == 'doctor'):
                        system_action[(domain, 'book_appointent')][x[0]] = x[1]
                for y in constraints:
                    if(y[0] == 'datetime'):
                        system_action[(domain, 'book_appointent')][y[0]] = y[1]
            elif intent == 'appointment/set_date':
                for y in constraints:
                    if(y[0] == 'datetime'):
                        system_action[(domain, 'set_appointment_date')][y[0]] = y[1]


        
        #################################################################################################
        # Reguła 2

        if domain == 'request_information':
            constraints_v2 = [(slot, value) for slot, value in state['request_state'][domain.lower()].items() if value != '']
            if intent == 'request_information/available_dates':
                for x in constraints_v2:
                    if(x[0] == 'doctor'):
                        system_action[(domain, 'date_info')][x[0]] =  x[1]
                for y in constraints_v2:
                    if(y[0] == 'datetime'):
                        system_action[(domain, 'date_info')][y[0]] = y[1]
            elif intent == 'request_information/doctors':
                system_action[("inform", 'Doctors_list')] = {"doctors": "dr. Kolano - okulista, dr. Kowalski - internista, dr. Kaszak - ginekolog"}
            elif intent == 'request_information/location':
                system_action[("inform", 'Location')] = {"street": "Marszałkowska", "number": "45", "city": "Poznań"}
            elif intent == 'request_information/cost':
                system_action[("inform", 'Cost')] = {"cost": "100 zł"}
            elif intent == 'request_information/opening_hours':
                system_action[("inform", 'Opening_Hours')] = {"hours": "'8:00 - 16:00"}
            elif intent == 'request_information/medical_services':
                system_action[("inform", 'Medical_services')] = {"services": "Okulista, Internista, Ginekolog"}
            elif len(constraints) == 0:
                system_action[("inform", 'NoOffer')] = {'0': '0'}

        #################################################################################################
        # Reguła 3
        if domain == 'end_conversation':
            system_action[(domain, 'End_Conversation')] = {'0': '0'}
        
        #################################################################################################
        # Reguła 4
        if domain == 'greeting':
            system_action[(domain, 'Greeting')] = {'0': '0'}

        #################################################################################################
        # Reguła 5
        if domain == 'prescription':
            constraints_v2 = [(slot, value) for slot, value in state['request_state'][domain.lower()].items() if value != '']
            if intent == 'prescription/request':
                for x in constraints_v2:
                    if(x[0] == 'prescription/type'):
                        system_action[(domain, 'create_prescription')][x[0]] = x[1]
                for y in constraints_v2:
                    if(y[0] == 'prescription/medicine'):
                        system_action[(domain, 'create_prescription')][y[0]] = y[1]
            elif intent == 'prescription/collect':
                for x in constraints_v2:
                    if(x[0] == 'prescription/type'):
                        system_action[(domain, 'collect_prescription')][x[0]] = x[1]
            elif intent == 'prescription/type':
                for x in constraints_v2:
                    if(x[0] == 'prescription/type_info'):
                        system_action[(domain, 'prescription type')][x[0]] =  x[1]
            if len(constraints_v2) == 0:
                system_action[(domain, 'NoOffer')] = []

        return system_action
                     
        ## Brakuje: Rejestracja, Login, Hasło, affirm, deny