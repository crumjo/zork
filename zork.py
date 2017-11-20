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
    health = -1.0

    def m_attack(self, player):
        player.hp = player.hp - self.attack


class Person(Monster):
    name = "Person"
    attack = -1
    health = 100.0


class Zombie(Monster):
    name = "Zombie"
    attack = random.randint(0, 10)
    health = random.randint(50.0, 100.0)


class Vampire(Monster):
    name = "Vampire"
    attack = random.randint(10, 20)
    health = random.randint(100.0, 200.0)


class Ghoul(Monster):
    name = "Ghoul"
    attack = random.randint(15, 30)
    health = random.randint(40.0, 80.0)


class Werewolf(Monster):
    name = "Werewolf"
    attack = random.randint(0, 40)
    health = 200.0


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
    name = "Sour Straw"
    attack_mod = random.uniform(1.0, 1.75)
    uses = 2


class ChocolateBars(Weapon):
    name = "Chocolate Bar"
    attack_mod = random.uniform(2.0, 2.4)
    uses = 4


class NerdBombs(Weapon):
    name = "Nerd Bomb"
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

    def p_attack(self, p_monster, p_weapon):
        p_monster.health = p_monster.health - (p_weapon.attack_mod * self.attack)
        monster.update()

    def weapon_update(self, weapon):
        if w.uses == 0:
            self.weapon_list.remove(weapon)

    
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

    def g_attack(self, g_weapon):
        for g_m in self.curr.observers:

            # FIX ME: This is where it crashes for some reason.
            self.p.attack(g_m, g_weapon)

    # Why are there two attack methods? Which one is used?
    def g_attack(self, g_monster, g_weapon):
        self.p.p_attack(g_monster, g_weapon)

    def humanize(self, h_monster):
        self.curr.remove_observer(h_monster)
        person = Person()
        self.curr.add_observer(person)
        
    def print_inv(self):
        for item in self.p.weapon_list:
            print(item.name, item.uses)


if __name__ == '__main__':
    game = Game(4)
    print("Welcome to Zork!")

    while game.p.hp != 0:
        print("Enter command: Menu, Go, Attack")
        command = str.lower(input())

        if command == "go":
            print("Enter direction: North, South, East, West")
            direction = str.lower(input())
            game.go(direction)

            # Lists all monsters in home.
            print("Monsters in house at position: " + str(game.x_pos) + ", " + str(game.y_pos))
            for x in game.curr.observers:
                print(x.name, x.health)

        if command == "attack":
            # Attack monsters here. Remove monster observables if their health <= 0
            print ("Enter weapon: Hershey Kiss, Chocolate Bar, Sour Straw, Nerd Bomb")
            weapon = input()

            # Never updates  uses
            tmp = Weapon()
            for monster in game.curr.observers:
                for w in game.p.weapon_list:
                    if weapon == w.name:
                        game.g_attack(monster, w)
                        # p_weapon.update_use()
                        # This makes it so it only uses top weapon w/ matching name
                        tmp = w
                        break
            tmp.update_use()
            if tmp.uses == 0:
                game.p.weapon_update(tmp)

            if monster.health <= 0:
                game.humanize(monster)

            print("____Monster Health____")

            for x in game.curr.observers:
                print(x.name, "%.2f" % x.health)

            # Now monsters attack player before player can attack again.
            for monster in game.curr.observers:
                # This might need to be made as a game function
                monster.m_attack(game.p)
            
            print("____Player Health____")
            print(game.p.hp)

        # Rinse and repeat until only humans or left or player leaves house.

        # Menu to get stats,inventory,help or exit game
        if command == "menu":
            print("Enter command: Stats, Inventory, Help, Exit")
            command = str.lower(input())

            # Prints player and monsters health
            if command == "stats":
                print()
                print("____Player Health____")
                print(game.p.hp)
                print()
                print("____Monster Health____")
                for m in game.curr.observers:
                    print(m.name, m.health)
                print()

            if command == "inventory":
                print ("____Player Inventory____")
                game.print_inv()

            if command == "help":
                print("Navigate your neighborhood by typing in the command 'Direction'")
                print("Then type in one of the directions listed to move if able")
                print("To attack all the monsters in a house at once use the command 'Attack'")
                print("Then type in one of the candy weapons you have available")
                print("Type 'Menu' for useful information such as your health and inventory")
                print("Hint some monsters take extra damage from some candy weapons")
                print("Where other monsters are immune to certain weapons!")

            if command == "exit":
                sys.exit(0)
