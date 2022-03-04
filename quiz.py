import QuizBuilder.play as quiz
from QuizBuilder import arguments

if (len(arguments) == 2 and arguments[1] == 'single') or len(arguments) == 1:
    quiz.single()
elif len(arguments) == 3 and arguments[1] == 'batch':
    quiz.batch(num_pokemon=int(arguments[2]))
elif len(arguments) == 2:
    pokemon_dex_nos = arguments[1].split(",")
    if len(pokemon_dex_nos) > 1:
        for i in range(len(pokemon_dex_nos)):
            pokemon_dex_nos[i] = int(pokemon_dex_nos[i])
        quiz.batch_select(dex_nos=pokemon_dex_nos)
    else:
        quiz.select(dex_no=int(arguments[1]))
else:
    print("Invalid Input")
