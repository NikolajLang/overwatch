#! python3
# random_overwatch.py - pick a random hero, gamemode, role, show info about a hero or play a quiz (singleplayer and multiplayer) among other things

import json
import requests
import random
import os
import platform

heroes_tank = ['D.Va', 'Orisa', 'Reinhardt', 'Roadhog', 'Sigma', 'Winston', 'Wrecking Ball', 'Zarya']
heroes_dps = ['Ashe', 'Bastion', 'Doomfist', 'Genji', 'Hanzo', 'Junkrat', 'Mccree', 'Mei', 'Pharah', 'Reaper', 'Soldier: 76', 'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker']
heroes_support = ['Ana', 'Baptiste', 'Brigitte', 'Lúcio', 'Mercy', 'Moira', 'Zenyatta']
heroes_all = heroes_tank + heroes_dps + heroes_support

gamemodes_arcade = ['1V1 Mystery Duel', '1V1 Limited Duel', '3V3 Elimination', '6V6 Elimination', '3V3 Lockout Elimination', '6V6 Lockout Elimination', '6V6 Mystery Heroes', '6V6 No limits', '6V6 Total Mayhem', '6V6 Low Gravity', '6V6 Capture The Flag', '8P Deathmatch', '4V4 Team Deathmatch', '8P Mystery Deathmatch', '8P Château Deathmatch', '8P Petra Deathmatch', '8P Mirrored Deathmatch', '6V6 Quick Play Classic']
gamemodes_normal = ['Quick Play Role Queue', 'Competitive']
gamemodes_all = gamemodes_arcade + gamemodes_normal

role_all = ['Tank', 'Damage', 'Support']

# loads or gets data about heroes
try:
    # loads/reads hero json file
    with open('hero_info_overwatch.json', encoding='utf-8') as f:
        info_json = f.read()
    # saves data from hero json file to a variable
    heroes_info = json.loads(info_json)
except:
    # if hero json file not found, get hero json data from GitHub, create a new hero json file and dump hero json data in the new file, then load the hero json data in a variable 
    print('Getting info about heroes data from GitHub...')
    get_hero_json = requests.get('https://raw.github.com/Crinibus/overwatch/master/hero_info_overwatch.json') # get hero json file from GitHub
    json_hero_data = json.loads(get_hero_json.text) # load hero json from string to dictionary
    print('Creating file with hero data...')
    json_hero_file = open('hero_info_overwatch.json', 'w') # create new hero json file
    json_hero_file.write(json.dumps(json_hero_data, indent=4, sort_keys=True)) # dump the hero json data in the new file and make it more readable
    print('Done creating file\n')
    # loads/reads hero json file
    with open('hero_info_overwatch.json', encoding='utf-8') as f:
        info_json = f.read()
    # saves data from hero json file to a variable
    heroes_info = json.loads(info_json)

# loads or gets data about quiz
try:
    # loads/reads quiz json file
    with open('quiz_overwatch.json', encoding='utf-8') as g:
        quiz_json = g.read()
    # saves data from quiz json file to a variable
    quiz_quistions = json.loads(quiz_json)
except:
    # if quiz json file not found, get quiz json data from GitHub, create a new quiz json file and dump quiz json data in the new file, then load the quiz json data in a variable
    print('Getting quiz data from GitHub...')
    get_quiz_json = requests.get('https://raw,github.com/Crinibus/overwatch/master/quiz_overwatch.json') # get quiz json file from GitHub
    json_quiz_data = json.loads(get_quiz_json) # load quiz json from to dictionary
    print('Creating file with quiz data...')
    json_quiz_file = open('quiz_overwatch.json', 'w') # create new quiz json file
    json_quiz_file.write(json.dumps(json_quiz_data, indent=4, sort_keys=True)) # dump the quiz json data in the new file and make it more readable
    print('Done creating file\n')
    # loads/reads quiz json file
    with open('quiz_overwatch.json', encoding='utf-8') as g:
        quiz_json = g.read()
    # saves data from quiz json file to a variable
    quiz_quistions = json.loads(quiz_json)

def hero_picker(role): # returns a random hero depending on what "role" is equal to
    if role.lower() in ('all', 'a'):
        return random.choice(heroes_all)
    elif role.lower() in ('tank', 't'):
        return random.choice(heroes_tank)
    elif role.lower() in ('dps', 'damage', 'd'):
        return random.choice(heroes_dps)
    elif role.lower() in ('support', 'healer', 's'):
        return random.choice(heroes_support)
    else:
        return 'Please select a role'

def gamemode_picker(mode): # returns a random gamemode depending on what "mode" is equal to
    if mode.lower() in ('all'):
        return random.choice(gamemodes_all)
    elif mode.lower() in ('arcade'):
        return random.choice(gamemodes_arcade)
    elif mode.lower() in ('normal'):
        return random.choice(gamemodes_normal)
    else:
        return 'Please select a gamemode'

