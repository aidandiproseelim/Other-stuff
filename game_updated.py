import random
import time
import os


def save_game_data(save_classification, save_rarity, save_damage, save_speed, save_level, save_experience,
                   save_total_player_health, save_player_gold):
    data_to_save = []
    data_to_save.append(str(save_classification))
    data_to_save.append(str(save_rarity))
    data_to_save.append(str(save_damage))
    data_to_save.append(str(save_speed))
    data_to_save.append(str(save_level))
    data_to_save.append(str(save_experience))
    data_to_save.append(str(save_total_player_health))
    data_to_save.append(str(save_player_gold))

    return data_to_save


def create_save(save_data, save_inventory, save_magic):
    save_loop = True
    while save_loop:
        save_slot = input("""Choose a save slot : 
    <1> 
    <2> 
    <3> 
    <4>
    <5>
    """)
        if save_slot == '1' or save_slot == '2' or save_slot == '3' or save_slot == '4' or save_slot == '5':
            save_path = "main_game/saves/"
            save_file = "save_slot{}.txt".format(save_slot)
            save_location = os.path.join(save_path, save_file)
            file = open(save_location, 'w')

            for item in save_data:
                file.write(item + '\n')

            if not save_magic:
                file.write('nothing' + '\t' + '\n')
                
            else:
                for spell in save_magic:
                    file.write(spell + '\t')

                file.write('\n')

            if not save_inventory:
                file.write('nothing' + '\t')

            else:
                for gear in save_inventory:
                    file.write(gear + '\t')

            file.close()

            save_loop = False

        else:
            print('That is not a save slot!')


def load_save():
    load_loop = True
    while load_loop:
        save_slot = input("""Select a save slot to load: 
    <1>
    <2>
    <3>
    <4>
    <5>
    or press <q> to exit
    
    """)
        if save_slot == '1' or save_slot == '2' or save_slot == '3' or save_slot == '4' or save_slot == '5':

            save_data = []
            try:
                save_path = "main_game/saves/"
                save_file = "save_slot{}.txt".format(save_slot)
                save_location = os.path.join(save_path, save_file)  
                file = open(save_location, 'r')

                for line in file:
                    save_data.append(line)

                file.close()

                loop = False

                return save_data

            except FileNotFoundError:
                print("That save file has not been used.")
                print()

        elif save_slot == 'q':
            list(save_data)

            save_data.append('longsword')
            save_data.append('common')
            save_data.append('1')
            save_data.append('5')
            save_data.append('1')
            save_data.append('0')
            save_data.append('50')

            return save_data


        else:
            print("That is not an available save slot. ")


def xp_gain(level, enemy_damage):
    xp = (level + 1) * enemy_damage / 4
    return xp


def gold_gain(enemy_health):
    if enemy_health < 5:
        gold = 1
    else:
        gold = int(enemy_health / 5)
    
    return gold


def weapon():
    weapon_class_list = ['shortsword', 'longsword', 'war axe', 'battleaxe', 'mace', 'greathammer']
    weapon_class = random.choice(weapon_class_list)
    return weapon_class


def rating(level):
    weapon_rating_dict = {28 : 'common',
                          56 : 'uncommon',
                          84 : 'rare',
                          112 : 'epic',
                          140 : 'peerless'}
    weapon_rarity = random.randrange(1,10) * (level * 2)
    for number in weapon_rating_dict:
        if weapon_rarity <= number:
            weapon_rating = weapon_rating_dict[number]
            return weapon_rating
        


def stats(weapon_class, weapon_rating, level, experience):
    damage_multi_class = {'common' : 1, 'uncommon' : 5, 'rare' : 10, 'epic' : 15, 'peerless' : 20}
    
    damage_multi_weapon = {'shortsword' : 0.9,
                           'longsword' : 1,
                           'war axe' : 1.1,
                           'mace' : 1.2,
                           'battleaxe' : 1.3,
                           'greathammer' : 1.4}
    
    damage = (1 + 0.1 * experience) * (level + 1) * damage_multi_class[weapon_rating] * damage_multi_weapon[weapon_class]
    return damage
            

def atk_speed(weapon_class):

    weapon_type = {'greathammer' : 1,
                   'battleaxe' : 2,
                   'mace' : 3,
                   'war axe' : 4,
                   'longsword' : 5,
                   'shortsword' : 6}
    
    speed = weapon_type[weapon_class]
    return speed


