import random
from flask import Flask
from flask.json import jsonify
app = Flask(__name__)

@app.route('/')
# def mexico_rules_hitman(disguises, kill_methods, wild_cards, num_players):
#     if num_players > len(wild_cards):
#         print "Wild card list too small for number of players."
#         return
#     for n in range(0, num_players):
#         for i in range(0, 2):
#             disguise_idx = random.randint(0, len(disguises) - 1)
#             disguise = disguises[disguise_idx]
#             disguises.pop(disguise_idx)
#
#             kill_method_idx = random.randint(0, len(kill_methods) - 1)
#             kill_method = kill_methods[kill_method_idx]
#             kill_methods.pop(kill_method_idx)
#
#             print "Player %s ==> Target %s: Disguise: %s | Kill method: %s" % (n+1, i+1, disguise, kill_method)
#             return n+1, i+1, disguise, kill_method

def mexico_rules_hitman():
    disguises = ['Crew', 'Helmut Kruger', 'Security guard', 'The Sheik', 'Stylist', 'Chef', 'Kitchen staff']
    kill_methods = ['Fireaxe', 'Set off explosive in catwalk room', 'Environmental', 'Sword', 'Fire extinguisher', 'Proximity mine', 'Gun']
    wild_cards = ['One save scum', 'Any starting location']
    num_players = 2

    result = []

    if num_players > len(wild_cards):
        print "Wild card list too small for number of players."
        return
    for n in range(0, num_players):
        for i in range(0, 2):
            disguise_idx = random.randint(0, len(disguises) - 1)
            disguise = disguises[disguise_idx]
            disguises.pop(disguise_idx)

            kill_method_idx = random.randint(0, len(kill_methods) - 1)
            kill_method = kill_methods[kill_method_idx]
            kill_methods.pop(kill_method_idx)

            result.append([n+1, i+1, disguise, kill_method])

            # return "Player %s ==> Target %s: Disguise: %s | Kill method: %s" % (n+1, i+1, disguise, kill_method)
            # return n+1, i+1, disguise, kill_method
    return sum(result, [])




mexico_rules_hitman()
