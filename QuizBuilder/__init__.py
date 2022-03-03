from bs4 import BeautifulSoup
import requests
import csv
import sys

arguments = sys.argv

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names"

TOTAL_POKEMON = 905

if (len(arguments) == 2 or len(arguments) == 3) and arguments[1] == 'update':
    generations_to_update = list(range(1, 9))

    if len(arguments) == 3:
        generations_to_update = arguments[2].split(",")
        for i in range(len(generations_to_update)):
            generations_to_update[i] = int(generations_to_update[i])

    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

        try:
            for generation_number in generations_to_update:
                filename_generation = str(generation_number)
                results = soup.find_all('table', {'class': 'roundy'})[
                    generation_number-1].findAll('tr', {'style': "background:#FFF"})

                with open('data/gen'+filename_generation+'.csv', 'w', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)

                    for row_number, entry in zip(range(len(results)), results):
                        if row_number == 0:
                            writer.writerow(
                                ["pokedex number", "english name", "katakana", "romaji"])

                        pokemon_entry = entry.find_all('td')

                        pokemon_number = pokemon_entry[0].get_text().strip()
                        pokemon_english = pokemon_entry[2].get_text().strip()
                        pokemon_katakana = pokemon_entry[3].get_text().strip()
                        pokemon_romaji = pokemon_entry[4].get_text().strip()

                        fields = [pokemon_number, pokemon_english,
                                  pokemon_katakana, pokemon_romaji]

                        print("Pokemon Number:", pokemon_number)
                        print("English Name:", pokemon_english)
                        print("Katakana:", pokemon_katakana)

                        writer.writerow(fields)
        except:
            print("Error")