def monster_choice(level):
    monster_choice_dict = {1 : ['slime', 'rat'],
                          2 : ['rat', 'fox', 'slime', 'boar'],
                          3 : ['goblin', 'skeleton', 'slime', 'boar', 'wolf', 'fox'],
                          4 : ['goblin', 'skeleton', 'minotaur', 'wolf', 'bear', 'spitter'],
                          5 : ['goblin', 'armoured skeleton', 'minotaur', 'spitter', 'bear', 'white wolf'],
                          6 : ['vicious goblin', 'armoured skeleton', 'minotaur marauder', 'toxic spitter', 'white wolf', 'troll'],
                          7 : ['dragon', 'minotaur marauder', 'venom spitter', 'shadow wolf', 'ravager troll']}
    monster = random.choice(monster_choice_dict[level])
    return monster


def multipliers(monster):
    if 'minotaur' in monster:
        d_multiplier, h_multiplier = 1.1, 1.2
        return d_multiplier, h_multiplier

    elif 'goblin' in monster:
        d_multiplier, h_multiplier = 1.2, 0.7
        return d_multiplier, h_multiplier

    elif 'skeleton' in monster:
        d_multiplier, h_multiplier = 1.1, 1.1

        return d_multiplier, h_multiplier

    elif 'dragon' in monster:
        d_multiplier, h_multiplier = 1.5, 1.5
        return d_multiplier, h_multiplier

    elif 'troll' in monster:
        d_multiplier, h_multiplier = 1.2, 1.4
        return d_multiplier, h_multiplier

    else:
        d_multiplier, h_multiplier = 1, 1
        return d_multiplier, h_multiplier


def monster_stats(level, d_multiplier, health):

    enemy_damage_minimum = level * d_multiplier * (health * 0.1)
    enemy_damage_maximum = level * d_multiplier * (health * 0.2)
    return enemy_damage_minimum, enemy_damage_maximum


def m_speed(monster):
    monster_speed_dict = {'slime' : 3,
                          'rat' : 4,
                          'fox' : 4,
                          'boar' : 3,
                          'wolf' : 5,
                          'skeleton' : 3,
                          'goblin' : 5,
                          'minotaur' : 3,
                          'spitter' : 5,
                          'bear' : 2,
                          'troll' : 1,
                          'armoured skeleton' : 2,
                          'vicious goblin' : 6,
                          'minotaur marauder' : 4,
                          'white wolf' : 5.5,
                          'shadow wolf' : 7,
                          'venom spitter' : 6,
                          'ravager troll' : 2,
                          'dragon' : 4}
    
    enemy_speed = monster_speed_dict[monster]
    return enemy_speed
    

def m_health(level, h_multiplier, experience):

    enemy_health_minimum = level * h_multiplier * (1 + experience * 0.2)
    enemy_health_maximum = level * h_multiplier * (1 + experience * 0.3)
    return enemy_health_minimum, enemy_health_maximum