def role_picker(): # returns a random role
    return random.choice(role_all)

def get_hero_info(hero): # prints info about a hero on multiple lines
    hero = hero.lower()
    if hero in heroes_info:
        print('\nInfo about {0}:'.format(hero.upper()))
        print('Name: {0}'.format(heroes_info[hero]['name']))
        if not hero.lower() == 'orisa':
            print('Age: {0} years'.format(heroes_info[hero]['age']))
        else:
            print('Age: {0}'.format(heroes_info[hero]['age']))
        if not heroes_info[hero]['height'] == 'Unknown':
            print('Height: {0} meters'.format(heroes_info[hero]['height']))
        else:
            print('Height: {0}'.format(heroes_info[hero]['height']))
        print('Nationality: {0}'.format(heroes_info[hero]['nationality']))
        print('Occupation: {0}'.format(heroes_info[hero]['occupation']))
        print('Affiliation: {0}\n'.format(heroes_info[hero]['affiliation']))
    else:
        get_hero_info(input('Choose again: '))

def help(): # prints what commands the user can use with some explanation
    print('\nhero: choose a role and the program picks a random hero inside that role')
    print('gamemode: choose a category and the program picks a random gamemode inside that category')
    print('role: the program returns a random role, e.g. "tank"')
    print('info: choose a hero to show information about')
    print('height: prints the height of each hero')
    print('age: prints the age of each hero')
    print('quiz: choose how many players you are and how many rounds you want to play. Try to answer the questions and see how many you can get correct')
    print('help: explains what you can with this program\n')

def heroes_height(): # prints the height of each hero
    print()
    for hero in heroes_info:
        if not heroes_info[hero]['height'] == 'Unknown':
            print('Height of {0}{1} \t{2} meters'.format(hero.upper(), " "*5, heroes_info[hero]['height']).expandtabs(10))
        else:
            if hero in ('ana', 'mei', 'moira', 'orisa', 'sombra'): # add extra spaces depending on the hero
                print('Height of {0}{1} \tUnknown'.format(hero.upper(), " "*7).expandtabs(10))
            else:
                print('Height of {0}{1} \tUnknown'.format(hero.upper(), " "*1).expandtabs(10))
    print()

def heroes_age(): # prints the age of each hero
    print()
    for hero in heroes_info:
        if not hero == 'orisa': # add extra spaces depending on the hero
            if hero in ('ana', 'ashe', 'd.va', 'genji', 'hanzo', 'lúcio', 'mccree', 'mei', 'mercy', 'moira', 'pharah', 'reaper', 'sigma', 'sombra', 'tracer', 'zarya'):
                print('Age of {0}{1} \t{2} years'.format(hero.upper(), " "*10, heroes_info[hero]['age']).expandtabs(10))
            else:
                print('Age of {0}{1} \t{2} years'.format(hero.upper(), " "*5, heroes_info[hero]['age']).expandtabs(10))
        else:
            print('Age of {0}{1} \t{2}'.format(hero.upper(), " "*7, heroes_info[hero]['age']).expandtabs(10))
    print()

def quiz_singleplayer(num_rounds): # quiz with {num_rounds} rounds for 1 player
    print(f'\nStarting quiz with {num_rounds} rounds')
    points = 0
    questions_shown = []
    for i in range(1, num_rounds + 1):
        tries = 0
        print(f'Round {i}')
        rnd_category = random.choice(list(quiz_quistions['what_hero'])) # TODO: 'what_hero' should be changed so it's a random category
        print(f'Category: {rnd_category}')
        rnd_num = random.randint(1,31)
        while rnd_num in questions_shown:
            rnd_num = random.randint(1,31) # find a new random number if it's already in questions_shown
        questions_shown.append(rnd_num)
        print(quiz_quistions['what_hero'][f'question{rnd_num}']['question']) # TODO: 'what_hero' should be changed so it's the random category
        while tries < 3:
            answer_input = input('Answer: ')
            if answer_input.lower() == quiz_quistions['what_hero'][f'question{rnd_num}']['answer']: # TODO: 'what_hero' should be changed so it's the random category
                print('You answered correct\n')
                points += 1
                break
            elif answer_input.lower() == '':
                print('Try again')
            else:
                if tries >= 0 and tries < 2:
                    print('You answered incorrect, try again\n')
                    tries += 1
                else:
                    print('You answeed incorrect, you have no more tries')
                    print('The answer is: {0}\n'.format(quiz_quistions['what_hero'][f'question{rnd_num}']['answer'].capitalize())) # TODO: 'what_hero' should be changed so it's the random category
                    break
    print(f'The quiz is over. You got {points} points\n\n')

