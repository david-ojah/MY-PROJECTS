import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, df, atk, magic, items):
        self.atkl = atk - 25
        self.atkh = atk + 25
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.magic = magic
        self.df = df
        self.items = items
        self.actions = ["Melee Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def deduct_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def choose_action(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "Actions" + Bcolors.ENDC)
        for item in self.actions:
            print(Bcolors.OKGREEN + Bcolors.BOLD + "    " + str(i) + ":", item + Bcolors.ENDC)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "Magic:" + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "Your Mana:", str(self.mp),
              "/", str(self.mp) + Bcolors.ENDC)
        for spell in self.magic:
            print(Bcolors.OKGREEN + Bcolors.BOLD + "    " + str(i) + ":", spell.name, "(cost:",
                  str(spell.cost) + " Mana)" + Bcolors.ENDC)
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "Items:" + Bcolors.ENDC)
        for items in self.items:
            print(Bcolors.OKBLUE + Bcolors.BOLD + "    " + str(i) + ":", items.name, ":",
                  items.description + Bcolors.ENDC)
            i += 1
