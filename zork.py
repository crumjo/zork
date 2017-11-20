#! /usr/bin/env python3

# TO DO:
# 1. Add getters and setters for proper OO encapsulation.

from observable import Observable
from observer import Observer
import random
import sys


class House(Observable):
    def update(self, *args, **kwargs):
        pass


class Monster(Observer):

    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def m_attack(self, player):
        player.hp = player.hp - self.attack

    def set_name(self, name):
        self.name = name

    def set_attack(self, attack):
        self.attack = attack

    def set_health(self, health):
        self.health = health


class Person(Monster):

    def __init__(self):
        self.name = "Person"
        self.attack = -1
        self.health = 100


class Zombie(Monster):

    def __init__(self, attack, health):
        self.name = "Zombie"
        self.attack = attack
        self.health = health


class Vampire(Monster):

    def __init__(self, attack, health):
        self.name = "Vampire"
        self.attack = attack
        self.health = health


class Ghoul(Monster):

    def __init__(self, attack, health):
        self.name = "Ghoul"
        self.attack = attack
        self.health = health


class Werewolf(Monster):

    def __init__(self, attack):
        self.name = "Werewolf"
        self.health = 200
        self.attack = attack


class Weapon(object):

    name = ""
    attack_mod = 1.0
    uses = 1

    def get_name(self):
        return self.name

    def get_attack_mod(self):
        return self.attack_mod

    def get_uses(self):
        return self.uses

    def set_name(self, name):
        self.name = name

    def set_attack_mod(self, attack_mod):
        self.attack_mod = attack_mod

    def set_uses(self, uses):
        self.uses = uses

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

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.attack

    def get_weapon_list(self):
        return self.weapon_list

    def final_attack(self, x1, x2):
        return x1 * x2

    def p_attack(self, p_monster, p_weapon):
        if p_weapon.get_name() == "hershey kiss":
            p_monster.set_health(p_monster.get_health() -
                                 p_weapon.get_attack_mod() *
                                 self.attack)

            monster.update()

        elif p_weapon.get_name() == "sour straw":
            if p_monster.get_name() == "Zombie":
                p_monster.set_health(p_monster.get_health() -
                                     2 *
                                     (p_weapon.get_attack_mod() *
                                      self.attack))

                monster.update()

            elif p_monster.get_name() == "Werewolf":
                pass

            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                monster.update()

        elif p_weapon.get_name() == "chocolate bar":
            if p_monster.get_name() == "Vampire" or p_monster.get_name() == "Werewolf":
                pass
            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                monster.update()
        else:
            if p_monster.get_name() == "Ghoul":
                p_monster.set_health(p_monster.get_health() -
                                     5 *
                                     (p_weapon.get_attack_mod() *
                                      self.attack))
                monster.update()
            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                monster.update()
                
    def weapon_update(self, weapon):
        if w.get_uses() == 0:
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
                            z_attack = random.randint(0, 10)
                            z_health = random.randint(50.0, 100.0)
                            zombie = Zombie(z_attack, z_health)
                            house.add_observer(zombie)
                            zombie.update()

                        if rand == 2:
                            v_attack = random.randint(10, 20)
                            v_health = random.randint(100.0, 200.0)
                            vampire = Vampire(v_attack, v_health)
                            house.add_observer(vampire)
                            vampire.update()

                        if rand == 3:
                            g_attack = random.randint(15, 30)
                            g_health = random.randint(40.0, 80.0)
                            ghoul = Ghoul(g_attack, g_health)
                            house.add_observer(ghoul)
                            ghoul.update()

                        if rand == 4:
                            w_attack = random.randint(0, 40)
                            werewolf = Werewolf(w_attack)
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
        if g_monster.get_name() != "Person":
            self.p.p_attack(g_monster, g_weapon)

    def humanize(self, h_monster):
        self.curr.remove_observer(h_monster)
        person = Person()
        self.curr.add_observer(person)
        
    def print_inv(self):
        for item in self.p.get_weapon_list():
            if item.get_name() == "hershey kiss":
                print(item.get_name())
            else:
                print(item.get_name(), item.get_uses())

    def check_won(self, nh):
        for x in range(0, nh.size):
            for y in range(0, nh.size):
                tmp = nh.grid[x][y]
                for m in tmp.observers:
                    if m.name != "Person":
                        return 0
                    else:
                        return 1


if __name__ == '__main__':

    if len(sys.argv) == 2:
        size = int(sys.argv[1])
    else:
        print("Provide a single argument for the size of the grid.\n"
              "Example: ./zork.py 4     creates a 4x4 grid.")
        sys.exit(0)


    # Take command line argument for size.
    game = Game(size)
    print("Welcome to Zork!")

    # while game.p.hp > 0:
    while 1:

        if game.check_won(game.nh) == 1:
                print("All monsters transformed back into humans! You win!")
                sys.exit(0)

        print("\nEnter Command (Go, Attack, Stats, Inv, Help, Exit): ")
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
                print(x.get_name(), "%.2f" % x.get_health())

        elif command == "attack":

            print ("Enter a valid weapon (Hershey Kiss, Chocolate Bar, Sour Straw, Nerd Bomb): ")
            weapon = str.lower(input())

            tmp = Weapon()
            weapon_available = False
            for monster in game.curr.observers:
                for w in game.p.weapon_list:
                    if weapon == w.get_name():
                        weapon_available = True
                        game.g_attack(monster, w)

                        # This makes it so it only uses top weapon w/ matching name
                        tmp = w
                        break

            if weapon_available is True:

                tmp.update_use()
                if tmp.get_uses() == 0:
                    game.p.weapon_update(tmp)

                for monster in game.curr.observers:
                    if monster.get_health() <= 0:
                        game.humanize(monster)

                # Now monsters attack player before player can attack again.
                for monster in game.curr.observers:
                    # This might need to be made as a game function
                    monster.m_attack(game.p)

                print("\n____Player Health____")
                print(game.p.get_hp())

                print("\n____Monster Health____")
                for x in game.curr.observers:
                    print(x.get_name(), "%.2f" % x.get_health())

                
            else:
                print("\n'" + weapon + "' is not in your inventory.")
                
        # Prints player and monsters health
        elif command == "stats":
            print("\n____Player Health____")
            print(game.p.get_hp())
            print("\n____Monster Health____")
            for m in game.curr.observers:
                print(m.get_name(), "%.2f" % m.get_health())

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