def quiz_multiplayer(num_rounds, num_players): # multiplayer quiz with {num_rounds} rounds and {num_players} players, each player have 1 try to answer each question
    os.system(check_platform()) # clear the terminal according to operation system
    print(f'\nStarting multiplayer quiz with {num_rounds} rounds and {num_players} players')
    questions_shown = [] # used to store already shown questions
    players = [] # used to store players
    for i in range(1, num_players + 1):
        name_input = input(f'Enter name for Player {i}: ')
        players.append(Player(name_input))
    for i in range(1, num_rounds + 1):
        rnd_category = random.choice(list(quiz_quistions['what_hero'])) # TODO: 'what_hero' should be changed so it's a random category
        print(f'Category: {rnd_category}')
        rnd_num = random.randint(1,31) # used to pick random question
        while rnd_num in questions_shown:
            rnd_num = random.randint(1,31) # find a new random number if it's already in questions_shown
        questions_shown.append(rnd_num)
        for player in players:
            os.system(check_platform())
            print(f'Round {i}')
            print(f"Question for {player.name}")
            print(quiz_quistions['what_hero'][f'question{rnd_num}']['question']) # TODO: 'what_hero' should be changed so it's the random category
            answer_input = input('Answer: ')
            if answer_input.lower() == quiz_quistions['what_hero'][f'question{rnd_num}']['answer']: # TODO: 'what_hero' should be changed so it's the random category
                player.points += 1
        os.system(check_platform())
        print('Correct answer for round {0} is: {1}\n'.format(i, quiz_quistions['what_hero'][f'question{rnd_num}']['answer'].capitalize())) # TODO: 'what_hero' should be changed so it's the random category
        if i < num_rounds:
            input('Enter to start the next round ')
 
    # TODO: maybe add a option to send a mail with the results of a quiz
    # TODO: make a ranking system and show it when the quiz is over

    print('The quiz is over')
    for player in players:
        print('{0} got {1} points'.format(player.name, player.points))
    print()

class Player: # used in quiz_multiplayer() to create a new player
    def __init__(self, name):
        self.name = name
    points = 0
    tries = 0

def check_platform(): # checks which operating system the user is on and returns the string to clear the terminal
    if platform.system() == 'Windows':
        return 'cls'
    elif platform.system() in ('Linux', 'Darwin'): # Darwin is Mac OS
        return 'clear'

def main(): # start of the program
    while True: # loops the code, so the user can keep selecting
        start_input = input('Choose what to pick (hero, gamemode, role, info, height, age, quiz, help): ').lower()
        if start_input.lower() == 'hero':
            while True:
                role_input = input('Choose a role (all, tank, dps, support): ')
                if role_input == '':
                    break
                if not hero_picker(role_input) == 'Please select a role':
                    print('Picked hero: {0}\n'.format(hero_picker(role_input)))
                else:
                    print('{0}\n'.format(hero_picker(role_input)))
        elif start_input.lower() == 'gamemode':
            while True:
                gamemode_input = input('Choose a category (all, normal, arcade): ')
                if gamemode_input == '':
                    break
                print('Picked gamemode: {0}\n'.format(gamemode_picker(gamemode_input)))
        elif start_input.lower() == 'info':
            while True:
                info_input = input('Choose a hero: ')
                if info_input == '':
                    break
                get_hero_info(info_input)
        elif start_input.lower() == 'role':
            print('Picked role: {}\n'.format(role_picker()))
        elif start_input.lower() == 'help':
            help()
        elif start_input.lower() == 'height':
            heroes_height()
        elif start_input.lower() == 'age':
            heroes_age()
        elif start_input.lower() == 'quiz':
            try:
                num_players = int(input('Enter number of players: '))
            except ValueError:
                num_players = int(input('Please enter an integer number of players: '))
            try:
                quiz_num = int(input('Enter number of rounds: '))
            except ValueError:
                quiz_num = int(input('Please enter an integer number of rounds: '))
            if num_players == 1:
                quiz_singleplayer(quiz_num)
            elif num_players > 1:
                quiz_multiplayer(quiz_num, num_players)
            else:
                print('Please enter an integer above 1')
        elif start_input.lower() not in ('hero', 'gamemode', 'role', 'info', 'help', 'height', 'age', 'quiz'):
            print('Try again\n')

try:
    main()
except KeyboardInterrupt:
    print('\nProgram closed by user')
except NameError: 
    # # try to load the hero and quiz json files again
    # print('Tring to load json files again...')
    # # loads/reads json file
    # with open('hero_info_overwatch.json', encoding='utf-8') as f:
    #     info_json = f.read()
    # # saves data from json file to a variable
    # heroes_info = json.loads(info_json)

    # # loads/reads quiz json file
    # with open('quiz_overwatch.json', encoding='utf-8') as g:
    #     quiz_json = g.read()
    # # saves data from quiz json file to a variable
    # quiz_quistions = json.loads(quiz_json)
    
    print('A NameError occurred')
    main()