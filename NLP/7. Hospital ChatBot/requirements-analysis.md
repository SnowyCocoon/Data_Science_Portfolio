System rezerwacji wizyt u lekarza
==============

Zadanie 0: Logowanie do systemu (połączone z 2,3,14,15,21)
--------------------------------

*system:* Proszę podać swój identyfikator w systemie.

*user:* 1234567890

*system:* Proszę podać swoje hasło.

*user:* xxxx

Zadanie 1: Rejestracja w systemie przychodni 
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, chciałbym zarejestrować się do systemu.

*system:* W celu rejestracji do systemu potrzebujemy Twojej zgody na przetwarzanie danych osobowych, więcej informacji na temat przetwarzania danych osobowych znajdziesz **tutaj (link)**. Czy przeczytałeś regulamin i akceptujesz powyższe zgody? (TAK/NIE)

*user:* Tak

*system:* Proszę podać swoje imię

*user:* Jan

*system:* Proszę podać swoje nazwisko

*user:* Kowalski

*system:* Proszę podać swój adres email

*user:* jan.kowalski@wp.pl

*system:* Proszę podać swoje hasło

*user:* *************

*system:* Proszę powtórzyć hasło

*user:* *************

*system:* Proszę podać swój pesel

*user:* ###########

*system:* Twoje konto zostało zarejestrowane. Twój identyfikator to 123456. 

Zadanie 2: Rezerwacja wizyty (logowanie)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, chciałbym zarezerwować wizytę.

**Zadanie 0 (logowanie)**

*system:* Do jakiego specjalisty zarezerwować wizytę.

*user:* Jan Kowalski

*system:* Najbliższe wolne terminy to:
            - 14.02.2021 - 14:30
            - 24.03.2021 - 11:00

*user:* 14.02.2021 - 14:30

*system:* Wizyta została zarezerwowana.

Zadanie 3: Przeniesienie wizyty (logowanie)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Chciałbym/Chciałabym przenieść swoją wizytę na inny termin?

**Zadanie 0 (logowanie)**

*system* Proszę podać ID wizyty

*user:* XXXXXXXXXX (ID wizyty)

*system* Proszę wybrać dzień w formacie (DD.MM.RRRR) na który przenieść wizytę

*user:* XX.XX.XXXX (DD.MM.RRRR)

*system* W danym dniu można się umówić na wizytę w godzinach : xx.xx, xx.xx, xx.xx.... (Jeżeli nie ma terminu w danym dniu, to system prosi o podanie innej daty)

*user:* xx.xx (HH.MM)

*system* Dziękujemy, wizyta o ID: XXXXXXXXXX została przeniesiona na DD.MM.RRRR, HH.MM

Zadanie 4: Porada odnośnie symptomów (Sieć neuronowa do określenia prostej choroby na podstawie symptomów)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Boli mnie XXX, Źle się czuję, Jest mi niedobrze, Mam XX.XX Stopni, ...

*system:* Proszę podać więcej informacji.

*user:* XXX, XXX, XXX, XXX, XXX

*system:* To może być XXXX. Nie jest to nic poważnego. Jeżeli jednak obawiasz się o swoje zdrowie, proszę zapisać się na wizytę.

*system:* To może być XXXX. Nie jest to choroba, którą powinno się ignorować. Przeniesiemy Pana/Panią do systemu zapisów.


Zadanie 5: Czy mam prawo do zmiany lekarza pierwszego kontaktu i w jaki sposób to zrobić?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, jak zmienić lekarza pierwszego kontaktu?

*system:* Zmiana lekarza następuje po złożeniu odpowiedniej deklaracji w placówce przychodni. Deklarację można zmienić dwa razy w roku.

Zadanie 6: Czy są oferowane wizyty domowe?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, czy w ofercie znajdują się wizyty domowe?

*system:* W naszej ofercie znajdują się wizyty domowe lekarzy internistów. Wizyty tego rodzaju zalecane są osobom starszym.

Zadanie 7: W jakim wypadku mogę skorzystać ze świadczeń opieki zdrowotnej poza kolejnością?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Kiedy mogę skorzystać ze świadczeń opieki zdrowotnej poza kolejnością?

*system:* Ze świadczeń opieki zdrowotnej poza kolejnością mogą skorzystać osoby z zagrożeniem zdrowia lub życia, bądź z pakietem rozszerzonym.

Zadanie 8: Czy do lekarza specjalisty muszę mieć skierowanie?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, czy do lekarza specjalisty potrzebuję skierowania?

*system:* W ramach działania naszej placówki oferowane są jedynie poradnie prywatne, nie honorujemy konsultacji lekarskich na NFZ w tym skierowań na badania. Do lekarza specjalisty skierowanie jest niewymagane.

Zadanie 9: Czy lekarz pierwszego kontaktu przyjmuje w soboty?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Czy lekarz pierwszego kontaktu przyjmuje w soboty?

*system:* Nasza przychodnia jest otwarta 24 godziny na dobę, 7 dni w tygodniu. W takim wypadku lekarz pierwszego kontaktu przyjmuje pacjentów w soboty.

