from bs4 import BeautifulSoup
import requests
import csv
import sys

arguments = sys.argv

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Japanese_Pok%C3%A9mon_names"

if len(arguments) == 2 and arguments[1] == 'get':
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")

        try:
            for generation_number in range(8):
                filename_generation = str(generation_number+1)
                results = soup.find_all('table', {'class': 'roundy'})[
                    generation_number].findAll('tr', {'style': "background:#FFF"})

                with open('data/gen'+filename_generation+'.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)

                    for entry in results:
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
