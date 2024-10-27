import random

# Print game title
print('Welcome to AdventureMania!')
print('New Game')

# User creates their character
player_name = input('Character Name: ')
player_class = input('Choose your class (Swordsman, Elf Archer, Wizard): ')

# Define player stats based on class and assign attacks
if player_class.lower() == 'swordsman':
    player_health = 100
    player_attack = 15
    player_defense = 10
    player_attacks = {
        "Sword Strike": 20,
        "Shield Bash": 10
    }
elif player_class.lower() == 'elf archer':
    player_health = 80
    player_attack = 18
    player_defense = 8
    player_attacks = {
        "Long Bow": 15,
        "Throw Bomb": 25
    }
elif player_class.lower() == 'wizard':
    player_health = 70
    player_attack = 20
    player_defense = 5
    player_attacks = {
        "Fireball": 30,
        "Ice Blast": 15
    }
else:
    print("Invalid class! Defaulting to Swordsman.")
    player_class = 'Swordsman'
    player_health = 100
    player_attack = 15
    player_defense = 10
    player_attacks = {
        "Sword Strike": 20,
        "Shield Bash": 10
    }

# Initialize player level
player_level = 1

print(f"\nWelcome, {player_name} the {player_class}!")
print(f"Stats - Level: {player_level}, Health: {player_health}, Attack: {player_attack}, Defense: {player_defense}\n")

print(f"{player_name} Is walking through a forest..")


# Function to simulate dice roll
def roll_dice(sides=6):
    return random.randint(1, sides)


# Create an enemy and scale its stats based on player level
def create_enemy(player_level):
    enemies = [
        {"name": "Goblin", "base_health": 35, "base_attack": 10, "base_defense": 5, "attacks": {"Claw Swipe": 8, "Poison Spit": 12}},
        {"name": "Orc", "base_health": 60, "base_attack": 12, "base_defense": 7, "attacks": {"Club Smash": 15, "War Cry": 5}},
        {"name": "Dark Wizard", "base_health": 50, "base_attack": 15, "base_defense": 3, "attacks": {"Shadow Bolt": 20, "Curse": 10}}
    ]
    enemy = random.choice(enemies)
    # Scale enemy stats based on player level
    enemy['health'] = int(enemy['base_health'] * (1 + player_level * 0.1))
    enemy['attack'] = int(enemy['base_attack'] * (1 + player_level * 0.1))
    enemy['defense'] = int(enemy['base_defense'] * (1 + player_level * 0.1))
    return enemy