Zadanie 10: Jakie są godziny otwarcia przychodni?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Jakie są godziny otwarcia przychodni?

*system:* Przychodnia jest otwarta 24 godziny na dobę.


Zadanie 11: Czy do przychodni mogą zapisać się osoby nieubezpieczone?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Czy do przychodni mogą zapisać się osoby nieubezpieczone?

*system:* Oczywiście, że tak.

Zadanie 12: Czy przychodnia jest NFZ/prywatna?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Czy przychodnia jest NFZ?

*system:* Przychodnia jest całkowicie prywatna.

Zadanie 13: Gdzie znajdują się placówki?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Gdzie znajdują się placówki?

*system:* Proszę podać województwo

*user:* XXXXXX

*system:* W danym województwie nasze placówki znajdują się w następujących miejscach: (po 1 na województwo)
-> Poznań, ul. Święty Marcin 12/73  60-805
-> .....

Zadanie 14: Sprawdź swoje wizyty (logowanie)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* W jakie dni mam zaplanowane wizyty?

**Zadanie 0 (logowanie)**

*system:*  Ma Pan/Pani wizyty w poszczególne dni:  
            - 14.02.2021 - Dentysta Anna Kowalska,  
            - 24.03.2021 - Okulista Jan Kowalski  

Zadanie 15: Sprawdź swoje wyniki (logowanie)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Chciałabym sprawdzić wyniki swoich badań

**Zadanie 0 (logowanie)**

*system:* Lista wyników Twoich badań z ostatnich 60 dni:  
            - Wyniki badań okulistycznych (21.03.2021) [1]  
            - Wyniki badań cytologicznych (19.03.2021) [2]  
            W celu sprawdzenia konkrentego badania wpisz jego numer

*user:* 1

*system:* Plik podsumowywujący badanie: **tutaj (link)**  
Komentarz doktora: "Wszystko w normie"

Zadanie 16: Pytanie o cennik
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Jakie są ceny za usługi w przychodni?

*system:* Czy interesuje Pana/Panią: 
1. Ubezpieczenie
2. Pojedyńcza wizyta bez ubezpieczenia
3. Wizyty w ramach ubezpieczenia

*user:* (1/2/3)

*system:* Ceny ubezpieczeń zaczynają się już od 500 zł miesięcznie! Po szczegółowe informacje proszę udać sie na strone www.JanetMed.com **(Ceny ubezpieczeń)**

*system:* Wizyta do lekarza internisty/okulisty/dentysty to już 100zł za badanie! Po szczegółowe informacje proszę udać sie na strone www.JanetMed.com **(Ceny pojedyńczej wizyty bez ubezpieczenia)**

*system:* Wszystkie podstawowe badania są oferowane za darmo dla klientów ubezpieczonych. W przypadku chęci zapisania się na operację lub zabieg specjalistyczny, cena zależy od rodzaju ubezpieczenia (Najtańsze zwalnia już z 75% kosztów!). Po szczegółowe informacje proszę udać sie na strone www.JanetMed.com **(Ceny Wizyt w ramach ubezpieczenia)**

Zadanie 17: Czy lekarz może odmówić wydania skierowania?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, czy lekarz może odmówić wydania skierowania na badania?

*system:* Lekarz może odmówić wydania skierowania jeżeli uzna, że pacjent nie ma wskazań do badania.

Zadanie 18: Jakie są konsekwencje niepojawienia się na wizycie?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Jakie są konsekwencje niepojawienia się na wizycie?

*system:* Czy jest Pan/Pani ubezpieczona w naszej przychodni?

*user:* Tak/Nie

*system:* **(Nie)** Jeżeli nie jest Pan/Pani ubezpieczony/a, to pobierana jest zaliczka wysokości 20% ceny umówionego spotkania.

*system:* **(Tak)** Jeżeli jest Pan/Pani u nas ubezpieczony/a, to nie ponosi Pan/Pani żadnych konsekwencji.

Zadanie 19: Wykaz specjalistów na przychodni
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Jacy specjaliści pracują w przychodni?

*system:* Specjaliści pracujący w przychodni:  
    - Dentysta Anna Kowalska  
    - Okulista Jan Kowalski  
    - Internista Andrzej Mroży  
    - Ginekolog Paweł Borowski  

Zadanie 20: Jak przygotować się do badania krwi?
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, w jaki sposób przygotować się na badanie krwi?

*system:* Na pobieranie krwi przyjdź na czczo, nie przyjmuj pokarmów przez około 12 godzin. Unikaj spożywania alkoholu oraz wysiłku fizycznego co najmniej dzień przed. Przed zabiegiem wypij niewielką ilość wody.

Zadanie 21: Anulowanie rezerwacji (logowanie)
--------------------------------

*system:* Witamy w systemie przychodni dr. Janet.

*user:* Dzień dobry, chciałbym anulować wizytę.

**Zadanie 0 (logowanie)**

*system:*  Ma Pan/Pani wizyty w poszczególne dni: x,x,x,x,x. Proszę wybrać którą wizytę chce Pan/Pani anulować.

*user:* 14.04

*system:* wizyta została anulowana.