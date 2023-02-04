import random
import uuid

class NLG:
    """
    Moduł, który tworzy reprezentację tekstową aktu systemowego wybranego przez taktykę dialogu.

    Wejście: Akt systemu (rama)

    Wyjście: Tekst
    """
    def __init__(self):
        pass

    def change_to_text(self, system_acts):
        """
        Funkcja zamieniająca akt systemu na tekst rozumiany przez użytkownika.
        """
        if(len(system_acts) == 0):
            return "Nie mam już nic do powiedzenia :("

        act = system_acts.pop(0)
        if(len(act) == 0):
            return "Nie mam już nic do powiedzenia :("

        for action in act:
            domain, intent = action
            if(domain == "greeting"):
                return random.choice(["Cześć, mam na imię Janet", "Hej, jestem Janet. W czym mogę pomóc?", "Dzień dobry, nazywam się Janet"])

            if(domain == "end_conversation"):
                return random.choice(["Dziękujemy za skorzystanie z naszych usług!", "Do widzenia!", "Do zobaczenia!"])

            if(domain == "appointment"):
                if (intent == "NoOffer"):
                    return "Proszę sprecyzować zapis na wizytę (lekarz, godzina)"
                if (intent == "book_appointent"):
                    answer = "Zarezerwowano wizytę"
                    for key in act[action]:
                        value = act[action][key]
                        if(key == "doctor"):
                            answer += f" do lekarza {value}"
                        if(key== "datetime"):
                            answer += f" umówiona na: {value}"
                    return answer
                if (intent == "set_appointment_date"):
                    value = act[action]["datetime"]
                    return f"Ustawiono datę wizyty na {value}"
            
            if(domain == "inform"):
                if (intent == "Doctors_list"):
                    value = act[action]["doctors"]
                    return f"Lista doktorów w naszej placówce: \n{value}"
                if (intent == "Medical_services"):
                    value = act[action]["services"]
                    return f"Lista usług oferowanych w naszej placówce: \n{value}"
                if (intent == "Location"):
                    city = act[action]["city"]
                    street = act[action]["street"]
                    number = act[action]["number"]
                    return f"Placówka znajduje się w {city}, {street} {number}"
                if (intent == "Opening_Hours"):
                    value = act[action]["hours"]
                    return f"Placówka jest otwarta w godzinach {value}"
                if (intent == "NoOffer"):
                    return f"Nie posiadam takiej wiedzy, żeby odpowiedzieć na to pytanie :("

            if(domain == "prescription"):
                if(intent == "create_prescription" or intent == "collect_prescription"):
                    answer = f"Odebrano receptę {uuid.uuid4().hex}"
                    return answer
                if(intent == "prescription type"):
                    return "Wszystkie recepty w naszej placówce są elektroniczne"
                if (intent == "NoOffer"):
                    return f"Nie rozumiem :("

