import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Define desired sizes
background_size = (1280,720)  # screen size
swordsman_size = (100, 150)    # size for the swordsman sprite
archer_size = (100, 150)       # size for the swordsman sprite
wizard_size = (100, 150)       # size for the swordsman sprite
goblin_size = (80, 120)        # size for the swordsman sprite
orc_size = (100, 150)          # size for the swordsman sprite
dark_wizard_size = (100, 150)  # size for the swordsman sprite

# Load images
base_path = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(base_path, 'images', 'forest_background.jpg'))
swordsman_sprite = pygame.image.load(os.path.join(base_path, 'images', 'swordsman.png'))
archer_sprite = pygame.image.load(os.path.join(base_path, 'images', 'brawler.png'))
wizard_sprite = pygame.image.load(os.path.join(base_path, 'images', 'wizard.png'))

# Load enemy sprites
goblin_sprite = pygame.image.load(os.path.join(base_path, 'images', 'goblin.png'))
orc_sprite = pygame.image.load(os.path.join(base_path, 'images', 'alien.png'))
dark_wizard_sprite = pygame.image.load(os.path.join(base_path, 'images', 'witch.png'))

# Scale images to desired sizes
background_image = pygame.transform.scale(background_image, background_size)
swordsman_sprite = pygame.transform.scale(swordsman_sprite, swordsman_size)
archer_sprite = pygame.transform.scale(archer_sprite, archer_size)
wizard_sprite = pygame.transform.scale(wizard_sprite, wizard_size)
goblin_sprite = pygame.transform.scale(goblin_sprite, goblin_size)
orc_sprite = pygame.transform.scale(orc_sprite, orc_size)
dark_wizard_sprite = pygame.transform.scale(dark_wizard_sprite, dark_wizard_size)

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)

# Print game title
print('Welcome to AdventureMania!')
print('New Game')

# User creates their character
player_name = input('Character Name: ')
player_class = input('Choose your class (Swordsman, Brawler, Wizard): ')

# Define player stats based on class and assign attacks
if player_class.lower() == 'swordsman':
    player_health = 100
    player_attack = 15
    player_defense = 10
    player_attacks = {
        "Sword Strike": 25,
        "Shield Bash": 15
    }
    player_sprite = swordsman_sprite
elif player_class.lower() == 'brawler':
    player_health = 80
    player_attack = 18
    player_defense = 8
    player_attacks = {
        "Punch": 20,
        "Kick": 20
    }
    player_sprite = archer_sprite
elif player_class.lower() == 'wizard':
    player_health = 70
    player_attack = 20
    player_defense = 5
    player_attacks = {
        "Fireball": 30,
        "Spell": 10
    }
    player_sprite = wizard_sprite
else:
    print("Invalid class! Defaulting to Swordsman.")
    player_class = 'Swordsman'
    player_health = 100
    player_attack = 15
    player_defense = 10
    player_attacks = {
        "Sword Strike": 25,
        "Shield Bash": 15
    }
    player_sprite = swordsman_sprite

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
        {"name": "Goblin", "base_health": 35, "base_attack": 10, "base_defense": 5, "attacks": {"Claw Swipe": 8, "Poison Spit": 12}, "sprite": goblin_sprite},
        {"name": "Orc", "base_health": 60, "base_attack": 12, "base_defense": 7, "attacks": {"Club Smash": 15, "War Cry": 5}, "sprite": orc_sprite},
        {"name": "Dark Wizard", "base_health": 50, "base_attack": 15, "base_defense": 3, "attacks": {"Shadow Bolt": 20, "Curse": 10}, "sprite": dark_wizard_sprite}
    ]
    enemy = random.choice(enemies)
    enemy['health'] = int(enemy['base_health'] * (1 + player_level * 0.1))
    enemy['attack'] = int(enemy['base_attack'] * (1 + player_level * 0.1))
    enemy['defense'] = int(enemy['base_defense'] * (1 + player_level * 0.1))
    return enemy


# Function to draw health bars
def draw_health_bars(player_health, enemy_health, enemy_base_health):
    # Player health bar
    player_health_bar_width = int((player_health / 100) * 200)
    pygame.draw.rect(screen, (0, 255, 0), (100, 350, player_health_bar_width, 20))

    # Enemy health bar
    enemy_health_bar_width = int((enemy_health / enemy_base_health) * 200)
    pygame.draw.rect(screen, (255, 0, 0), (500, 350, enemy_health_bar_width, 20))


# Combat function
def combat(player_health, player_attack, player_defense, player_attacks, player_level):
    enemy = create_enemy(player_level)
    enemy_sprite = enemy['sprite']
    print(f"\nA wild {enemy['name']} appears!")

    while player_health > 0 and enemy['health'] > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return player_health, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # "Sword Strike"
                    chosen_attack = "Sword Strike"
                elif event.key == pygame.K_2 and player_class.lower() == 'elf archer':  # "Long Bow"
                    chosen_attack = "Long Bow"
                elif event.key == pygame.K_3 and player_class.lower() == 'wizard':  # "Fireball"
                    chosen_attack = "Fireball"
                else:
                    print("Invalid choice! Defaulting to a basic attack.")
                    chosen_attack = list(player_attacks.keys())[0]

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

        # Drawing sprites
        screen.blit(background_image, (0, 0))
        screen.blit(player_sprite, (100, 400))
        screen.blit(enemy_sprite, (500, 400))  # Display the enemy sprite

        # Display player and enemy health bars
        draw_health_bars(player_health, enemy['health'], enemy['base_health'])

        # Display player stats
        player_text = font.render(f"{player_name} - Health: {player_health}", True, (255, 255, 255))
        screen.blit(player_text, (50, 50))

        pygame.display.flip()

    return player_health, False

# Main game loop
running = True
while player_health > 0 and running:
    player_health, victory = combat(player_health, player_attack, player_defense, player_attacks, player_level)
    if victory:
        player_level += 1  # Leveling up (expand as needed)
    else:
        running = False  # End the game if player is defeated

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background and sprites
    screen.blit(background_image, (0, 0))  # Draw the background
    screen.blit(swordsman_sprite, (100, 400))  # Position for the swordsman sprite
    screen.blit(archer_sprite, (250, 400))      # Position for the archer sprite
    screen.blit(wizard_sprite, (400, 400))      # Position for the wizard sprite
    screen.blit(goblin_sprite, (550, 400))      # Position for the goblin sprite
    screen.blit(orc_sprite, (700, 400))          # Position for the orc sprite
    screen.blit(dark_wizard_sprite, (850, 400))  # Position for the dark wizard sprite

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
