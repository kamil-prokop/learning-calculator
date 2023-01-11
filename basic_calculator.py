import logging
logging.basicConfig(level=logging.DEBUG)

intro_question = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

types_of_calculations = {
    "1": ["Dodawanie", "składnik", "składnik", "Dodaję", "do"],
    "2": ["Odejmowanie", "odjemną", "odjemnik", "Od", "odejmuję"],
    "3": ["Mnożenie", "czynnik", "czynnik", "Mnożę", "przez"],
    "4": ["Dzielenie", "dzielną", "dzielnik", "Dzielę", "przez"]
}
