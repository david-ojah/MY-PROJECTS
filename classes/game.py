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
    def __init__(self, hp, mp, df, atk, magic):
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.magic = magic
        self.df = df
        self.actions = ["Melee Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_magic_damage(self, i):
        magic_low = self.magic[i]["damage"] - 10
        magic_high = self.magic[i]["damage"] + 10
        return random.randrange(magic_low, magic_high)

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

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_mp_spell_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
