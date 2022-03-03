from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
from torch import rand
from random import randint

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names"

POKEMON_NUMBER = 722
# randint(1, 905)
# print(POKEMON_NUMBER)

POKEMON_GENERATIONS = {
    1: (1, 151),
    2: (152, 251),
    3: (252, 386),
    4: (387, 493),
    5: (494, 649),
    6: (650, 721),
    7: (722, 809),
    8: (810, 905)
}  # A dictionary representing each Generation of Pokemon and the range of Pokedex numbers that correspond to it


def generation(pokemon_number):
    '''
    Returns the Generation of a Pokemon whose Pokedex number is pokemon_number
    '''
    for generation_number in POKEMON_GENERATIONS:
        lower_bound, upper_bound = POKEMON_GENERATIONS[generation_number]
        if pokemon_number >= lower_bound and pokemon_number <= upper_bound:
            return generation_number


GENERATION_NUMBER = generation(POKEMON_NUMBER)

generation_lower_bound = POKEMON_GENERATIONS[GENERATION_NUMBER][0]
generation_upper_bound = POKEMON_GENERATIONS[GENERATION_NUMBER][1]

resp = requests.get(URL, headers=headers)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = soup.find_all('table', {'class': 'roundy'})[
        GENERATION_NUMBER-1].findAll('tr', {'style': "background:#FFF"})

    for pokemon_number, entry in zip(range(generation_lower_bound, generation_upper_bound+1), results):
        if pokemon_number == POKEMON_NUMBER:
            pokemon_entry = entry.find_all('td')
            pokemon_english = pokemon_entry[2].get_text().strip()
            pokemon_katakana = pokemon_entry[3].get_text().strip()
            pokemon_romaji = pokemon_entry[4].get_text().strip()

            print(pokemon_katakana + pokemon_romaji, pokemon_english)