def combat(monster, enemy_damage, enemy_health, enemy_speed, health, speed, damage, inventory, magic, inventory_dict, magic_dict):

    player_first = False
    monster_first = False
    if speed < enemy_speed:
        enemy_damage *= 1.3
        monster_first = True
    elif speed > monster_speed:
        damage *= 1.5
        player_first = True
    elif speed == enemy_speed:
        first = random.randint(1, 2)
        if first == 1:
            player_first = True
        else:
            monster_first = True


                
    print("Your weapon will deal {:.2f} damage per hit. ".format(damage))
    print("You have {} health. ".format(health))

    while enemy_health > 0 and health > 0:
        time.sleep(0.5)
        

        reflect_damage = False
        negate_damage = False
        crit = False
        stagger = False
        cripple = False
        initial_enemy_damage = enemy_damage
        repeats = 0
        spirit = 10
        print("You have {} spirit.".format(spirit))
        loop = True
        while loop:           

            if monster_first and repeats == 0:
                health -= (enemy_damage / 2)
                print("The {} attacked you for {:.2f} damage, you have {:.2f} health remaining!".format(monster, enemy_damage / 2, health))
                repeats += 1
  
            move = input('''Choose a move:
    < attack    (1) >
    < block     (2) >
    < use item  (3) >
    < use spell (4) >
            ''')
            
            if move == '1':
                if crit:
                    enemy_health -= damage * 1.7
                    print("you attacked the {} for {:.2f} damage, they have {:.2f} health remaining!".format(monster, damage * 1.5, enemy_health))
                    crit = False
                    
                else:
                    enemy_health -= damage
                    print( "you attacked the {} for {:.2f} damage, they have {:.2f} health remaining!".format(monster, damage, enemy_health))

                if enemy_health < 0 or health < 0:
                    break

                if stagger:
                    health -= (enemy_damage / 2)
                    stagger = False
                    
                else:
                    if reflect_damage:
                        enemy_health -= enemy_damage
                        print("You deflected {:.2f} damage, they have {:.2f} health remaining!".format(enemy_damage, enemy_health))
                        reflect_damage = False
                        
                    elif negate_damage:
                        print("Your potion blocked the {}'s attack!".format(monster))
                        negate_damage = False
                        
                    else:
                        health -= enemy_damage
                    
                        print("The {} attacked you for {:.2f} damage, you have {:.2f} health remaining!".format(monster, enemy_damage, health))
                if monster_health < 0 or health < 0:
                    break
                
            elif move == '2':
                if reflect_damage:
                    enemy_health -= enemy_damage
                    print("You deflected {:.2f} damage, they have {:.2f} health remaining!".format(enemy_damage, enemy_health))
                    reflect_damage = False
                elif negate_damage:
                    print("Your potion blocked the {}'s attack!".format(monster))
                    negate_damage = False
                
                else:
                    health -= (enemy_damage / 3)
                    print("The {} attacked you for {:.2f} damage, you have {:.2f} health remaining!".format(monster, enemy_damage / 3, health))
                if enemy_health < 0 or health < 0:
                    break
                
                print("Your next attack will deal 70 % more damage! ")
                crit = True
                stagger = True
                
            elif move == '3':
                valid_number = 0
                for item in inventory_dict:
                    if item in inventory:
                        valid_number += 1
                    
                   
                if valid_number == 0:
                    print('Your inventory is empty!')
                    
                else:
                    print("In your inventory, you have:")

                    
                    for item, number in inventory_dict.items():
                        if item in inventory:
                            duplicates = inventory.count(item)
                            print(item, 'x' + str(duplicates) +'   <{}>'.format(number))
                    
                        
                    choosing_item = True
                    while choosing_item:
                        use_item = input("""What item would you like to use? Type the number or enter <q> to exit """).strip().lower()
                            
                        if (use_item == inventory_dict['Small Health Potion']) and ('Small Health Potion' in inventory):
                            health += (0.25 * total_player_health)
                            print('You have been healed for {:.2f} points, you have {:.2f} health'.format(0.25 * total_player_health, health))
                            inventory.remove('Small Health Potion')
                            choosing_item = False
                            
                        elif (use_item == inventory_dict['Large Health Potion']) and ('Large Health Potion' in inventory):
                            health += (0.75 * total_player_health)
                            print('You have been healed for {:.2f} points, you have {:.2f} health'.format(0.75 * total_player_health, health))
                            inventory.remove('Large Health Potion')
                            choosing_item = False
                            
                        elif (use_item == inventory_dict['Berserker Potion']) and ('Berserker Potion' in inventory):
                            damage *= 1.6
                            inventory.remove('Berserker Potion')
                            choosing_item = False
                            
                        elif (use_item == inventory_dict['Reflect Potion']) and ('Reflect Potion' in inventory):
                            reflect_damage = True
                            inventory.remove('Reflect Potion')
                            choosing_item = False
                            
                        elif (use_item == inventory_dict['Damage Potion']) and ('Damage Potion' in inventory):
                            enemy_health -= (enemy_health * 0.3)
                            print("The {} has been damaged for {:.2f} points, they have {:.2f} health left.".format(monster, enemy_health * 0.3, enemy_health))
                            inventory.remove('Damage Potion')
                            choosing_item = False

                        elif (use_item == inventory_dict['Negative Potion']) and ('Negative Potion' in inventory):
                            negate_damage = True
                            inventory.remove('Negative Potion')
                            choosing_item = False

                        elif use_item == 'q':
                            choosing_item = False

                        else:
                            print('That is not a usable item')
                            
            elif move == '4':
                valid_number = 0
                for spell in magic_dict:
                    if spell in magic:
                        valid_number += 1

                if valid_number == 0:
                    print('You know no spells.')
                    
                else:
                    print("You can cast:")
                    for spell, number in magic_dict.items():
                        if spell in magic:
                            print(spell, '   <{}>'.format(number))
                        
                    choosing_spell = True
                    while choosing_spell:
                        use_spell = input("""What spell would you like to use? Type the number or enter <q> to exit """).strip().lower()
                        if (use_spell == magic_dict['Cripple']) and ('Cripple' in magic) and (spirit >= 5):
                            cripple = True
                            print('The {} has been crippled!'.format(monster))
                            magic.remove('Cripple')
                            spirit -= 5
                            print('You have {} spirit remaining'.format(spirit))
                            choosing_spell = False
                            
                        elif (use_spell == magic_dict['Blood Leech']) and ('Blood Leech' in magic) and (spirit >= 2):
                            enemy_health -= (enemy_health * 0.2)
                            health += (enemy_health * 0.2)
                            print('The {} has been wounded for {:.2f} and you have been healed for {:.2f}!'.format(monster, enemy_health * 0.2, enemy_health * 0.2))
                            magic.remove('Blood Leech')
                            spirit -= 2
                            print('You have {} spirit remaining'.format(spirit))
                            choosing_spell = False
                            
                        elif (use_spell == magic_dict['Inversion']) and ('Inversion' in magic) and (spirit >= 2):
                            health, enemy_health = enemy_health, health
                            print('You have been healed for {:.2f} points, you have {:.2f} health'.format(0.25 * total_player_health, health))
                            magic.remove('Small Health Potion')
                            spirit -= 2
                            print('You have {} spirit remaining'.format(spirit))
                            choosing_spell = False

                        elif use_spell == 'q':
                            choosing_spell = False

                        else:
                            print('You cannot cast that.')
                                            
                        
            else:
                print("That is not an option. ")
                
    if health <= 0:
        print("""
        You have been defeated by the {}!
        """.format(monster))
        dead = True
        return dead

    elif monster_health <= 0:
        print("""
        You have defeated the {}!
        """.format(monster))
        return dead
                

