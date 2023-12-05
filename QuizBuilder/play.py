import csv
from QuizBuilder import TOTAL_POKEMON
import secrets

POKEMON_GENERATIONS = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649),
    6: (650, 721),
    7: (722, 809),
    8: (810, 905),
    9: (906, 1017),
}


def determine_generation(dex_no):
    for generation in POKEMON_GENERATIONS:
        lower, upper = POKEMON_GENERATIONS[generation]
        if dex_no >= lower and dex_no <= upper:
            return generation


def single():
    random_generation = str(secrets.SystemRandom().randint(1, 8))

    try:
        with open("data/gen" + random_generation + ".csv", encoding="utf-8") as csvfile:
            reader = list(csv.reader(csvfile))

            random_pokemon_number = secrets.SystemRandom().randint(1, len(reader) - 1)

            pokemon_entry = reader[random_pokemon_number]
            pokedex_number, english_name, katakana = pokemon_entry[0:3]

            print("Regional Dex Number:", random_pokemon_number)
            print("PokeDex Number:", pokedex_number)
            print("English Name:", english_name)
            print("Pokemon Katakana:", katakana)

    except:
        print("Invalid File")


def batch(num_pokemon):
    assert num_pokemon > 0 and num_pokemon <= TOTAL_POKEMON

    for i in range(num_pokemon):
        random_generation = str(secrets.SystemRandom().randint(1, 8))

        try:
            with open(
                "data/gen" + random_generation + ".csv", encoding="utf-8"
            ) as csvfile:
                reader = list(csv.reader(csvfile))

                random_pokemon_number = secrets.SystemRandom().randint(1, len(reader) - 1)

                pokemon_entry = reader[random_pokemon_number]
                pokedex_number, english_name, katakana = pokemon_entry[0:3]

                print("Regional Dex Number:", random_pokemon_number)
                print("PokeDex Number:", pokedex_number)
                print("English Name:", english_name)
                print("Pokemon Katakana:", katakana)

        except:
            print("Invalid File")


def select(dex_no):
    generation = determine_generation(dex_no=dex_no)
    regional_dex_number = dex_no - POKEMON_GENERATIONS[generation][0] + 1

    with open("data/gen" + str(generation) + ".csv", encoding="utf-8") as csvfile:
        reader = list(csv.reader(csvfile))

        pokemon_entry = reader[regional_dex_number]
        pokedex_number, english_name, katakana = pokemon_entry[0:3]

        print("Regional Dex Number:", regional_dex_number)
        print("PokeDex Number:", pokedex_number)
        print("English Name:", english_name)
        print("Pokemon Katakana:", katakana)


def batch_select(dex_nos):
    for dex_no in dex_nos:
        select(dex_no=dex_no)
