#! /usr/bin/env python3

from observable import Observable
from observer import Observer
import random
import sys


# Halloween Zork game using OO
# @author Patton Finley & Josh Crum
# @Version Nov 2017



# House class that observes the monsters in it, inherates(typo)
# observable class
class House(Observable):
    def update(self, *args, **kwargs):
        pass


# Monster class that defines setters and getters for monsters
# inhereits(typo) from the observer class
class Monster(Observer):

    
    # Constructor class for monsters
    #
    # @param name - string for name of monster
    # @param attack - int for amount of damage monster does
    # @param health - int for amount of health monster has
    
    def __init__(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health

    
    # Getter method that returns the monsters name
    
    def get_name(self):
        return self.name

    
    # Getter method that returns the monsters health

    def get_health(self):
        return self.health

    # Getter method that returns the monsters attack
    
    def get_attack(self):
        return self.attack

    
    # Method that takes in a player and deals monster damage
    # to them
    # @param player an object that takes damage
    
    def m_attack(self, player):
        player.set_hp(player.get_hp() - self.attack)

    # Setter method that sets the monsters name to the inputted
    # name
    # @param string name - string to rename monster

    def set_name(self, name):
        self.name = name


    # Setter method that sets the monsters attack to the inputted
    # attack
    # @param int attack - int to set a monster attack too

    def set_attack(self, attack):
        self.attack = attack

    
    # Setter method that sets the monsters health to the inputted
    # health
    # @param int health - int to set monsters health
    #
    def set_health(self, health):
        self.health = health



# Person class that inherits from monster class and defines
# a monster as a person

class Person(Monster):

    
    # Constructor class for a person
    
    def __init__(self):
        self.name = "Person"
        self.attack = -1
        self.health = 100


# Zombie class that inherits from monster class and
# defines a monsters as a zombie

class Zombie(Monster):


    # Constructor class for Zombies
    # @param attack - int for amount of damage the zombie does
    # @param health - int for amount of health zombie has

    def __init__(self, attack, health):
        self.name = "Zombie"
        self.attack = attack
        self.health = health


# Vampire class that inherits from monster class and
# defines a monsters as a vampire

class Vampire(Monster):

   
    # Constructor class for Vampires
    # @param attack - int for amount of damage the vampire does
    # @param health - int for amount of health vampire has
    
    def __init__(self, attack, health):
        self.name = "Vampire"
        self.attack = attack
        self.health = health


# Ghoul class that inherits from monster class and
# defines a monsters as a ghoul

class Ghoul(Monster):


    # Constructor class for Ghouls
    # @param attack - int for amount of damage the ghoul does
    # @param health - int for amount of health ghoul has

    def __init__(self, attack, health):
        self.name = "Ghoul"
        self.attack = attack
        self.health = health


# Werewolf class that inherits from monster class and
# defines a monsters as a werewolf

class Werewolf(Monster):

    # Constructor class for Werewolfs
    # @param attack - int for amount of damage the Werewolf does
    # @param health - int for amount of health Werewolf has
    
    def __init__(self, attack):
        self.name = "Werewolf"
        self.health = 200
        self.attack = attack


# Weapon class that defines a weapon inheriets form object
class Weapon(object):

    # string for name of the weapon
    name = ""
    # float for attack mod a weapon has
    attack_mod = 1.0
    # int for how many uses you have left on a weapon
    uses = 1

    
    # Getter method that returns the weapons name
    def get_name(self):
        return self.name

    
    # Getter method that returns the weapons attack mod
    def get_attack_mod(self):
        return self.attack_mod

    
    # Getter method that returns the amount of uses a weaopn
    # has left
    
    def get_uses(self):
        return self.uses

   
    # Setter method that sets the weapons name to the inputted
    # name
    # @param string name - string to rename weapon
    
    def set_name(self, name):
        self.name = name

    # Setter method that sets the weapons attack to the inputted
    # int
    # @param int attack_mod - what to set the attack mod to
    
    def set_attack_mod(self, attack_mod):
        self.attack_mod = attack_mod

    # Setter method that sets the weapons number of uses to the
    # inputted amount
    # @param int uses - int for number of uses
    def set_uses(self, uses):
        self.uses = uses

    # Helper method that takes one use off a weapon
    def update_use(self):
        self.uses = self.uses - 1


# Hersheykiss class that inherits from weapon class and
# defines a weapon as a Hershey kiss
class HersheyKiss(Weapon):
    # defines the name of hershey kiss
    name = "hershey kiss"
    # sets attack mod of heshey kiss
    attack_mod = 1.0
    # sets the uses
    uses = sys.maxsize


# SourStraw class that inherits from weapon class and
# defines a weapon as a sour straw
class SourStraws(Weapon):
    # defines the name of sour straws
    name = "sour straw"
    # defines the attack mod randomly between 1.0 and 1.75
    attack_mod = random.uniform(1.0, 1.75)
    # defines uses to 2
    uses = 2

# ChoclateBars class that inherits from weapon class and
# defines a weapon as a chocolate bar
class ChocolateBars(Weapon):
    # defines the name of chocolate bars
    name = "chocolate bar"
    # defines the attack mod randomly between 2.0 and 2.4
    attack_mod = random.uniform(2.0, 2.4)
    # defines uses to 4
    uses = 4


# NerdBombs class that inherits from weapon class and
# defines a weapon as a nerd bomb
class NerdBombs(Weapon):
    # defines the name of nerd bombs
    name = "nerd bomb"
    # defines the attack mod randomly from 3.5 to 5.0
    attack_mod = random.uniform(3.5, 5.0)
    # sets uses to 1
    uses = 1


# Player class that defines a player inherients from an object
class Player(object):
    # randomly sets player health between 250 and 275
    hp = random.randint(250, 275)
    # randomly sets player attack between 10 and 20
    attack = random.randint(10, 20)
    # defines array for inventory
    weapon_list = []

    def set_hp(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp

    def set_attack(self, attack):
        self.attack = attack

    def get_attack(self):
        return self.attack

    def get_weapon_list(self):
        return self.weapon_list

    # int to put in at least 1 hershey kiss
    kiss_check = 0
    # i used to decrement to until inventory is full
    i = 10
    # while loop to fill inventory
    while i != 0:
        # randomly picks what weapon it will be
        rand = random.randint(0, 3)

        # if the random is zero and hershey kisses arent
        # already added then they are added
        if rand == 0 and kiss_check != 1:
            hersheyKiss = HersheyKiss()
            weapon_list.append(hersheyKiss)
            kiss_check = 1
            i = i - 1

        # if the random is one then it adds sourstraws to inventory
        if rand == 1:
            sourStraws = SourStraws()
            weapon_list.append(sourStraws)
            i = i - 1

        # if the random is two then it adds chocolate bars to inventory
        if rand == 2:
            chocolateBars = ChocolateBars()
            weapon_list.append(chocolateBars)
            i = i - 1
        # if the random is three then it adds nerd bombs to inventory
        if rand == 3:
            nerdBombs = NerdBombs()
            weapon_list.append(nerdBombs)
            i = i - 1

    # Getter method that returns the players health(hp)
    def get_hp(self):
        return self.hp
    
    
    # Getter method that returns the players attack
    def get_attack(self):
        return self.attack


    # Getter method that returns the weapons list
    def get_weapon_list(self):
        return self.weapon_list
    
    # Method that attacks a monster and determines the amount
    # of damage to do to them
    def p_attack(self, p_monster, p_weapon):
        # if its a hershy kiss they all take the same amount of
        # damage
        if p_weapon.get_name() == "hershey kiss":
            # calls setter method to change monsters health
            p_monster.set_health(p_monster.get_health() -
                                 p_weapon.get_attack_mod() *
                                 self.attack)
            # updates monster
            monster.update()
        # elif the name is sour straw check to see if its a zombie
        # or werewolf
        elif p_weapon.get_name() == "sour straw":
            # if zombie it takes double damage
            if p_monster.get_name() == "Zombie":
                p_monster.set_health(p_monster.get_health() -
                                     2 *
                                     (p_weapon.get_attack_mod() *
                                      self.attack))
                # update monsters
                monster.update()
            # elif werewolf it takes no damage
            elif p_monster.get_name() == "Werewolf":
                pass
            # all other monsters take normal damage
            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                # update monsters
                monster.update()
        # elif if its a chocolate bar check to see if its a vampire
        # or werewolf
        elif p_weapon.get_name() == "chocolate bar":
            # checks if its a vampire or werewolf and passes if they are
            if p_monster.get_name() == "Vampire" or p_monster.get_name() == "Werewolf":
                pass
            # else deals damage to monster
            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                # update monster
                monster.update()
        # if not any of the other weapons its a candy bomb
        else:
            # checks to see if its a ghoul and deals 5 times damage if so
            if p_monster.get_name() == "Ghoul":
                p_monster.set_health(p_monster.get_health() -
                                     5 *
                                     (p_weapon.get_attack_mod() *
                                      self.attack))
                # updates monster
                monster.update()
            # else deals regular damage
            else:
                p_monster.set_health(p_monster.get_health() -
                                     p_weapon.get_attack_mod() *
                                     self.attack)
                # updates monster
                monster.update()
                

    # Helper method that checks if a weapon is out of uses
    # and removes it if its true
    # @param weapon weapon to check if its passed in
    def weapon_update(self, weapon):
        if w.get_uses() == 0:
            self.weapon_list.remove(weapon)


# Neighborhood class taht defines a neighborhood and fills it
# with houses, inherints from object
class Neighborhood(object):

    # Constructor class for neighborhood
    # param size - int for size of 2d array
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for x in range(size)] for y in range(size)]

    # Getter to return the size of the grid.
    def get_size(self):
        return self.size

    # Getter to return the grid of houses.
    def get_grid(self):
        return self.grid

    # Helper method that fills up the neighbor hood with houses
    # and then fills the houses with monsters
    def fill(self):
        for house in range(0, (self.size * self.size)):
            for x in range(0, self.size):
                for y in range(0, self.size):

                    # defines a house
                    house = House()
                    # randomly decides how full the house is
                    rand = random.randint(0, 10)
                    # randomly picks out a monster and puts it
                    # in the house
                    for i in range(0, rand):

                        # randomly picks a monster
                        rand = random.randint(0, 4)
                        # if rand is 0 it adds a person
                        if rand == 0:
                            person = Person()
                            house.add_observer(person)
                            person.update()

                        # if rand is 1 it adds a zombie
                        if rand == 1:
                            # defines health and attack for zombies
                            z_attack = random.randint(0, 10)
                            z_health = random.randint(50.0, 100.0)
                            # defines zombie
                            zombie = Zombie(z_attack, z_health)
                            # adds zombie to house
                            house.add_observer(zombie)
                            zombie.update()

                        # if rand is 2 it adds a vampire
                        if rand == 2:
                            # defines health and attack for vampire
                            v_attack = random.randint(10, 20)
                            v_health = random.randint(100.0, 200.0)
                            # defines a vampire
                            vampire = Vampire(v_attack, v_health)
                            # adds a vampire to the house
                            house.add_observer(vampire)
                            vampire.update()

                        # if rand is 3 it adds a ghoul
                        if rand == 3:
                            # defines health and attack for ghoul
                            g_attack = random.randint(15, 30)
                            g_health = random.randint(40.0, 80.0)
                            # defines a ghoul
                            ghoul = Ghoul(g_attack, g_health)
                            # adds the ghoul to the house
                            house.add_observer(ghoul)
                            ghoul.update()

                        # if rand is 4 it adds a werewolf
                        if rand == 4:
                            # defines attack for a werewolf
                            w_attack = random.randint(0, 40)
                            # defines a werewolf
                            werewolf = Werewolf(w_attack)
                            # adds a werewolf to the house
                            house.add_observer(werewolf)
                            werewolf.update()
                    # places house in grid
                    self.grid[x][y] = house

                    