primary_loop = 'y'
while primary_loop:
    player_experience = 0
    player_gold = 0
    main_inventory = []
    main_inventory_dict = {'Small Health Potion' : '1',
                           'Large Health Potion' : '2',
                           'Berserker Potion' : '3',
                           'Reflect Potion' : '4',
                           'Negative Potion' : '5',
                           'Damage Potion' : '6'}

    player_magic = []
    main_magic_dict = {'Cripple' : '1',
                       'Blood Leech' : '2',
                       'Inversion' : '3'}
    
    player_level = 1
    level_two = False
    level_three = False
    level_four = False
    level_five = False
    level_six = False
    level_seven = False

    player_dead = False

    total_player_health = 30
    player_health = total_player_health

    #starter weapon
    player_classification = 'longsword'
    player_rarity = 'common'
    player_damage = 1
    player_speed = 5

    print()
    load_game = input("Welcome to <game_name>! Press <enter> to start a new game or anything else to load a save. ")
    print()

    if load_game != "":
        repeat = True
        while repeat:
            save_data = load_save()
            try:
                player_classification = save_data[0].strip()
                player_rarity = save_data[1].strip()
                player_damage = float(save_data[2])
                player_speed = int(save_data[3])
                player_level = int(save_data[4])
                player_experience = float(save_data[5])
                player_gold = int(save_data[7])
                read_magic = save_data[8].split('\t')
                for spell in read_magic:
                    player_magic.append(spell)
                
                read_items = save_data[9].split('\t')
                for item in read_items:
                    main_inventory.append(item)
                    

                if player_level >= 1:
                    level_one = True
                if player_level >= 2:
                    level_two = True
                if player_level >= 3:
                    level_three = True
                if player_level >= 4:
                    level_four = True
                if player_level >= 5:
                    level_five = True
                if player_level >= 6:
                    level_six = True
                if player_level >= 7:
                    level_seven = True

                total_player_health = int(save_data[6])

                player_health = total_player_health
                repeat = False

            except IndexError:
                print('That save is empty!')
                print()

    print("""Your weapon is a {} {}:
    > Damage: {:.2f}
    > Speed: {:.2f}
    """.format(player_rarity, player_classification, player_damage, player_speed))
    try:
        main_inventory.remove('nothing')
        main_inventory.remove('\n')
        player_magic.remove('nothing')
        player_magic.remove('\n')
    except ValueError:
        print()

    battle = ''
    while battle == '':

        chosen_monster = monster_choice(player_level)

        d_multiplier, h_multiplier = multipliers(chosen_monster)
        monster_damage_minimum, monster_damage_maximum = monster_stats(player_level, d_multiplier, player_health)
        monster_damage = round(random.uniform(monster_damage_minimum, monster_damage_maximum), 1)
        monster_health_minimum, monster_health_maximum = m_health(player_level, h_multiplier, player_health)
        monster_health = round(random.uniform(monster_health_minimum, monster_health_maximum), 1)
        monster_speed = m_speed(chosen_monster)

        print("""You are fighting a {}!
         > Damage: {:.2f}
         > Health: {:.2f}
         > Speed: {}""".format(chosen_monster, monster_damage, monster_health, monster_speed))
        print()

        time.sleep(1)

        dead = combat(chosen_monster, monster_damage, monster_health, monster_speed, player_health, player_speed, player_damage, main_inventory, player_magic, main_inventory_dict, main_magic_dict)

        if dead:
            break

        xp = xp_gain(player_level, monster_health)
        gold = gold_gain(monster_health)
        player_experience += xp
        player_gold += gold
        print("XP: {:.2f}".format(player_experience))
        print("Gold: {}".format(player_gold))
        time.sleep(1)

        if 50 <= player_experience < 200 and not level_two:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 2!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_two = True
            total_player_health += 50

        elif 200 <= player_experience < 500 and not level_three:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 3!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_three = True
            total_player_health += int(monster_health)

        elif 500 <= player_experience < 2500 and not level_four:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 4!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_four = True
            total_player_health += int(monster_health)

        elif 2500 <= player_experience < 7500 and not level_five:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 5!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_five = True
            total_player_health += int(monster_health)

        elif 7500 <= player_experience < 15000 and not level_six:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 6!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_six = True
            total_player_health += int(monster_health)

        elif 15000 <= player_experience and not level_seven:
            player_level += 1
            print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            ~~~You have reached level 7!~~~
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
            level_seven = True
            total_player_health += int(monster_health)

        player_health = total_player_health

        time.sleep(1.5)

        loot = random.randrange(1, 100)
        if 0 == loot % 2:
            loot_classification = weapon()
            loot_rarity = rating(player_level)
            loot_damage = stats(loot_classification, loot_rarity, player_level, player_experience)
            loot_speed = atk_speed(loot_classification)
            print("""You found a {} {}!
          > Damage: {:.2f}
          > Speed: {}
            """.format(loot_rarity, loot_classification, loot_damage, loot_speed))
            print()

            print("""Your current weapon is a {} {}!
          > Damage: {:.2f}
          > Speed: {}
            """.format(player_rarity, player_classification, player_damage, player_speed))

            take_loot = input("Do you want to swap for this weapon? (y/n)".strip().lower())

            if take_loot == 'y' or take_loot == 'yes':
                player_classification = loot_classification
                player_rarity = loot_rarity
                player_damage = loot_damage
                player_speed = loot_speed

            print()

        shop = random.randrange(1,100)
        if 0 == shop % 3:
            print("You have encountered a wandering merchant.")
            use_shop = input("Would you like to see his stock? (y/n) ")
            if use_shop == 'y':
                shopping = True
                merchant_items = {'Small Health Potion' : [5, '[heal 25 % health points]'],
                                  'Large Health Potion' : [20, '[heal 75 % health points]'],
                                  'Berserker Potion' : [15, '[bonus 60 % damage]'],
                                  'Reflect Potion' : [30, '[reflect enemy damage back]'],
                                  'Damage Potion' : [20, '[instantly hits enemy for 30 % health]'],
                                  'Negative Potion' : [15, '[stops enemy from dealing damage]']}

                shop_choice = []
                for i in range(3):
                    shop_choice.append(random.choice(list(merchant_items)))
                    
                while shopping:
                
    
                    buy = input("""
MERCHANT STOCK:
    > {} {} -- {} Gold (input <1> to buy)
    > {} {} -- {} Gold (input <2> to buy)
    > {} {} -- {} Gold (input <3> to buy)
    When finished, input <q> to exit the store.
    You have {} gold to spend
    
    """.format(shop_choice[0], merchant_items[shop_choice[0]][1], merchant_items[shop_choice[0]][0],
               shop_choice[1], merchant_items[shop_choice[1]][1], merchant_items[shop_choice[1]][0],
               shop_choice[2], merchant_items[shop_choice[2]][1], merchant_items[shop_choice[2]][0],
               player_gold))
                    print()
                    if buy == '1':
                        if player_gold >= merchant_items[shop_choice[0]][0]:
                            main_inventory.append(shop_choice[0])
                            player_gold -= merchant_items[shop_choice[0]][0]
                        else:
                            print('You do not have enough gold for that item.')
                    elif buy == '2':
                        if player_gold >= merchant_items[shop_choice[1]][0]:
                            main_inventory.append(shop_choice[1])
                            player_gold -= merchant_items[shop_choice[1]][0]
                        else:
                            print('You do not have enough gold for that item.')
                    elif buy == '3':
                        if player_gold >= merchant_items[shop_choice[2]][0]:
                            main_inventory.append(shop_choice[2])
                            player_gold -= merchant_items[shop_choice[2]][0]
                        else:
                            print('You do not have enough gold for that item.')
                    else:
                        shopping = False
                        
        mage = random.randrange(1, 100)
        if 0 == mage % 3:
            print()
            print("You encounter a travelling mage.")
            buy_spells = input('Would you like to see what they have for sale? (y/n)')
            if buy_spells == 'y':
                shopping = True
                mage_items = {'Cripple' : [80, '[reduce enemy damage by 40 % and weaken them by 40 %]'],
                                  'Blood Leech' : [120, '[damage enemy for 20 % health and heal you for that much]'],
                                  'Inversion' : [100, "[switch your current health with the enemy's health.]"]}

                shop_choice = []
                for i in range(3):
                        shop_choice.append(random.choice(list(mage_items)))
                        
                while shopping:
                
    
                    buy = input("""
MAGE STOCK:
    > {} {} -- {} Gold (input <1> to buy)
    > {} {} -- {} Gold (input <2> to buy)
    > {} {} -- {} Gold (input <3> to buy)
    When finished, input <q> to exit the store.

    [spells are one time purchases, and can be used more than once]
    You have {} gold to spend
    
    """.format(shop_choice[0], mage_items[shop_choice[0]][1], mage_items[shop_choice[0]][0],
               shop_choice[1], mage_items[shop_choice[1]][1], mage_items[shop_choice[1]][0],
               shop_choice[2], mage_items[shop_choice[2]][1], mage_items[shop_choice[2]][0],
               player_gold))
                    print()
                    if buy == '1':
                        if player_gold >= mage_items[shop_choice[0]][0]:
                            player_magic.append(shop_choice[0])
                            player_gold -= mage_items[shop_choice[0]][0]
                        else:
                            print('You do not have enough gold for that spell.')
                    elif buy == '2':
                        if player_gold >= mage_items[shop_choice[1]][0]:
                            player_magic.append(shop_choice[1])
                            player_gold -= mage_items[shop_choice[1]][0]
                        else:
                            print('You do not have enough gold for that spell.')
                    elif buy == '3':
                        if player_gold >= mage_items[shop_choice[2]][0]:
                            player_magic.append(shop_choice[2])
                            player_gold -= mage_items[shop_choice[2]][0]
                        else:
                            print('You do not have enough gold for that spell.')
                    else:
                        shopping = False
                        
        battle = input('Press <enter> to continue, or press <s> to save your game. ')
        if battle == 's':
            save_data = save_game_data(player_classification, player_rarity, player_damage, player_speed, player_level, player_experience, total_player_health, player_gold)
            create_save(save_data, main_inventory, player_magic)

            battle = input("Save successful! Press <enter> to continue or <q> to quit. ")
            save_data.clear()

    if battle != '':
        break
    
    else:
        print()
        print('Would you like to return to the start?')
        primary_loop = input('y/n'.strip().lower())

