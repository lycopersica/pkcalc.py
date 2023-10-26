import pyinputplus as pyip


def get_type_effectiveness(attacking_type, defending_type):
    effectiveness = {
        ("Normal", "Rock"): 0.5,
        ("Normal", "Ghost"): 0,
        ("Normal", "Steel"): 0.5,
        ("Normal", "Normal"): 1,
        ("Normal", "Fire"): 1,
        ("Normal", "Water"): 1,
        ("Normal", "Electric"): 1,
        ("Normal", "Grass"): 1,
        ("Normal", "Ice"): 1,
        ("Normal", "Fighting"): 1,
        ("Normal", "Poison"): 1,
        ("Normal", "Ground"): 1,
        ("Normal", "Flying"): 1,
        ("Normal", "Psychic"): 1,
        ("Normal", "Bug"): 1,
        ("Normal", "Dragon"): 1,
        ("Normal", "Dark"): 1,
        ("Normal", "Fairy"): 1,
        ("Fire", "Fire"): 0.5,
        ("Fire", "Water"): 0.5,
        ("Fire", "Grass"): 2,
        ("Fire", "Ice"): 2,
        ("Fire", "Bug"): 2,
        ("Fire", "Rock"): 0.5,
        ("Fire", "Dragon"): 0.5,
        ("Fire", "Normal"): 1,
        ("Fire", "Electric"): 1,
        ("Fire", "Fighting"): 1,
        ("Fire", "Poison"): 1,
        ("Fire", "Ground"): 1,
        ("Fire", "Flying"): 1,
        ("Fire", "Psychic"): 1,
        ("Fire", "Ghost"): 1,
        ("Fire", "Dark"): 1,
        ("Fire", "Fairy"): 1,
        ("Water", "Fire"): 2,
        ("Water", "Water"): 0.5,
        ("Water", "Grass"): 0.5,
        ("Water", "Ground"): 2,
        ("Water", "Rock"): 2,
        ("Water", "Dragon"): 0.5,
        ("Water", "Normal"): 1,
        ("Water", "Fighting"): 1,
        ("Water", "Flying"): 1,
        ("Water", "Poison"): 1,
        ("Water", "Bug"): 1,
        ("Water", "Ghost"): 1,
        ("Water", "Steel"): 1,
        ("Water", "Electric"): 1,
        ("Water", "Psychic"): 1,
        ("Water", "Ice"): 1,
        ("Water", "Dark"): 1,
        ("Water", "Fairy"): 1,
        ("Electric", "Water"): 2,
        ("Electric", "Electric"): 0.5,
        ("Electric", "Grass"): 0.5,
        ("Electric", "Ground"): 0,
        ("Electric", "Flying"): 2,
        ("Electric", "Dragon"): 0.5,
        ("Electric", "Normal"): 1,
        ("Electric", "Fighting"): 1,
        ("Electric", "Poison"): 1,
        ("Electric", "Rock"): 1,
        ("Electric", "Bug"): 1,
        ("Electric", "Ghost"): 1,
        ("Electric", "Steel"): 1,
        ("Electric", "Fire"): 1,
        ("Electric", "Psychic"): 1,
        ("Electric", "Ice"): 1,
        ("Electric", "Dark"): 1,
        ("Electric", "Fairy"): 1,
        ("Grass", "Fire"): 0.5,
        ("Grass", "Water"): 2,
        ("Grass", "Grass"): 0.5,
        ("Grass", "Poison"): 0.5,
        ("Grass", "Ground"): 2,
        ("Grass", "Flying"): 0.5,
        ("Grass", "Bug"): 0.5,
        ("Grass", "Rock"): 2,
        ("Grass", "Dragon"): 0.5,
        ("Grass", "Normal"): 1,
        ("Grass", "Fighting"): 1,
        ("Grass", "Ghost"): 1,
        ("Grass", "Electric"): 1,
        ("Grass", "Psychic"): 1,
        ("Grass", "Ice"): 1,
        ("Grass", "Dark"): 1,
        ("Grass", "Fairy"): 1,
        ("Grass", "Steel"): 0.5,
        ("Ice", "Fire"): 0.5,
        ("Ice", "Water"): 0.5,
        ("Ice", "Grass"): 2,
        ("Ice", "Ice"): 0.5,
        ("Ice", "Ground"): 2,
        ("Ice", "Flying"): 2,
        ("Ice", "Dragon"): 2,
        ("Ice", "Steel"): 0.5,
        ("Ice", "Normal"): 1,
        ("Ice", "Fighting"): 1,
        ("Ice", "Poison"): 1,
        ("Ice", "Rock"): 1,
        ("Ice", "Bug"): 1,
        ("Ice", "Ghost"): 1,
        ("Ice", "Electric"): 1,
        ("Ice", "Psychic"): 1,
        ("Ice", "Dark"): 1,
        ("Ice", "Fairy"): 1,
        ("Fighting", "Normal"): 2,
        ("Fighting", "Ice"): 2,
        ("Fighting", "Poison"): 0.5,
        ("Fighting", "Flying"): 0.5,
        ("Fighting", "Psychic"): 0.5,
        ("Fighting", "Bug"): 0.5,
        ("Fighting", "Rock"): 2,
        ("Fighting", "Ghost"): 0,
        ("Fighting", "Dark"): 2,
        ("Fighting", "Steel"): 2,
        ("Fighting", "Fairy"): 0.5,
        ("Fighting", "Fighting"): 1,
        ("Fighting", "Ground"): 1,
        ("Fighting", "Fire"): 1,
        ("Fighting", "Water"): 1,
        ("Fighting", "Grass"): 1,
        ("Fighting", "Electric"): 1,
        ("Fighting", "Dragon"): 1,
        ("Poison", "Grass"): 2,
        ("Poison", "Poison"): 0.5,
        ("Poison", "Ground"): 0.5,
        ("Poison", "Rock"): 0.5,
        ("Poison", "Ghost"): 0.5,
        ("Poison", "Steel"): 0,
        ("Poison", "Fairy"): 2,
        ("Poison", "Normal"): 1,
        ("Poison", "Fighting"): 1,
        ("Poison", "Flying"): 1,
        ("Poison", "Bug"): 1,
        ("Poison", "Fire"): 1,
        ("Poison", "Water"): 1,
        ("Poison", "Electric"): 1,
        ("Poison", "Psychic"): 1,
        ("Poison", "Ice"): 1,
        ("Poison", "Dragon"): 1,
        ("Poison", "Dark"): 1,
        ("Ground", "Fire"): 2,
        ("Ground", "Electric"): 2,
        ("Ground", "Grass"): 0.5,
        ("Ground", "Poison"): 2,
        ("Ground", "Flying"): 0,
        ("Ground", "Bug"): 0.5,
        ("Ground", "Rock"): 2,
        ("Ground", "Steel"): 2,
        ("Ground", "Fairy"): 1,
        ("Ground", "Normal"): 1,
        ("Ground", "Fighting"): 1,
        ("Ground", "Ground"): 1,
        ("Ground", "Ghost"): 1,
        ("Ground", "Water"): 1,
        ("Ground", "Psychic"): 1,
        ("Ground", "Ice"): 1,
        ("Ground", "Dragon"): 1,
        ("Ground", "Dark"): 1,
        ("Flying", "Electric"): 0.5,
        ("Flying", "Grass"): 2,
        ("Flying", "Fighting"): 2,
        ("Flying", "Bug"): 2,
        ("Flying", "Rock"): 0.5,
        ("Flying", "Steel"): 0.5,
        ("Flying", "Fairy"): 1,
        ("Flying", "Normal"): 1,
        ("Flying", "Flying"): 1,
        ("Flying", "Poison"): 1,
        ("Flying", "Ground"): 1,
        ("Flying", "Ghost"): 1,
        ("Flying", "Fire"): 1,
        ("Flying", "Water"): 1,
        ("Flying", "Psychic"): 1,
        ("Flying", "Ice"): 1,
        ("Flying", "Dragon"): 1,
        ("Flying", "Dark"): 1,
        ("Psychic", "Fighting"): 2,
        ("Psychic", "Poison"): 2,
        ("Psychic", "Psychic"): 0.5,
        ("Psychic", "Steel"): 0.5,
        ("Psychic", "Dark"): 0,
        ("Psychic", "Normal"): 1,
        ("Psychic", "Flying"): 1,
        ("Psychic", "Ground"): 1,
        ("Psychic", "Rock"): 1,
        ("Psychic", "Bug"): 1,
        ("Psychic", "Ghost"): 1,
        ("Psychic", "Fire"): 1,
        ("Psychic", "Water"): 1,
        ("Psychic", "Grass"): 1,
        ("Psychic", "Electric"): 1,
        ("Psychic", "Ice"): 1,
        ("Psychic", "Dragon"): 1,
        ("Psychic", "Fairy"): 1,
        ("Bug", "Fire"): 0.5,
        ("Bug", "Grass"): 2,
        ("Bug", "Fighting"): 0.5,
        ("Bug", "Poison"): 0.5,
        ("Bug", "Flying"): 0.5,
        ("Bug", "Psychic"): 2,
        ("Bug", "Ghost"): 0.5,
        ("Bug", "Dark"): 2,
        ("Bug", "Steel"): 0.5,
        ("Bug", "Fairy"): 0.5,
        ("Bug", "Normal"): 1,
        ("Bug", "Ground"): 1,
        ("Bug", "Rock"): 1,
        ("Bug", "Bug"): 1,
        ("Bug", "Water"): 1,
        ("Bug", "Electric"): 1,
        ("Bug", "Ice"): 1,
        ("Bug", "Dragon"): 1,
        ("Rock", "Fire"): 2,
        ("Rock", "Ice"): 2,
        ("Rock", "Fighting"): 0.5,
        ("Rock", "Ground"): 0.5,
        ("Rock", "Flying"): 2,
        ("Rock", "Bug"): 2,
        ("Rock", "Steel"): 0.5,
        ("Rock", "Fairy"): 1,
        ("Rock", "Normal"): 1,
        ("Rock", "Poison"): 1,
        ("Rock", "Rock"): 1,
        ("Rock", "Ghost"): 1,
        ("Rock", "Water"): 1,
        ("Rock", "Grass"): 1,
        ("Rock", "Electric"): 1,
        ("Rock", "Psychic"): 1,
        ("Rock", "Dragon"): 1,
        ("Rock", "Dark"): 1,
        ("Ghost", "Normal"): 0,
        ("Ghost", "Psychic"): 2,
        ("Ghost", "Ghost"): 2,
        ("Ghost", "Dark"): 0.5,
        ("Ghost", "Fighting"): 1,
        ("Ghost", "Flying"): 1,
        ("Ghost", "Poison"): 1,
        ("Ghost", "Ground"): 1,
        ("Ghost", "Rock"): 1,
        ("Ghost", "Bug"): 1,
        ("Ghost", "Steel"): 1,
        ("Ghost", "Fire"): 1,
        ("Ghost", "Water"): 1,
        ("Ghost", "Grass"): 1,
        ("Ghost", "Electric"): 1,
        ("Ghost", "Ice"): 1,
        ("Ghost", "Dragon"): 1,
        ("Ghost", "Fairy"): 1,
        ("Dark", "Fighting"): 0.5,
        ("Dark", "Psychic"): 2,
        ("Dark", "Ghost"): 2,
        ("Dark", "Dark"): 0.5,
        ("Dark", "Fairy"): 0.5,
        ("Dark", "Normal"): 1,
        ("Dark", "Flying"): 1,
        ("Dark", "Poison"): 1,
        ("Dark", "Ground"): 1,
        ("Dark", "Rock"): 1,
        ("Dark", "Bug"): 1,
        ("Dark", "Steel"): 1,
        ("Dark", "Fire"): 1,
        ("Dark", "Water"): 1,
        ("Dark", "Grass"): 1,
        ("Dark", "Electric"): 1,
        ("Dark", "Ice"): 1,
        ("Dark", "Dragon"): 1,
        ("Steel", "Rock"): 2,
        ("Steel", "Steel"): 0.5,
        ("Steel", "Fire"): 0.5,
        ("Steel", "Water"): 0.5,
        ("Steel", "Electric"): 0.5,
        ("Steel", "Ice"): 2,
        ("Steel", "Fairy"): 2,
        ("Steel", "Normal"): 1,
        ("Steel", "Fighting"): 1,
        ("Steel", "Flying"): 1,
        ("Steel", "Poison"): 1,
        ("Steel", "Ground"): 1,
        ("Steel", "Bug"): 1,
        ("Steel", "Ghost"): 1,
        ("Steel", "Grass"): 1,
        ("Steel", "Psychic"): 1,
        ("Steel", "Dragon"): 1,
        ("Steel", "Dark"): 1,
        ("Fairy", "Fire"): 0.5,
        ("Fairy", "Fighting"): 2,
        ("Fairy", "Poison"): 0.5,
        ("Fairy", "Dragon"): 2,
        ("Fairy", "Dark"): 2,
        ("Fairy", "Steel"): 0.5,
        ("Fairy", "Normal"): 1,
        ("Fairy", "Flying"): 1,
        ("Fairy", "Ground"): 1,
        ("Fairy", "Rock"): 1,
        ("Fairy", "Bug"): 1,
        ("Fairy", "Ghost"): 1,
        ("Fairy", "Water"): 1,
        ("Fairy", "Grass"): 1,
        ("Fairy", "Electric"): 1,
        ("Fairy", "Psychic"): 1,
        ("Fairy", "Ice"): 1,
        ("Fairy", "Fairy"): 1,
        ("Dragon", "Ice"): 1,
        ("Dragon", "Dragon"): 2,
        ("Dragon", "Fairy"): 0,
        ("Dragon", "Fire"): 1,
        ("Dragon", "Water"): 1,
        ("Dragon", "Grass"): 1,
        ("Dragon", "Electric"): 1,
        ("Dragon", "Normal"): 1,
        ("Dragon", "Fighting"): 1,
        ("Dragon", "Flying"): 1,
        ("Dragon", "Poison"): 1,
        ("Dragon", "Ground"): 1,
        ("Dragon", "Rock"): 1,
        ("Dragon", "Bug"): 1,
        ("Dragon", "Ghost"): 1,
        ("Dragon", "Steel"): 0.5,
        ("Dragon", "Psychic"): 1,
        ("Dragon", "Dark"): 1,
    }

    return effectiveness[(attacking_type, defending_type)]