# Function to find treasure based on player level
def find_treasure(player_level):
    # Basic treasure for lower levels
    basic_treasures = [
        {"type": "Health Potion", "heal": 20},
        {"type": "Super Potion", "heal": 50},
        {"type": "Enchanted Sword", "attack_increase": 5},
        {"type": "Magic Shield", "defense_increase": 3}
    ]

    # Advanced treasures for higher levels
    advanced_treasures = [
        {"type": "Greater Health Potion", "heal": 100},
        {"type": "Legendary Sword", "attack_increase": 15},
        {"type": "Mystic Armor", "defense_increase": 10},
        {"type": "Phoenix Feather", "heal": player_health // 2}  # Heals half of max health
    ]

    # Determine treasure tier based on player level
    if player_level >= 5:
        return random.choice(advanced_treasures)
    else:
        return random.choice(basic_treasures)


# Process treasure effects
def apply_treasure(treasure, player_health, player_attack, player_defense):
    if "heal" in treasure:
        player_health += treasure["heal"]
        print(f"You found a {treasure['type']}! It heals you by {treasure['heal']} health points. Your health is now {player_health}.")
    elif "attack_increase" in treasure:
        player_attack += treasure["attack_increase"]
        print(f"You found an {treasure['type']}! Your attack increases by {treasure['attack_increase']}. Your attack is now {player_attack}.")
    elif "defense_increase" in treasure:
        player_defense += treasure["defense_increase"]
        print(f"You found a {treasure['type']}! Your defense increases by {treasure['defense_increase']}. Your defense is now {player_defense}.")
    return player_health, player_attack, player_defense


# Level up function
def level_up(player_level, player_health, player_attack, player_defense):
    player_level += 1
    player_health = int(player_health * 1.1)
    player_attack = int(player_attack * 1.1)
    player_defense = int(player_defense * 1.1)
    print(f"\nLevel up! You are now level {player_level}.")
    print(f"New stats - Health: {player_health}, Attack: {player_attack}, Defense: {player_defense}\n")
    return player_level, player_health, player_attack, player_defense


# Start combat
def combat(player_health, player_attack, player_defense, player_attacks, player_level):
    enemy = create_enemy(player_level)
    print(f"\nA wild {enemy['name']} appears!")
    print(f"Enemy stats - Health: {enemy['health']}, Attack: {enemy['attack']}, Defense: {enemy['defense']}\n")

    # Combat loop
    while player_health > 0 and enemy['health'] > 0:
        # Player's turn - Choose attack
        print("\nYour available attacks:")
        for attack, power in player_attacks.items():
            print(f"- {attack} (Power: {power})")
        chosen_attack = input("Choose your attack: ").strip().title()

        if chosen_attack in player_attacks:
            attack_power = player_attacks[chosen_attack]
        else:
            print("Invalid choice! Defaulting to a basic attack.")
            chosen_attack = list(player_attacks.keys())[0]
            attack_power = player_attacks[chosen_attack]

        # Player's attack roll
        player_roll = roll_dice(20) + attack_power
        enemy_roll = roll_dice(20) + enemy['defense']
        if player_roll > enemy_roll:
            damage = player_roll - enemy_roll
            enemy['health'] -= damage
            print(f"{player_name} used {chosen_attack} and hit the {enemy['name']}, {damage} damage dealt! Enemy health reduced to {enemy['health']}.")
        else:
            print("Your attack missed!")

        # Check if enemy is defeated
        if enemy['health'] <= 0:
            print(f"You defeated the {enemy['name']}!\n")
            return player_health, True  # Return True indicating victory

        # Enemy's turn - Randomly choose an attack
        enemy_attack = random.choice(list(enemy['attacks'].keys()))
        enemy_attack_power = enemy['attacks'][enemy_attack]

        # Enemy's attack roll
        enemy_roll = roll_dice(20) + enemy_attack_power
        player_roll = roll_dice(20) + player_defense
        if enemy_roll > player_roll:
            damage = enemy_roll - player_roll
            player_health -= damage
            print(f"The {enemy['name']} used {enemy_attack} and dealt {damage} damage! Your health is now {player_health}.")
        else:
            print(f"The {enemy['name']}'s attack missed!")

        # Check if player is defeated
        if player_health <= 0:
            print("You have been defeated! Game Over.\n")
            return player_health, False  # Return False indicating loss

    return player_health, False


# Game loop
while player_health > 0:
    player_health, victory = combat(player_health, player_attack, player_defense, player_attacks, player_level)
    if victory:
        print("Congratulations, you survived this battle!")
        player_level, player_health, player_attack, player_defense = level_up(player_level, player_health, player_attack, player_defense)

        # Offer the player a choice to continue or find treasure
        next_step = input("Do you want to continue deeper into the forest for another battle, or search for treasure? (battle/treasure): ").strip().lower()
        if next_step == 'treasure':
            treasure = find_treasure(player_level)  # Pass player level to find_treasure
            player_health, player_attack, player_defense = apply_treasure(treasure, player_health, player_attack, player_defense)
        elif next_step == 'battle':
            print("\nYou venture further into the forest and prepare for another battle...")
        else:
            print("Invalid choice. Continuing further into the forest by default.\n")
    else:
        print("Better luck next time, adventurer.")
        break
