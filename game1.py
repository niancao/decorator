# -*- coding = utf-8 -*-
# @Time : 2023/3/5 16:09
# @Author : caozizhe
# @File : game1.py
# @Software: PyCharm

import time


def display_scene(func):
    def wrapper(*args, **kwargs):
        scene, choices = func(*args, **kwargs)
        print(scene)
        print("What do you want to do?")
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
        choice = input("> ")
        return int(choice) - 1
    return wrapper


@display_scene
def room1(choices):
    scene = "You are in a dark room with two doors. One door leads to the north, the other to the east."
    return (scene, ["Go north", "Go east", "Stay here"])


@display_scene
def room2(choices):
    scene = "You enter a room filled with traps. You see a button on the wall and a door to the west."
    return (scene, ["Press the button", "Go west", "Stay here"])


@display_scene
def room3(choices):
    scene = "You are in a room with a pit in the middle. You see a rope hanging from the ceiling and a door to the east."
    return (scene, ["Climb the rope", "Go east", "Jump over the pit"])


@display_scene
def room4(choices):
    scene = "You enter a room with a large chest in the center. You see a door to the south."
    return (scene, ["Open the chest", "Go south", "Ignore the chest"])


@display_scene
def room5(choices):
    scene = "You find yourself in a room with a giant spider. You see a door to the west."
    return (scene, ["Fight the spider", "Go west", "Hide in a corner"])

def game():
    paly_again = True
    while paly_again:
        position = 1
        print("------   Let's begin   ------")
        print("------     Welcom      ------\n")
        while position != 6:
            if position == 1:
                choice = room1(["Go north", "Go east", "Stay here"])
                if choice == 0:
                    position = 3
                elif choice == 1:
                    position = 4
                elif choice == 2:
                    print("A group of monsters come into the room and attack you.")
                    print("You died, game over.")
                    break

            elif position == 2:
                choice = room2(["Press the button", "Go west", "Stay here"])
                if choice == 0:
                    print("A secret door opens in the wall to the north.")
                    position = 3
                elif choice == 1:
                    print("You try to open the door to the west, back to the first palce")
                    position == 1
                elif choice == 2:
                    print("A group of monsters come into the room and attack you.")
                    print("You died, game over.")
                    break

            elif position == 3:
                choice = room3(["Climb the rope", "Go east", "Jump over the pit"])
                if choice == 0:
                    print("saw a chest")
                    position = 4
                elif choice == 1:
                    print("Found a spider")
                    position = 5
                elif choice == 2:
                    print("Back to the first place")
                    position = 1

            elif position == 4:
                choice = room4(["Open the chest", "Go south", "Ignore the chest"])
                if choice == 0:
                    print("Enter a new place, and found spiders")
                    position = 5
                elif choice == 1:
                    print("Back to the first place")
                    position = 1
                elif choice == 2:

                    position = 3

            elif position == 5:
                choice = room5(["Fight the spider", "Go west", "Hide in a corner"])
                if choice == 0:
                    print("You killed the spider! Congratulations, you win!")
                    break
                elif choice == 1:
                    position = 4
                elif choice == 2:
                    print("The spider found you and killed you. Game over.")
                    break

        choice = input("Do you want to play again? (y/n) > ")
        if choice in "y":
            play_again = True
        else:
            paly_again = False

game()
print("------   Game Finshed !!!   ------")

