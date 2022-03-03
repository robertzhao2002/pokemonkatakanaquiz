# Pokémon Katakana Quiz #

## About ##

This project was built using the BeautifulSoup4 Python library. It was used to retrieve the most recent Pokémon name, Pokédex number, and Katakana Name. The purpose of this project is to use Pokémon names (which are all in Japanese Katakana) to practice reading and recognizing Japanese Katakana characters. For implementation details, check `__init.py__` in the `QuizBuilder` module.

## Quiz Commands ##

### Single Random Pokémon ###

To obtain a single random Pokémon, run this command in the terminal.

``` python quiz.py single ```

### Batch of Random Pokémon ###

To obtain a single random Pokémon, run this command in the terminal.

``` python quiz.py batch ```

### Specific Pokémon ###

To obtain a single random Pokémon, run this command in the terminal.

``` python quiz.py [pokedex-number] ```

## Updating the CSV Files ##

To update the CSV files to the latest Pokémon data, run this command in the terminal. This will scrape all of Bulbapedia and recreate each CSV file. Proceed with caution! This could take a while!

``` python quiz.py update ```

If you would like to update specific generations, please run this command. Be sure to put NO SPACES between the desired generation numbers! The generation numbers do not necessarily have to be in order.

``` python quiz.py update [generation numbers separated by a comma]```

This will update Generations 2, 4, and 6.

``` python quiz.py update 2,6,4```

This or any variant of this **MAY NOT** behave correctly!

``` python quiz.py update 1 2, 2,46```


