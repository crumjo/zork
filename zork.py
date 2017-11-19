#! /usr/bin/env python3

from observable import Observable
from observer import Observer
import random
import sys


class House(Observable):
    def update(self, *args, **kwargs):
        pass

class Monster(Observer):
    name = ""
    attack = -1
    health = -1

    def m_attack(self, player):
        player.hp - self.attack


class Person(Monster):
    name = "Person"
    attack = -1
    health = 0


class Zombie(Monster):
    name = "Zombie"
    attack = random.randint(0, 10)
    health = random.randint(50, 100)


class Vampire(Monster):
    name = "Vampire"
    attack = random.randint(10, 20)
    health = random.randint(100, 200)


class Ghoul(Monster):
    name = "Ghoul"
    attack = random.randint(15, 30)
    health = random.randint(40, 80)


class Werewolf(Monster):
    name = "Werewolf"
    attack = random.randint(0, 40)
    health = 200


class Weapon(object):
    name = ""
    attack_mod = 1.0
    uses = 1

    def update_use(self):
        self.uses = self.uses - 1


class HersheyKiss(Weapon):
    name = "Hershey Kiss"
    attack_mod = 1.0
    uses = sys.maxsize


class SourStraws(Weapon):
    name = "Sour Straws"
    attack_mod = random.uniform(1.0, 1.75)
    uses = 2


class ChocolateBars(Weapon):
    name = "Chocolate Bars"
    attack_mod = random.uniform(2.0, 2.4)
    uses = 4


class NerdBombs(Weapon):
    name = "Nerd Bombs"
    attack_mod = random.uniform(3.5, 5.0)
    uses = 1


class Player(object):
    hp = random.randint(100, 125)
    attack = random.randint(10, 20)
    weapon_list = []

    for i in range(0, 10):
        rand = random.randint(0, 3)

        if rand == 0:
            hersheyKiss = HersheyKiss()
            weapon_list.append(hersheyKiss)

        if rand == 1:
            sourStraws = SourStraws()
            weapon_list.append(sourStraws)

        if rand == 2:
            chocolateBars = ChocolateBars()
            weapon_list.append(chocolateBars)

        if rand == 3:
            nerdBombs = NerdBombs()
            weapon_list.append(nerdBombs)

    def p_attack(self, monster, weapon):
        monster.health - (weapon.attack_mod * self.attack)
        monster.update()


class Neighborhood(object):
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for x in range(size)] for y in range(size)]

    def fill(self):
        for house in range(0, (self.size * self.size)):
            for x in range(0, self.size):
                for y in range(0, self.size):

                    house = House()
                    for i in range(0, 10):
                        rand = random.randint(0, 4)
                        if rand == 0:
                            person = Person()
                            house.add_observer(person)
                            person.update()
                            print(person.name, person.attack, person.health)

                        if rand == 1:
                            zombie = Zombie()
                            house.add_observer(zombie)
                            zombie.update()

                        if rand == 2:
                            vampire = Vampire()
                            house.add_observer(vampire)
                            vampire.update()

                        if rand == 3:
                            ghoul = Ghoul()
                            house.add_observer(ghoul)
                            ghoul.update()

                        if rand == 4:
                            werewolf = Werewolf()
                            house.add_observer(werewolf)
                            werewolf.update()

                    self.grid[x][y] = house


class Game(object):

    def __init__(self, size):
        self.size = size
        self.p = Player()
        self.nh = Neighborhood(size)
        self.nh.fill()
        self.x_pos = 0
        self.y_pos = 0
        self.curr = self.nh.grid[self.x_pos][self.y_pos]

    # Check if it is valid move first.
    def go(self, direct):

        if direct == "north":
            temp = self.y_pos
            if (temp + 1) > (self.size - 1):
                print("No houses to the north.")
            else:
                self.y_pos = self.y_pos + 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]
                print("Direction: " + direct)

        if direct == "south":
            temp = self.y_pos
            if (temp - 1) < 0:
                print("No houses to the south.")
            else:
                self.y_pos = self.y_pos - 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]
                print("Direction: " + direct)

        if direct == "east":
            temp = self.x_pos
            if (temp + 1) > (self.size - 1):
                print("No houses to the east.")
            else:
                self.x_pos = self.x_pos + 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]
                print("Direction: " + direct)

        if direct == "west":
            temp = self.x_pos
            if (temp - 1) < 0:
                print("No houses to the west.")
            else:
                self.x_pos = self.x_pos - 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]
                print("Direction: " + direct)

    def attack_p(self, weapon):
        # Attack the player
        pass

    def attack_m(self):
        # Attack the monsters
        pass


if __name__ == '__main__':
    game = Game(4)
    print("Welcome to Zork!")

    while game.p.hp != 0:
        direction = input("Enter direction: ")
        game.go(direction)

        # TO DO:

        # List all monsters in home here. Has to somehow show all observables for this home.
        print("Monsters in house at position: " + str(game.x_pos) + ", " + str(game.y_pos))
        for x in game.curr.observers:
            print(x.name)

        # print(game.curr.observers)

        # Attack monsters here. Remove monster observables if their health <= 0

        # Now monsters attack player before player can attack again.

        # Rinse and repeat until only humans or left or player leaves house.