# Game class used to build the game
class Game(object):

    # Constructor method that defines everything for the game
    # @param size - size to build the 2d array
    def __init__(self, size):
        # sets size to inputted size
        self.size = size
        # iniatates the player
        self.p = Player()
        # iniatates the neighborhood
        self.nh = Neighborhood(size)
        # fills the neighborhood
        self.nh.fill()
        # places player at spot [0][0]
        self.x_pos = 0
        self.y_pos = 0
        # defines the location of player
        tmp_grid = self.nh.get_grid();
        self.curr = tmp_grid[self.x_pos][self.y_pos]

    # Getter method to return the x position of the house.
    def get_x_pos(self):
        return self.x_pos

    # Getter method to return the y position of the house.
    def get_y_pos(self):
        return self.y_pos

    # Helper method to see if a move is valid and moves
    # the player if able
    # param direct - string on where to go
    def go(self, direct):
        # checks to see if direct is north
        if direct == "north":
            # checks for valid movement
            temp = self.y_pos
            if (temp + 1) > (self.size - 1):
                print("\nNo houses to the north.")
            # moves if able
            else:
                self.y_pos = self.y_pos + 1
                tmp_grid = self.nh.get_grid();
                self.curr = tmp_grid[self.x_pos][self.y_pos]

        # checks to see if direct is south
        if direct == "south":
            # checks for valid move
            temp = self.y_pos
            if (temp - 1) < 0:
                print("\nNo houses to the south.")
            # moves if able
            else:
                self.y_pos = self.y_pos - 1
                tmp_grid = self.nh.get_grid();
                self.curr = tmp_grid[self.x_pos][self.y_pos]

        # checks to see if direct is east
        if direct == "east":
            # checks for valid move
            temp = self.x_pos
            if (temp + 1) > (self.size - 1):
                print("\nNo houses to the east.")
            # moves if able
            else:
                self.x_pos = self.x_pos + 1
                tmp_grid = self.nh.get_grid();
                self.curr = tmp_grid[self.x_pos][self.y_pos]

        # checks to see if direct is west
        if direct == "west":
            # checks for vaild move
            temp = self.x_pos
            if (temp - 1) < 0:
                print("\nNo houses to the west.")
            # moves if able
            else:
                self.x_pos = self.x_pos - 1
                tmp_grid = self.nh.get_grid();
                self.curr = tmp_grid[self.x_pos][self.y_pos]

    # helper method to attack players
    # @param g_monster - monster to be attacked
    # @param g_weapon - weapon to be attack with
    def g_attack(self, g_monster, g_weapon):
        # checks to see if the monster is not a person
        if g_monster.get_name() != "Person":
            # calls player attack
            self.p.p_attack(g_monster, g_weapon)


    # helper method that removes a monster ands a person
    # @param h_monster - monster to converted into a human
    def humanize(self, h_monster):
        # removes monster from house
        self.curr.remove_observer(h_monster)
        # declares a person
        person = Person()
        # adds a person to thouse
        self.curr.add_observer(person)
        
    
    # helper method that prints the invtory of a player
   
    def print_inv(self):
        # loops through the weapon_list of a player
        for item in self.p.get_weapon_list():
            # checks to see if its a hershey kiss
            if item.get_name() == "hershey kiss":
                #you never run out of kisses
                print(item.get_name())
            # prints item name and uses
            else:
                print(item.get_name(), item.get_uses())

             
    # Method to see if you have won the game
    def check_won(self, nh):
        # count for number of cleared houses
        count = 0
        # loops through the neighborhood
        for x in range(0, nh.get_size()):
            for y in range(0, nh.get_size()):
                # check is a flag to see if a house is cleared
                check = 1
                # tmp is the house to be checked
                tmp = nh.grid[x][y]
                # loops through monsters in tmp
                for m in tmp.observers:
                    # if one of the monster isnt a person
                    if m.get_name() != "Person":
                        # flags house as not cleared
                        check = 0
                # if check is equal to 1 then it increments
                # count
                if check == 1:
                    count = count + 1

        # if count is equal to size of the grid it returns 1
        if count == (size * size):
            return 1
        # else it returns 0
        return 0


