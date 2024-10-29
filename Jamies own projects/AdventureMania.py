import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
base_path = os.path.dirname(__file__)
background_image = pygame.image.load(os.path.join(base_path, 'images', 'forest_background.jpg'))
background_image = pygame.transform.scale(background_image,
                                          (screen_width, screen_height))  # Scale background to screen size

# Load class sprites
class_sprites = {
    "Swordsman": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'swordsman.png')),
                                        (100, 150)),
    "Brawler": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'brawler.png')), (100, 150)),
    "Wizard": pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'wizard.png')), (100, 150)),
}

# Load enemy images
enemy_size = (100, 150)  # size for enemy sprites
goblin_sprite = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'goblin.png')), enemy_size)
orc_sprite = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'alien.png')), enemy_size)
dark_wizard_sprite = pygame.transform.scale(pygame.image.load(os.path.join(base_path, 'images', 'witch.png')),
                                            enemy_size)

# Initialize font1
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
        {"name": "Orc", "base_health": 60, "base_attack": 12, "base_defense": 7,
         "attacks": {"Ray Gun": 15, "Probe": 5}, "sprite": orc_sprite},
        {"name": "Dark Wizard", "base_health": 50, "base_attack": 15, "base_defense": 3,
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


# Combat function
def combat(player_name, player_class, player_health, player_attack, player_defense, player_attacks, player_level):
    enemy = create_enemy(player_level)
    enemy_sprite = enemy['sprite']
    player_sprite = class_sprites[player_class]  # Get player sprite based on class
    print(f"\nA wild {enemy['name']} appears!")

    while player_health > 0 and enemy['health'] > 0:
        screen.fill((0, 0, 0))  # Clear the screen
        screen.blit(background_image, (0, 0))  # Draw scaled background

        draw_health_bars(player_health, enemy['health'], enemy['base_health'])
        screen.blit(enemy_sprite, (500, 200))  # Draw enemy sprite
        screen.blit(player_sprite, (100, 200))  # Draw player sprite

        # Draw attack options with background
        attack_choices = {}
        if player_class.lower() == 'swordsman':
            attack_choices = {"1": "Sword Strike", "2": "Shield Bash"}
        elif player_class.lower() == 'brawler':
            attack_choices = {"1": "Punch", "2": "Kick"}
        elif player_class.lower() == 'wizard':
            attack_choices = {"1": "Fireball", "2": "Lightning Bolt"}

        # Background for attack menu
        pygame.draw.rect(screen, (50, 50, 50), (80, 80, 300, 150))  # Darker background for visibility
        for idx, (key, attack) in enumerate(attack_choices.items()):
            attack_label = font.render(f"{key}. {attack}", True, (255, 255, 255))
            screen.blit(attack_label, (100, 100 + idx * 40))  # Position attack menu lower on the screen

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return player_health, False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_2):  # Check if either move is selected
                    chosen_attack = attack_choices[str(event.key - pygame.K_1 + 1)]  # Get attack based on key press
                    attack_power = player_attacks[chosen_attack]

                    # Player's attack roll
                    player_roll = roll_dice(20) + attack_power
                    enemy_roll = roll_dice(20) + enemy['defense']
                    if player_roll > enemy_roll:
                        damage = player_roll - enemy_roll
                        enemy['health'] -= damage
                        print(f"{player_name} used {chosen_attack} and dealt {damage} damage!")
                    else:
                        print("Your attack missed!")

                    # Enemy's turn to attack
                    if enemy['health'] > 0:  # Enemy attacks only if it's still alive
                        enemy_attack_name = random.choice(list(enemy['attacks'].keys()))
                        enemy_attack_power = enemy['attacks'][enemy_attack_name]
                        enemy_roll = roll_dice(20) + enemy_attack_power
                        player_roll = roll_dice(20) + player_defense
                        if enemy_roll > player_roll:
                            damage = enemy_roll - player_roll
                            player_health -= damage
                            print(
                                f"{enemy['name']} used {enemy_attack_name} and dealt {damage} damage! Your health is now {player_health}.")
                        else:
                            print(f"{enemy['name']}'s attack missed!")

                # Update display
                pygame.display.flip()

    if player_health <= 0:
        print("You have been defeated!")
        return 0, False  # Player defeated
    return player_health, True  # Player won

# Function to display level-up message
def display_level_up_message(level):
    level_up_text = font.render(f"Congratulations! You leveled up to Level {level}!", True, (255, 255, 0))
    screen.blit(level_up_text, (screen_width // 2 - level_up_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Show the message for 2 seconds


# Main game loop
def main():
    intro_screen()
    player_name = get_player_name()
    player_class = class_selection_screen()

    # Player stats
    player_health = 100
    player_attack = 10
    player_defense = 5
    player_level = 1

    # Define player attacks based on class
    if player_class.lower() == 'swordsman':
        player_attacks = {
            "Sword Strike": 25,  # Increased damage
            "Shield Bash": 15  # Added new attack
        }
    elif player_class.lower() == 'brawler':
        player_attacks = {
            "Punch": 20,  # Increased damage
            "Kick": 20  # Added new attack
        }
    elif player_class.lower() == 'wizard':
        player_attacks = {
            "Fireball": 30,  # Increased damage
            "Lightning Bolt": 10  # Added new attack
        }
    else:
        print("Invalid class! Defaulting to Swordsman.")
        player_attacks = {
            "Sword Strike": 25,
            "Shield Bash": 15
        }

    # Combat loop
    while True:
        player_health, victory = combat(player_name, player_class, player_health, player_attack, player_defense,
                                        player_attacks, player_level)
        if player_health <= 0:
            print("Game Over")
            break
        if victory:
            player_level += 1  # Increase player level after victory
            player_health = 100  # Reset health for next battle
            display_level_up_message(player_level)  # Show level-up message
            print(f"You leveled up! Now at level {player_level}.")


if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()  # Ensure pygame quits after the game ends
