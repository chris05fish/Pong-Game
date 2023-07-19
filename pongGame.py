import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 3
paddle1_x = 20
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 20
paddle2_y = height // 2 - paddle_height // 2

# Set up the ball
ball_radius = 10
ball_speed_x = .75
ball_speed_y = .75
ball_x = width // 2
ball_y = height // 2

# Set up the score variables
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
        paddle2_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Check collision with walls
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Check if ball is out of bounds
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2
        ball_y = height // 2
    if ball_x > width:
        score1 += 1
        ball_x = width // 2
        ball_y = height // 2

    # Clear the window
    window.fill(BLACK)

    # Draw the paddles
    pygame.draw.rect(window, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

    # Draw the scores
    score_text1 = font.render(str(score1), True, WHITE)
    window.blit(score_text1, (width // 4, 20))
    score_text2 = font.render(str(score2), True, WHITE)
    window.blit(score_text2, (width * 3 // 4, 20))
    
    pygame.display.update()