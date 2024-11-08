import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AdventureMania")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
font = pygame.font.Font(None, 36)

# Load Images
background_img = pygame.image.load('forest_background.png').convert()
background_img = pygame.transform.scale(background_img, (800, 600))
intro_background = pygame.image.load('intro_background.png').convert()  # New intro background
intro_background = pygame.transform.scale(intro_background, (800, 600))

character_images = {
    "Knight": pygame.image.load('swordsman.png').convert_alpha(),
    "Brawler": pygame.image.load('brawler.png').convert_alpha(),
    "Wizard": pygame.image.load('wizard.png').convert_alpha(),
}
enemy_images = {
    "Goblin": pygame.image.load('goblin.png').convert_alpha(),
    "Alien": pygame.image.load('Alien.png').convert_alpha(),
    "Witch": pygame.image.load('witch.png').convert_alpha(),
}

# Scale character and enemy images
for key in character_images:
    character_images[key] = pygame.transform.scale(character_images[key], (150, 150))
for key in enemy_images:
    enemy_images[key] = pygame.transform.scale(enemy_images[key], (150, 150))


# Function to render text on screen with black outline
def draw_text(text, position, color=WHITE, outline_color=BLACK, outline_width=2):
    outline_text = font.render(text, True, outline_color)
    screen.blit(outline_text, (position[0] - outline_width, position[1] - outline_width))  # Top-left
    screen.blit(outline_text, (position[0] + outline_width, position[1] - outline_width))  # Top-right
    screen.blit(outline_text, (position[0] - outline_width, position[1] + outline_width))  # Bottom-left
    screen.blit(outline_text, (position[0] + outline_width, position[1] + outline_width))  # Bottom-right
    screen.blit(outline_text, (position[0] - outline_width, position[1]))  # Left
    screen.blit(outline_text, (position[0] + outline_width, position[1]))  # Right
    screen.blit(outline_text, (position[0], position[1] - outline_width))  # Top
    screen.blit(outline_text, (position[0], position[1] + outline_width))  # Bottom
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)


# Function to draw health bars
def draw_health_bar(current_health, max_health, position, bar_width=200, bar_height=20):
    health_ratio = current_health / max_health
    health_bar_width = int(bar_width * health_ratio)
    pygame.draw.rect(screen, RED, (*position, bar_width, bar_height))  # Background bar
    pygame.draw.rect(screen, GREEN, (*position, health_bar_width, bar_height))  # Current health


# Function to display the intro screen
def intro_screen():
    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(intro_background, (0, 0))  # Display intro background
        draw_text("WELCOME TO ADVENTUREMANIA!", (210, 250))
        draw_text("Press any key to start", (290, 350))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                return  # Proceed to the next screen when a key is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return  # Proceed to the next screen when the mouse is clicked


