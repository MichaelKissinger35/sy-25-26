import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  

    enemy_pos[1] += enemy_speed
  
    if enemy_pos[1] > HEIGHT:
        # The enemy should go back to the top with a new X position
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")
  
    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True


    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()


# Function to apply screen shake
def screen_shake(intensity):
    return random.randint(-intensity, intensity), random.randint(-intensity, intensity)

shake_intensity = 100  # Intensity of the shake
shake_duration = 1   # Duration of the shake in frames

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  

    enemy_pos[1] += enemy_speed
  
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")

        # Trigger a brief screen shake on a "near miss"
        shake_intensity = 5
        shake_duration = 10

    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True

        # Trigger a stronger screen shake on game over
        shake_intensity = 10
        shake_duration = 20

    # Apply screen shake if active
    if shake_duration > 0:
        offset_x, offset_y = screen_shake(shake_intensity)
        shake_duration -= 1
    else:
        offset_x, offset_y = 0, 0

    # Drawing with screen shake offset
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0] + offset_x, enemy_pos[1] + offset_y, enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0] + offset_x, player_pos[1] + offset_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()# Function to apply screen shake
def screen_shake(intensity):
    return random.randint(-intensity, intensity), random.randint(-intensity, intensity)

shake_intensity = 0  # Intensity of the shake
shake_duration = 0   # Duration of the shake in frames

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  

    enemy_pos[1] += enemy_speed
  
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")


        shake_intensity = 5
        shake_duration = 10

    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True

        # Trigger a stronger screen shake on game over
        shake_intensity = 10
        shake_duration = 20

    # Apply screen shake if active
    if shake_duration > 0:
        offset_x, offset_y = screen_shake(shake_intensity)
        shake_duration -= 1
    else:
        offset_x, offset_y = 0, 0

    # Drawing with screen shake offset
    screen.fill((0, 0, 0))
    
    # Apply the offset to the entire screen rendering
    screen.blit(screen, (offset_x, offset_y))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()



import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50
player_speed = 40

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 25

score = 0
game_over = False

# Trail properties
trail_length = 10
trail = []

# Function to apply screen shake
def screen_shake(intensity):
    return random.randint(-intensity, intensity), random.randint(-intensity, intensity)

shake_intensity = 0  # Intensity of the shake
shake_duration = 0   # Duration of the shake in frames

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  

    enemy_pos[1] += enemy_speed

    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        print(f"Score: {score}")

        shake_intensity = 5
        shake_duration = 10

    if (enemy_pos[0] < player_pos[0] + player_size and
        enemy_pos[0] + enemy_size > player_pos[0] and
        enemy_pos[1] < player_pos[1] + player_size and
        enemy_pos[1] + enemy_size > player_pos[1]):
        print("Game Over!")
        game_over = True

        shake_intensity = 10
        shake_duration = 20

    # Apply screen shake if active
    if shake_duration > 0:
        offset_x, offset_y = screen_shake(shake_intensity)
        shake_duration -= 1
    else:
        offset_x, offset_y = 0, 0

    # Update trail
    trail.append(tuple(player_pos))
    if len(trail) > trail_length:
        trail.pop(0)

    # Drawing with screen shake offset
    screen.fill((0, 0, 0))

    # Draw enemy
    pygame.draw.rect(screen, RED, (enemy_pos[0] + offset_x, enemy_pos[1] + offset_y, enemy_size, enemy_size))

    # Draw player trail (motion blur)
    for i, pos in enumerate(trail):
        alpha = int(255 * (i + 1) / trail_length * 0.5)  # Fading alpha
        trail_surf = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
        trail_surf.fill((0, 0, 255, alpha))
        screen.blit(trail_surf, (pos[0] + offset_x, pos[1] + offset_y))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_pos[0] + offset_x, player_pos[1] + offset_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
if enemy_pos[1] > HEIGHT:
    enemy_pos[1] = 0
    enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
    score += 1
    print(f"Score: {score}")

    # Player grows in size (up to a max)
    player_size = min(player_size + 50, 1500)

    # Enemy speed fluctuates between 5 and 20
    enemy_speed = random.randint(5, 20)

    shake_intensity = 5
    shake_duration = 10
