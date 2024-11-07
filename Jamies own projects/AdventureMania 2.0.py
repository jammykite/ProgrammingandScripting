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
background_size = (1280, 720)  # screen size
swordsman_size = (100, 150)  # size for the swordsman sprite
archer_size = (100, 150)  # size for the archer sprite
wizard_size = (100, 150)  # size for the wizard sprite
enemy_size = (100, 150)  # size for enemy sprites

# Load images
base_path = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(base_path, 'images', 'forest_background.jpg'))
swordsman_sprite = pygame.image.load(os.path.join(base_path, 'images', 'swordsman.png'))
archer_sprite = pygame.image.load(os.path.join(base_path, 'images', 'brawler.png'))
wizard_sprite = pygame.image.load(os.path.join(base_path, 'images', 'wizard.png'))

# Load enemy images
goblin_sprite = pygame.image.load(os.path.join(base_path, 'images', 'goblin.png'))
orc_sprite = pygame.image.load(os.path.join(base_path, 'images', 'alien.png'))
dark_wizard_sprite = pygame.image.load(os.path.join(base_path, 'images', 'witch.png'))

# Scale images to desired sizes
background_image = pygame.transform.scale(background_image, background_size)
swordsman_sprite = pygame.transform.scale(swordsman_sprite, swordsman_size)
archer_sprite = pygame.transform.scale(archer_sprite, archer_size)
wizard_sprite = pygame.transform.scale(wizard_sprite, wizard_size)

# Scale enemy images
goblin_sprite = pygame.transform.scale(goblin_sprite, enemy_size)
orc_sprite = pygame.transform.scale(orc_sprite, enemy_size)
dark_wizard_sprite = pygame.transform.scale(dark_wizard_sprite, enemy_size)

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)


