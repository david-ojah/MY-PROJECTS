from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.items import Items

# Magic
fire = Spell("Dragon's Breath", 20, 100, "Dark")
ice = Spell("Frostbite", 15, 80, "Dark")
lightning = Spell("Thunderbolt", 10, 60, "Dark")
air = Spell("Whirlwind", 5, 40, "Dark")
heal = Spell("Heal Spell(75 HP)", 15, 75, "Defence Magic")
player_spells = [fire, ice, lightning, air, heal]
# Items
heal_potion = Items("Heal Potion", "Self Heal", "Restores 75 Health", 100)
mega_heal = Items("Mega Heal Potion", "Self Heal", "Restores 100% Health", 600)
elixir = Items("Elixir", "Party heal", "Restores 100% Mana and Health of one party member", 600)
mega_elixir = Items("MegaElixir", "Party heal all", "Restores 100% Mana and Health of all party members", 600)
grenade = Items("Grenade", "Throwable", "Deals 300 damage", 300)
player_items = [heal_potion, mega_heal, elixir, mega_elixir, grenade]
# Instantiate People
player = Person(500, 65, 34, 35, player_spells, player_items)
enemy = Person(1200, 65, 40, 45, [], [])

running = True

print(Bcolors.OKRED + Bcolors.BOLD + "ENEMY" + Bcolors.ENDC)

while running:
    print("===================")
    player.choose_action()
    player_choice = int(input(Bcolors.OKBLUE + Bcolors.BOLD + "Choose Action\n" + Bcolors.ENDC))
    index = player_choice - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print(Bcolors.OKGREEN + Bcolors.BOLD + "You've dealt", damage, "points of damage" + Bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        player_choice_magic = int(input(Bcolors.OKBLUE + Bcolors.BOLD +
                                        "Choose Magic or Press '0' to go back to previous Menu:\n" + Bcolors.ENDC)) - 1
        spell = player.magic[player_choice_magic]
        magic_damage = spell.generate_magic_damage()
        if player_choice_magic == -1:
            continue

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.OKRED, "\nNot Enough magic points", Bcolors.ENDC)
            print("-------------------")
            print(Bcolors.OKBLUE + Bcolors.BOLD + "Your Mana:", str(player.get_mp()),
                  "/", str(player.get_max_mp()) + Bcolors.ENDC)
            continue
        player.deduct_mp(spell.cost)

        if spell.magic_type == "Defence Magic":
            player.heal(magic_damage)
            print(Bcolors.OKGREEN + Bcolors.BOLD + "You've healed", magic_damage, "Health with", spell.name + Bcolors.ENDC)
        elif spell.magic_type == "Dark":
            enemy.take_damage(magic_damage)
            print(Bcolors.OKGREEN + Bcolors.BOLD + "You've dealt", magic_damage, "points of  magical damage with",
                  spell.name + Bcolors.ENDC)
    elif index == 2:
        player.choose_items()
        player_choice_items = int(input(Bcolors.OKGREEN + Bcolors.BOLD +
                                        "Choose Items or Press '0' to go back to previous Menu:\n" + Bcolors.ENDC)) - 1
        if player_choice_items == -1:
            continue

        items = player.items[player_choice_items]
        if items.item_type == "Self Heal":
            player.heal(items.props)
            print(Bcolors.OKGREEN + Bcolors.BOLD + "You've healed", items.props, "HP with",
                  items.name + Bcolors.ENDC)
        elif items.item_type == "Throwable":
            enemy.take_damage(items.props)
            print(Bcolors.OKGREEN + Bcolors.BOLD + "You've dealt", items.props, "points of damage with",
                  items.name + Bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(Bcolors.OKRED + Bcolors.BOLD + "The Enemy has dealt", enemy_damage, "points of damage." + Bcolors.ENDC)
    print("-------------------")
    print(Bcolors.OKGREEN + Bcolors.BOLD + "Your Health:", str(player.get_hp()),
          "/", str(player.get_max_hp()) + Bcolors.ENDC)
    print(Bcolors.OKBLUE + Bcolors.BOLD + "Your Mana:", str(player.get_mp()),
          "/", str(player.get_max_mp()) + Bcolors.ENDC)
    print(Bcolors.OKRED + Bcolors.BOLD + "Enemy Health:", str(enemy.get_hp()) + Bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN, "You've Won", Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.OKRED, "You've been Defeated", Bcolors.ENDC)
        running = False