pokemon_types = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water',
                 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']


def main():
    attacking_type = pyip.inputMenu(prompt="Enter the type of the attacking move: \n", choices=pokemon_types, numbered=False)
    defending_type1 = pyip.inputMenu(prompt="Enter the first type of the defending Pokemon: \n", choices=pokemon_types, numbered=False)
    defending_type2 = pyip.inputMenu(prompt="Enter the second type of the defending Pokemon (if applicable, otherwise "
                                            "leave blank): \n", choices=pokemon_types, numbered=False, blank=True)
    if defending_type2:
        effectiveness = get_type_effectiveness(attacking_type, defending_type1) * get_type_effectiveness(attacking_type,
                                                                                                         defending_type2)
    else:
        effectiveness = get_type_effectiveness(attacking_type, defending_type1)

    if effectiveness == 0:
        print("This attack is not very effective.")
    elif effectiveness == 0.25:
        print("This attack is not very effective.")
    elif effectiveness == 0.5:
        print("This attack is not very effective.")
    elif effectiveness == 1:
        print("This attack is normal effectiveness.")
    elif effectiveness == 2:
        print("This attack is super effective!")
    elif effectiveness == 4:
        print("This attack is EXTRA super effective!")


while True:
    main()
# To do
# create program exit condition
# -- add input validation
# -- error handling
