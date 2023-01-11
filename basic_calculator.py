import logging
logging.basicConfig(level=logging.DEBUG)

intro_question = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

types_of_calculations = {
    "1": ["Dodawanie", "składnik", "składnik", "Dodaję", "do"],
    "2": ["Odejmowanie", "odjemną", "odjemnik", "Od", "odejmuję"],
    "3": ["Mnożenie", "czynnik", "czynnik", "Mnożę", "przez"],
    "4": ["Dzielenie", "dzielną", "dzielnik", "Dzielę", "przez"]
}

specification_order_first = specification_order_second = " "

if (intro_question == "1" or intro_question == "3"):
    specification_order_first = " 1"
    specification_order_second = " 2"

first_number_text = "Podaj " + types_of_calculations.get(intro_question)[1] + specification_order_first + ": "
first_number = float(input(first_number_text))

second_number_text = "Podaj " + types_of_calculations.get(intro_question)[2] + specification_order_second + ": "
second_number = float(input(second_number_text))

arithmetic_description = str(str(types_of_calculations.get(intro_question)[3]) + " " + str(first_number) + " " 
                            + str(types_of_calculations.get(intro_question)[4]) + " " + str(second_number))