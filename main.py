from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 30},
         {"name": "Ice", "cost": 20, "damage": 40},
         {"name": "Water", "cost": 5, "damage": 20}]
player = Person(500, 65, 34, 60, magic)
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
        print("You've dealt", damage, "points of damage", " Enemy HP:", enemy.get_hp())

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("The Enemy has dealt", enemy_damage, "points of damage", " Your HP:", player.get_hp())