#! /usr/bin/env python3

# TO DO:
# 1. Check for game won. It currently only tells you if you lose.
# 2. Adjust which weapons damage which monsters.
# 3. Monsters of the same type have to have random health.
# 3. ????
# 4. Profit.

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
    health = 100


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
    health = 200


class Weapon(object):
    name = ""
    attack_mod = 1.0
    uses = 1

    def update_use(self):
        self.uses = self.uses - 1


class HersheyKiss(Weapon):
    name = "hershey kiss"
    attack_mod = 1.0
    uses = sys.maxsize


class SourStraws(Weapon):
    name = "sour straw"
    attack_mod = random.uniform(1.0, 1.75)
    uses = 2


class ChocolateBars(Weapon):
    name = "chocolate bar"
    attack_mod = random.uniform(2.0, 2.4)
    uses = 4


class NerdBombs(Weapon):
    name = "nerd bomb"
    attack_mod = random.uniform(3.5, 5.0)
    uses = 1


class Player(object):
    hp = random.randint(100, 125)
    attack = random.randint(10, 20)
    weapon_list = []

    kiss_check = 0
    i = 10
    while i != 0:
        rand = random.randint(0, 3)

        if rand == 0 and kiss_check != 1:
            hersheyKiss = HersheyKiss()
            weapon_list.append(hersheyKiss)
            kiss_check = 1
            i = i - 1

        if rand == 1:
            sourStraws = SourStraws()
            weapon_list.append(sourStraws)
            i = i - 1

        if rand == 2:
            chocolateBars = ChocolateBars()
            weapon_list.append(chocolateBars)
            i = i - 1

        if rand == 3:
            nerdBombs = NerdBombs()
            weapon_list.append(nerdBombs)
            i = i - 1

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
                    rand = random.randint(0, 10)
                    for i in range(0, rand):
                        rand = random.randint(0, 4)
                        if rand == 0:
                            person = Person()
                            house.add_observer(person)
                            person.update()

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
                print("\nNo houses to the north.")
            else:
                self.y_pos = self.y_pos + 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]

        if direct == "south":
            temp = self.y_pos
            if (temp - 1) < 0:
                print("\nNo houses to the south.")
            else:
                self.y_pos = self.y_pos - 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]

        if direct == "east":
            temp = self.x_pos
            if (temp + 1) > (self.size - 1):
                print("\nNo houses to the east.")
            else:
                self.x_pos = self.x_pos + 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]

        if direct == "west":
            temp = self.x_pos
            if (temp - 1) < 0:
                print("\nNo houses to the west.")
            else:
                self.x_pos = self.x_pos - 1
                self.curr = self.nh.grid[self.x_pos][self.y_pos]

    def g_attack(self, g_monster, g_weapon):
        if g_monster.name != "Person":
            self.p.p_attack(g_monster, g_weapon)

    def humanize(self, h_monster):
        self.curr.remove_observer(h_monster)
        person = Person()
        self.curr.add_observer(person)
        
    def print_inv(self):
        for item in self.p.weapon_list:
            if item.name == "hershey kiss":
                print(item.name)
            else:
                print(item.name, item.uses)

if __name__ == '__main__':

    # Take command line argument for size.
    game = Game(4)
    print("Welcome to Zork!")

    #while game.p.hp > 0:
    while 1:
        print("\nEnter Command: Go, Attack, Stats, Inv, Help")
        command = str.lower(input())

        if command == "go":
            print("Enter direction: North, South, East, West")
            direction = str.lower(input())
            game.go(direction)

            # Lists all monsters in home.
            print("\nMonsters in house at current position ("
                  + str(game.x_pos) + ", " + str(game.y_pos) +
                  "): ")
            for x in game.curr.observers:
                print(x.name, x.health)

        elif command == "attack":
            # Attack monsters here. Remove monster observables if their health <= 0
            print ("Enter weapon: Hershey Kiss, Chocolate Bar, Sour Straw, Nerd Bomb")
            weapon = str.lower(input())

            tmp = Weapon()
            weapon_available = False
            for monster in game.curr.observers:
                for w in game.p.weapon_list:
                    if weapon == w.name:
                        weapon_available = True
                        game.g_attack(monster, w)

                        # This makes it so it only uses top weapon w/ matching name
                        tmp = w
                        break
            
            tmp.update_use()
            if tmp.uses == 0:
                game.p.weapon_update(tmp)
            print("here1")
            print(monster.health,monster.name)
            if monster.health <= 0:
                print("here2")
                game.humanize(monster)
            print("here3")
            print("\n____Monster Health____")
                
            if weapon_available is True:
                for x in game.curr.observers:
                    print(x.name, "%.2f" % x.health)

                # Now monsters attack player before player can attack again.
                for monster in game.curr.observers:
                    # This might need to be made as a game function
                    monster.m_attack(game.p)
                    
                print("\n____Player Health____")
                print(game.p.hp)
                
            else:
                print("\n Please enter a valid weapon")
                
        # Prints player and monsters health
        elif command == "stats":
            print("\n____Player Health____")
            print(game.p.hp)
            print("\n____Monster Health____")
            for m in game.curr.observers:
                print(m.name, "%.2f" % m.health)

        elif command == "inv":
            print ("\n____Player Inventory____")
            game.print_inv()

        elif command == "help":
            print("\nGame Objective: Navigate from house to house in a neighborhood\n"
                  "and eliminate all the monsters. Once a monster has been\n"
                  "eliminated, it turns into a person which will give you health.\n")
            print("Commands: ")
            print("- Go: Move one house to the north, south, east, or west.")
            print("- Attack: Attack all the monsters in the house after a weapon\n"
                  "has been chosen.")
            print("- Stats: Display your health and the health of the\n"
                  "monsters in the current house.")
            print ("- Inv: List all the weapons and their uses in your inventory.\n")

        elif command == "exit":
                sys.exit(0)

        else:
            print("\nCommand not recognized.\n")

    print("Game over. You lose.")