# Function to display intro screen
def intro_screen():
    screen.fill((0, 0, 0))
    title_text = font.render("Welcome to AdventureMania!", True, (255, 255, 255))
    new_game_text = font.render("Press Enter to Start a New Game", True, (255, 255, 255))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 50))
    screen.blit(new_game_text, (screen_width // 2 - new_game_text.get_width() // 2, screen_height // 2 + 10))
    pygame.display.flip()

    # Wait for user to press Enter
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    waiting = False


# Function to get player name
def get_player_name():
    player_name = ""
    while True:
        screen.fill((0, 0, 0))
        name_text = font.render(f"Enter your character name: {player_name}", True, (255, 255, 255))
        screen.blit(name_text, (screen_width // 2 - name_text.get_width() // 2, screen_height // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    if player_name:  # Ensure name is not empty
                        return player_name
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]  # Remove last character
                else:
                    player_name += event.unicode  # Add character


# Function to select class
def class_selection_screen():
    classes = ["Swordsman", "Brawler", "Wizard"]
    selected_class = None

    while selected_class is None:
        screen.fill((0, 0, 0))
        title_text = font.render("Choose your class:", True, (255, 255, 255))
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, screen_height // 2 - 100))

        for index, player_class in enumerate(classes):
            class_text = font.render(f"{index + 1}. {player_class}", True, (255, 255, 255))
            screen.blit(class_text,
                        (screen_width // 2 - class_text.get_width() // 2, screen_height // 2 - 50 + index * 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    selected_class = classes[int(event.key) - pygame.K_1]

    return selected_class


# Function to simulate dice roll
def roll_dice(sides=6):
    return random.randint(1, sides)


# Create an enemy and scale its stats based on player level
def create_enemy(player_level):
    enemies = [
        {"name": "Goblin", "base_health": 35, "base_attack": 10, "base_defense": 5,
         "attacks": {"Claw Swipe": 8, "Poison Spit": 12}, "sprite": goblin_sprite},
        {"name": "Alien", "base_health": 60, "base_attack": 12, "base_defense": 7,
         "attacks": {"Ray Gun": 15, "Probe": 5}, "sprite": orc_sprite},
        {"name": "Witch", "base_health": 50, "base_attack": 15, "base_defense": 3,
         "attacks": {"Hex": 20, "Curse": 10}, "sprite": dark_wizard_sprite}
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


# Function to draw the text box
def draw_text_box(messages):
    pygame.draw.rect(screen, (0, 0, 0), (100, 400, 1080, 200))  # Draw the text box background
    for i, message in enumerate(messages):
        text_surface = font.render(message, True, (255, 255, 255))
        screen.blit(text_surface, (110, 410 + i * 30))  # Spacing between messages


# Combat function
def combat(player_name, player_class, player_health, player_attack, player_defense, player_attacks, player_level):
    enemy = create_enemy(player_level)
    enemy_sprite = enemy['sprite']
    print(f"\nA wild {enemy['name']} appears!")
    messages = []

    # Load player sprite based on class
    if player_class.lower() == 'swordsman':
        player_sprite = swordsman_sprite
    elif player_class.lower() == 'brawler':
        player_sprite = archer_sprite
    elif player_class.lower() == 'wizard':
        player_sprite = wizard_sprite

    while player_health > 0 and enemy['health'] > 0:
        # Display choices
        messages.append("Choose your attack: ")
        messages.append(f"1. {list(player_attacks.keys())[0]}")
        messages.append(f"2. {list(player_attacks.keys())[1]}")
        draw_text_box(messages)

        pygame.display.flip()

        chosen_attack = None
        attack_power = 0  # Default value for attack_power to avoid UnboundLocalError

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return player_health, False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    chosen_attack = list(player_attacks.keys())[0]
                    attack_power = player_attacks[chosen_attack]
                elif event.key == pygame.K_2:
                    chosen_attack = list(player_attacks.keys())[1]
                    attack_power = player_attacks[chosen_attack]

        # Proceed only if an attack was chosen
        if chosen_attack:
            # Player's turn
            player_roll = roll_dice(20) + player_attack
            enemy_roll = roll_dice(20) + enemy['defense']
            if player_roll > enemy_roll:
                damage = player_roll - enemy_roll + attack_power
                enemy['health'] -= damage
                messages.append(
                    f"{player_name} used {chosen_attack} and hit the {enemy['name']}, dealing {damage} damage! Enemy health is now {enemy['health']}."
                )
            else:
                messages.append("Your attack missed!")

            # Check if enemy is defeated
            if enemy['health'] <= 0:
                messages.append(f"You defeated the {enemy['name']}!")
                draw_text_box(messages)
                pygame.display.flip()
                pygame.time.delay(2000)
                return player_health, True  # Return True indicating victory

            # Enemy's turn - Randomly choose an attack
            enemy_attack = random.choice(list(enemy['attacks'].keys()))
            enemy_damage = enemy['attacks'][enemy_attack]
            player_health -= enemy_damage
            messages.append(
                f"The {enemy['name']} used {enemy_attack} and dealt {enemy_damage} damage! Your health is now {player_health}."
            )

            draw_text_box(messages)
            pygame.display.flip()
            pygame.time.delay(2000)
            messages.clear()  # Clear messages for the next round

    if player_health <= 0:
        messages.append("You have been defeated!")
        draw_text_box(messages)
        pygame.display.flip()
        pygame.time.delay(2000)
        return 0, False  # Player defeated


# Main function
def main():
    intro_screen()
    player_name = get_player_name()
    player_class = class_selection_screen()

    player_health = 100
    player_attack = 15
    player_defense = 10
    player_level = 1

    if player_class == "Swordsman":
        player_attacks = {"Slash": 20, "Parry": 10}
    elif player_class == "Brawler":
        player_attacks = {"Punch": 15, "Uppercut": 25}
    elif player_class == "Wizard":
        player_attacks = {"Fireball": 30, "Magic Shield": 10}

    player_health, victory = combat(player_name, player_class, player_health, player_attack, player_defense,
                                    player_attacks, player_level)

    if victory:
        print(f"Congratulations, {player_name}! You've won the battle!")
    else:
        print("Game Over. Try again!")


if __name__ == "__main__":
    main()