if __name__ == '__main__':

    if len(sys.argv) == 2:
        size = int(sys.argv[1])
    # tells you to put in valid input
    else:
        print("Provide a single argument for the size of the grid.\n"
              "Example: ./zork.py 4     creates a 4x4 grid.")
        # and exits to reput in input
        sys.exit(0)

    # Take command line argument for size.
    game = Game(size)
    print("Welcome to Zork!")

    # loop that runs the game
    while game.p.get_hp() > 0:
        # checks to see if the game has been won
        if game.check_won(game.nh) == 1:
                print("All monsters transformed back into humans! You win!")
                sys.exit(0)

        # prints out the commands available
        print("\nEnter Command (Go, Attack, Stats, Inv, Help, Exit): ")
        # converts to lowercase
        command = str.lower(input())

        # if command is go it trys to move the player
        if command == "go":
            # prints off valid directions
            print("Enter direction: North, South, East, West")
            # converts to lowercase and stores the command
            direction = str.lower(input())
            game.go(direction)

            # Lists all monsters in home.
            print("\nMonsters in house at current position ("
                  + str(game.get_x_pos()) + ", " + str(game.get_y_pos()) +
                  "): ")
            
            for x in game.curr.observers:
                print(x.get_name(), "%.2f" % x.get_health())

        # elif command is attack it trys to do an attack sequence
        elif command == "attack":

            # prints available commands for input
            print ("Enter a valid weapon (Hershey Kiss, Chocolate Bar, Sour Straw, Nerd Bomb): ")
            # converts input to lowercase and stores it
            weapon = str.lower(input())

            # sets temp as a weapon
            tmp = Weapon()
            weapon_available = False
            if len(game.curr.observers) != 0:
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

                    i = 0
                    while i < len(game.curr.observers):
                    # for monster in game.curr.observers:
                        # if monster.get_health() <= 0:
                        if game.curr.observers[i].get_health() <= 0:
                            game.humanize(game.curr.observers[i])
                            i = i - 1
                        i = i + 1

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

            else:
                print("\nThis house is empty. There is nothing to attack.")
                
        # Prints player and monsters health
        elif command == "stats":
            print("\n____Player Health____")
            print(game.p.get_hp())

            if len(game.curr.observers) != 0:
                print("\n____Monster Health____")
                for m in game.curr.observers:
                    print(m.get_name(), "%.2f" % m.get_health())
            else:
                print("\nThe house is empty. Maybe you are the monster...")

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
            print("\nCommand not recognized.")

    print("Game over. You lose.")