# Function for text input
def get_text_input(prompt):
    user_text = ""
    entering_text = True
    while entering_text:
        screen.fill(BLACK)
        screen.blit(intro_background, (0, 0))
        draw_text(prompt, (250, 150))
        draw_text(user_text, (370, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    entering_text = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
    return user_text


# Character creation screen with images
def character_creation():
    player_name = get_text_input("Enter your character's name:")
    class_options = ["Knight", "Brawler", "Wizard"]
    selected_class = 0
    choosing_class = True
    while choosing_class:
        screen.fill(BLACK)
        screen.blit(intro_background, (0, 0))
        draw_text("Choose your class (use arrow keys):", (220, 150))

        # Display class options and highlight the selected one
        for i, option in enumerate(class_options):
            color = WHITE if i == selected_class else (100, 100, 100)
            draw_text(option, (300, 220 + i * 40), color)

        # Show selected character image
        screen.blit(character_images[class_options[selected_class]], (450, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_class = (selected_class + 1) % len(class_options)
                elif event.key == pygame.K_UP:
                    selected_class = (selected_class - 1) % len(class_options)
                elif event.key == pygame.K_RETURN:
                    choosing_class = False

    player_class = class_options[selected_class]
    return player_name, player_class


# Player setup based on class
def setup_player(player_class):
    if player_class == 'Knight':
        return {"health": 100, "max_health": 100, "attack": 15, "defense": 10,
                "attacks": {"Sword Strike": 20, "Shield Bash": 10}}
    elif player_class == 'Brawler':
        return {"health": 80, "max_health": 80, "attack": 18, "defense": 8, "attacks": {"Punch": 15, "Kick": 25}}
    elif player_class == 'Wizard':
        return {"health": 70, "max_health": 70, "attack": 20, "defense": 5,
                "attacks": {"Fireball": 30, "Ice Blast": 15}}
    else:
        return {"health": 100, "max_health": 100, "attack": 15, "defense": 10,
                "attacks": {"Sword Strike": 20, "Shield Bash": 10}}


# Function to show the transition screen when an enemy appears
def enemy_appears_screen():
    screen.fill(BLACK)
    draw_text(f"One day.. {player_name} is walking through a magical forest.", (100, 200))
    draw_text("An enemy appears out of nowhere and attacks!!", (115, 250))
    draw_text("Press any key to continue...", (230, 500))

    pygame.display.flip()

    # Wait for player input before continuing to combat
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_input = False  # Proceed to the combat screen


# Display player stats with background and character image
def display_stats(player, player_name, player_class, player_level):
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    screen.blit(character_images[player_class], (500, 150))
    draw_text(f"{player_name} the {player_class}", (50, 50))
    draw_text(f"Level: {player_level} Health: {player['health']}", (50, 100))
    draw_text(f"Attack: {player['attack']} Defense: {player['defense']}", (50, 150))
    pygame.display.flip()


# Enemy creation
def create_enemy(player_level):
    enemies = [
        {"name": "Goblin", "base_health": 35, "base_attack": 10, "base_defense": 5,
         "attacks": {"Claw Swipe": 8, "Poison Spit": 12}},
        {"name": "Alien", "base_health": 60, "base_attack": 12, "base_defense": 7,
         "attacks": {"Ray Gun": 15, "Probe": 5}},
        {"name": "Witch", "base_health": 50, "base_attack": 15, "base_defense": 3,
         "attacks": {"Hex": 20, "Curse": 10}}
    ]
    enemy = random.choice(enemies)
    enemy['health'] = enemy['max_health'] = int(enemy['base_health'] * (1 + player_level * 0.1))
    enemy['attack'] = int(enemy['base_attack'] * (1 + player_level * 0.1))
    enemy['defense'] = int(enemy['base_defense'] * (1 + player_level * 0.1))
    return enemy


# Combat with enemy images and attack options
def combat(player, player_level):
    enemy = create_enemy(player_level)
    player_actions = list(player['attacks'].keys())
    selected_action = 0
    choosing_action = True

    while player["health"] > 0 and enemy["health"] > 0:
        screen.fill(BLACK)
        screen.blit(background_img, (0, 0))
        screen.blit(character_images[player["class"]], (75, 300))
        screen.blit(enemy_images[enemy["name"]], (470, 350))  # Show the correct enemy image

        # Draw health bars
        draw_health_bar(player["health"], player["max_health"], (100, 50))
        draw_health_bar(enemy["health"], enemy["max_health"], (500, 50))

        # Display health text
        draw_text(f"Player Health: {player['health']}", (100, 20))
        draw_text(f"Enemy Health: {enemy['health']}", (500, 20))

        if choosing_action:
            # Display available attacks and highlight selected one
            draw_text("Choose your attack:", (35, 450))
            for i, action in enumerate(player_actions):
                color = WHITE if i == selected_action else (100, 100, 100)
                draw_text(action, (70, 485 + i * 40), color)
        else:
            # Display attack and damage outcome
            player_damage = player["attacks"][player_actions[selected_action]]
            enemy["health"] -= max(player_damage - enemy["defense"], 0)
            draw_text(f"{player['name']} used {player_actions[selected_action]}!", (280, 200))
            pygame.display.flip()
            pygame.time.delay(1000)

            if enemy["health"] > 0:
                enemy_damage = enemy["attack"]
                player["health"] -= max(enemy_damage - player["defense"], 0)
                draw_text(f"{enemy['name']} attacks for {enemy_damage} damage!", (250, 250))
                pygame.display.flip()
                pygame.time.delay(1000)

            choosing_action = True  # Reset to choose action again

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and choosing_action:
                if event.key == pygame.K_DOWN:
                    selected_action = (selected_action + 1) % len(player_actions)
                elif event.key == pygame.K_UP:
                    selected_action = (selected_action - 1) % len(player_actions)
                elif event.key == pygame.K_RETURN:
                    choosing_action = False

    return player["health"] > 0


# Main setup and game loop
intro_screen()  # Show intro screen first
player_name, player_class = character_creation()
player = setup_player(player_class)
player["name"] = player_name
player["class"] = player_class
player_level = 1

# New screen added here before combat starts
enemy_appears_screen()  # New screen added here

running = True
while running:
    display_stats(player, player_name, player_class, player_level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    victory = combat(player, player_level)
    if victory:
        player_level += 1
        player["health"] = min(player["max_health"], int(player["health"] * 1.1))
        player["attack"] = int(player["attack"] * 1.1)
        player["defense"] = int(player["defense"] * 1.1)
    else:
        break

pygame.quit()
