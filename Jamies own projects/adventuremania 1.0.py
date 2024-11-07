import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("AdventureMania")

# Colors and Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)


# Function to render text on screen
def draw_text(text, position, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)


# Function for text input
def get_text_input(prompt):
    user_text = ""
    entering_text = True
    while entering_text:
        screen.fill(BLACK)
        draw_text(prompt, (50, 150))
        draw_text(user_text, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Confirm input with Enter
                    entering_text = False
                elif event.key == pygame.K_BACKSPACE:  # Remove last character
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode  # Add new character
    return user_text


# Character creation screen with in-game inputs
def character_creation():
    player_name = get_text_input("Enter your character's name:")

    # Display class options and let player choose
    class_options = ["Swordsman", "Elf Archer", "Wizard"]
    selected_class = 0
    choosing_class = True
    while choosing_class:
        screen.fill(BLACK)
        draw_text("Choose your class (use arrow keys):", (50, 150))

        # Display each class with an arrow indicating the selection
        for i, option in enumerate(class_options):
            color = WHITE if i == selected_class else (100, 100, 100)
            draw_text(option, (50, 200 + i * 40), color)

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
                elif event.key == pygame.K_RETURN:  # Confirm choice
                    choosing_class = False

    player_class = class_options[selected_class]
    return player_name, player_class


# Player setup based on class
def setup_player(player_class):
    if player_class == 'Swordsman':
        return {"health": 100, "attack": 15, "defense": 10, "attacks": {"Sword Strike": 20, "Shield Bash": 10}}
    elif player_class == 'Elf Archer':
        return {"health": 80, "attack": 18, "defense": 8, "attacks": {"Long Bow": 15, "Throw Bomb": 25}}
    elif player_class == 'Wizard':
        return {"health": 70, "attack": 20, "defense": 5, "attacks": {"Fireball": 30, "Ice Blast": 15}}
    else:
        return {"health": 100, "attack": 15, "defense": 10, "attacks": {"Sword Strike": 20, "Shield Bash": 10}}


# Display game info
def display_stats(player_name, player_class, player_level, player_health, player_attack, player_defense):
    screen.fill(BLACK)
    draw_text(f"{player_name} the {player_class}", (50, 50))
    draw_text(f"Level: {player_level} Health: {player_health}", (50, 100))
    draw_text(f"Attack: {player_attack} Defense: {player_defense}", (50, 150))
    pygame.display.flip()


# Enemy creation function
def create_enemy(player_level):
    enemies = [
        {"name": "Goblin", "base_health": 35, "base_attack": 10, "base_defense": 5,
         "attacks": {"Claw Swipe": 8, "Poison Spit": 12}},
        {"name": "Orc", "base_health": 60, "base_attack": 12, "base_defense": 7,
         "attacks": {"Club Smash": 15, "War Cry": 5}},
        {"name": "Dark Wizard", "base_health": 50, "base_attack": 15, "base_defense": 3,
         "attacks": {"Shadow Bolt": 20, "Curse": 10}}
    ]
    enemy = random.choice(enemies)
    enemy['health'] = int(enemy['base_health'] * (1 + player_level * 0.1))
    enemy['attack'] = int(enemy['base_attack'] * (1 + player_level * 0.1))
    enemy['defense'] = int(enemy['base_defense'] * (1 + player_level * 0.1))
    return enemy


# Combat function with Pygame selection
def combat(player, player_level):
    enemy = create_enemy(player_level)
    screen.fill(BLACK)
    draw_text(f"A wild {enemy['name']} appears!", (50, 200))
    pygame.display.flip()
    pygame.time.delay(2000)

    # Combat loop
    while player["health"] > 0 and enemy["health"] > 0:
        screen.fill(BLACK)
        draw_text(f"Player Health: {player['health']}   Enemy Health: {enemy['health']}", (50, 100))

        # Display player's attack choices with selection
        attack_list = list(player["attacks"].keys())
        selected_attack = 0
        attack_chosen = False
        while not attack_chosen:
            screen.fill(BLACK)
            draw_text("Choose your attack (use arrow keys):", (50, 150))
            for i, attack in enumerate(attack_list):
                color = WHITE if i == selected_attack else (100, 100, 100)
                draw_text(f"{attack} (Power: {player['attacks'][attack]})", (50, 200 + i * 40), color)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_attack = (selected_attack + 1) % len(attack_list)
                    elif event.key == pygame.K_UP:
                        selected_attack = (selected_attack - 1) % len(attack_list)
                    elif event.key == pygame.K_RETURN:
                        attack_chosen = True

        chosen_attack = attack_list[selected_attack]
        attack_power = player["attacks"][chosen_attack]

        # Player attack calculation
        player_roll = random.randint(1, 20) + attack_power
        enemy_roll = random.randint(1, 20) + enemy['defense']
        if player_roll > enemy_roll:
            damage = player_roll - enemy_roll
            enemy['health'] -= damage
            draw_text(f"{chosen_attack} hits {enemy['name']} for {damage}!", (50, 350))
        else:
            draw_text("Your attack missed!", (50, 350))

        # Enemy attack calculation
        enemy_attack = random.choice(list(enemy['attacks'].keys()))
        enemy_attack_power = enemy['attacks'][enemy_attack]
        enemy_roll = random.randint(1, 20) + enemy_attack_power
        player_roll = random.randint(1, 20) + player["defense"]
        if enemy_roll > player_roll:
            damage = enemy_roll - player_roll
            player["health"] -= damage
            draw_text(f"{enemy['name']} used {enemy_attack} and dealt {damage}!", (50, 400))
        else:
            draw_text(f"The {enemy['name']}'s attack missed!", (50, 400))

        pygame.display.flip()
        pygame.time.delay(1500)  # Pause for readability

        if player["health"] <= 0:
            draw_text("You have been defeated! Game Over.", (50, 450))
            pygame.display.flip()
            pygame.time.delay(2000)
            break
        elif enemy['health'] <= 0:
            draw_text(f"You defeated the {enemy['name']}!", (50, 450))
            pygame.display.flip()
            pygame.time.delay(2000)
            return True  # Victory

    return False  # Defeat


# Main game setup
player_name, player_class = character_creation()
player = setup_player(player_class)
player["name"] = player_name
player_level = 1

# Game loop
running = True
while running:
    display_stats(player_name, player_class, player_level, player["health"], player["attack"], player["defense"])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    victory = combat(player, player_level)
    if victory:
        player_level += 1
        player["health"] = int(player["health"] * 1.1)
        player["attack"] = int(player["attack"] * 1.1)
        player["defense"] = int(player["defense"] * 1.1)
    else:
        break  # End the game if defeated

pygame.quit()
