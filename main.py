from classes.game import Person, Bcolors

magic = [{"name": "Dragon's Breath", "cost": 10, "damage": 100},
         {"name": "Frostbite", "cost": 20, "damage": 80},
         {"name": "Thunderbolt", "cost": 5, "damage": 60}]
player = Person(500, 65, 34, 40, magic)
enemy = Person(1200, 65, 40, 25, magic)

running = True

print(Bcolors.OKRED + Bcolors.BOLD + "ENEMY" + Bcolors.ENDC)

while running:
    print("===================")
    player.choose_action()
    player_choice = int(input("Choose Action\n"))
    index = player_choice - 1

    if index == 0:
        damage = player.generate_damage()
        enemy.take_damage(damage)
        print(Bcolors.OKGREEN + Bcolors.BOLD + "You've dealt", damage, "points of damage" + Bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        player_choice_magic = int(input("Choose Magic:\n")) - 1
        magic_damage = player.generate_magic_damage(player_choice_magic)
        enemy.take_damage(magic_damage)
        spell = player.get_spell_name(player_choice_magic)
        cost = player.get_mp_spell_cost(player_choice_magic)
        current_mp = player.get_mp()
        print(Bcolors.OKGREEN + Bcolors.BOLD + "You've dealt", magic_damage, "points of  magical damage with",
              spell + Bcolors.ENDC)

        if cost > current_mp:
            print(Bcolors.OKRED, "\nNot Enough magic points", Bcolors.ENDC)
            print("-------------------")
            print(Bcolors.OKGREEN + Bcolors.BOLD + "Your HP:", str(player.get_hp()),
                  "/", str(player.get_max_hp()) + Bcolors.ENDC)
            print(Bcolors.OKBLUE + Bcolors.BOLD + "Your MP:", str(player.get_mp()),
                  "/", str(player.get_max_mp()) + Bcolors.ENDC)
            print(Bcolors.OKRED + Bcolors.BOLD + "Enemy HP:", str(enemy.get_hp()) + Bcolors.ENDC)
            continue
        player.deduct_mp(cost)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print(Bcolors.OKRED + Bcolors.BOLD + "The Enemy has dealt", enemy_damage, "points of damage." + Bcolors.ENDC)
    print("-------------------")
    print(Bcolors.OKGREEN + Bcolors.BOLD + "Your HP:", str(player.get_hp()),
          "/", str(player.get_max_hp()) + Bcolors.ENDC)
    print(Bcolors.OKBLUE + Bcolors.BOLD + "Your MP:", str(player.get_mp()),
          "/", str(player.get_max_mp()) + Bcolors.ENDC)
    print(Bcolors.OKRED + Bcolors.BOLD + "Enemy HP:", str(enemy.get_hp()) + Bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN, "You've Won", Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.OKRED, "You've been Defeated", Bcolors.ENDC)
        running = False
