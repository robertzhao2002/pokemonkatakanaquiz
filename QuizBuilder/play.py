import csv
from random import randint
from QuizBuilder import TOTAL_POKEMON


def single():
    random_generation = str(randint(1, 8))

    try:
        with open('data/gen'+random_generation+'.csv', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))

            random_pokemon_number = randint(1, len(reader)-1)

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
        random_generation = str(randint(1, 8))

        try:
            with open('data/gen'+random_generation+'.csv', encoding='utf-8') as csvfile:
                reader = list(csv.reader(csvfile))

                random_pokemon_number = randint(1, len(reader)-1)

                pokemon_entry = reader[random_pokemon_number]
                pokedex_number, english_name, katakana = pokemon_entry[0:3]

                print("Regional Dex Number:", random_pokemon_number)
                print("PokeDex Number:", pokedex_number)
                print("English Name:", english_name)
                print("Pokemon Katakana:", katakana)

        except:
            print("Invalid File")