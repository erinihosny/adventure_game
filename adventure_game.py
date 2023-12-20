import time
import random
items = []
evil = random.choice(["pirate", "wicked fairie", "troll", "gorgon", "dragon"])


def adventure_game():
    field()


def print_sleep(string):
    print(string)
    time.sleep(2)


def field():
    print_sleep("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_sleep(f"Rumor has it that a {evil} is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_sleep("In front of you is a house.")
    print_sleep("To your right is a dark cave.")
    print_sleep("In your hand you hold your trusty "
                "(but not very effective) dagger.")
    options()


def options():
        print_sleep("Enter 1 to knock on the door of the house.")
        print_sleep("Enter 2 to peer into the cave.")
        print_sleep("What would you like to do?")
        house_or_cave()


def house_or_cave():
    choice = input("(Please enter 1 or 2.)")
    if choice == "2":
        cave()
    elif choice == "1":
        house()
    else:
        house_or_cave()


def cave():
    print_sleep("You peer cautiously into the cave.")
    if "sword" in items:
        print_sleep("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
    else:
        print_sleep("It turns out to be only a very small cave.")
        print_sleep("Your eye catches a glint of metal behind a rock.")
        print_sleep("You have found the magical Sword of Ogoroth!")
        print_sleep("You discard your silly old dagger"
                    " and take the sword with you.")
        items.append("sword")
    print_sleep("You walk back out to the field.")
    options()


def house():
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock "
                f"when the door opens and out steps a {evil}.")
    print_sleep(f"Eep! This is the {evil}'s house!")
    print_sleep(f"The {evil} attacks you!")
    if "sword" not in items:
        print_sleep("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    run_or_fight()


def run_or_fight():
    choice2 = input("Would you like to (1) fight or (2) run away?")
    if choice2 == "2":
        print_sleep("You run back into the field. Luckily,"
                    " you don't seem to have been followed.")
        options()
    elif choice2 == "1":
        if "sword" in items:
            print_sleep(f"As the {evil} moves to attack,"
                        " you unsheath your new sword.")
            print_sleep("The Sword of Ogoroth shines brightly in your hand"
                        " as you brace yourself for the attack.")
            print_sleep(f"But the {evil} takes one look at your shiny new toy"
                        " and runs away!")
            print_sleep(f"You have rid the town of the {evil}."
                        " You are victorious!")
            restart()
        else:
            print_sleep("You do your best...")
            print_sleep(f"but your dagger is no match for the {evil}.")
            print_sleep("You have been defeated!")
        restart()
    else:
        run_or_fight()


def restart():
    again = input("Would you like to play again? (y/n)")
    items.clear()
    if again == "y":
        print_sleep("Excellent! Restarting the game ...")
        adventure_game()
    elif again == "n":
        print_sleep("Thanks for playing! See you next time.")
    else:
        restart()


adventure_game()
