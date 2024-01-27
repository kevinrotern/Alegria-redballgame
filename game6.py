import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Red Ball')
clock = pygame.time.Clock()

test_font = pygame.font.Font('PixelColeco-4vJW.ttf', 20)
sky_surface = pygame.image.load('sprite/sky.jpg')
ground_surface = pygame.image.load('sprite/ground.jpg')

# Resize image
sky_surface = pygame.transform.scale(sky_surface, (800, 300))
ground_surface = pygame.transform.scale(ground_surface, (800, 100))

text_surface = test_font.render('Score: 0', False, 'Black')
score = 0

slime_surface = pygame.image.load('sprite\slimeWalk2.png')
slime_rect = slime_surface.get_rect(midbottom=(750, 300))

bird_surface = pygame.image.load('sprite/bird1.png')
bird_surface = pygame.transform.scale(bird_surface, (50, 50))
bird_rect = bird_surface.get_rect(midbottom=(750, 250))
#s
ball_x_pos,ball_y_pos=80,300
player_surf = pygame.image.load('sprite/redball.png')
player_surf = pygame.transform.scale(player_surf, (40, 40))
player_rect = player_surf.get_rect(midbottom=(ball_x_pos, ball_y_pos))

# Player variables
player_speed = 4
jumping = False
y_gravity=1
jump_height=20
y_velocity=jump_height

game_over = False
times=0
turn=0
FPS=50
score_speed=0
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        jumping=True

    if jumping==True:
        ball_y_pos -= y_velocity
        print("first: ",ball_y_pos,y_velocity)
        y_velocity -=y_gravity
        print("first: ",y_gravity,y_velocity)
        if y_velocity < -jump_height:
            jumping= False
            y_velocity =jump_height
        player_rect=player_surf.get_rect(midbottom=(ball_x_pos, ball_y_pos))
        screen.blit(player_surf,player_rect)
    else:
        player_rect=player_surf.get_rect(midbottom=(ball_x_pos, ball_y_pos))
        screen.blit(player_surf,player_rect)


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Update and draw the score
    score += 0.4
    text_surface = test_font.render(f'Score: {int(score)}', False, 'Black')
    screen.blit(text_surface, (350, 30))

    # Update and draw the speed
    if turn%3 != 0:
     if score-score_speed <= 300:
      slime_rect.x -= player_speed
     else:
        score_speed=score
        player_speed+=2
     if slime_rect.right < 0:
        slime_rect.left = 800 
        turn +=1
     screen.blit(slime_surface, slime_rect)
    else:
     bird_rect.x -= player_speed
     if bird_rect.right < 0:
        bird_rect.left = 800
        turn +=1
     screen.blit(bird_surface, bird_rect)
     
   
    # Check for collision
    if player_rect.colliderect(slime_rect) or player_rect.colliderect(bird_rect):
        game_over_text = test_font.render('Game Over!', False, 'Red')
        restart_text = test_font.render('Press R to Restart', False, 'Black')


        screen.blit(game_over_text, (340, 120))
        screen.blit(restart_text, (300, 170))
        
        pygame.display.update()  # Update the display to show the "Game Over!" text

        # Wait for the user to press 'R' to restart
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    waiting_for_restart = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Restart the game
                    player_rect = player_surf.get_rect(midbottom=(80, 300))
                    slime_rect = slime_surface.get_rect(midbottom=(750, 300))
                    bird_rect = bird_surface.get_rect(midbottom=(750, 280))
                    score = 0
                    game_over = False
                    waiting_for_restart = False

    else:
        print('1')

    # Draw the player
    screen.blit(player_surf, player_rect)

    pygame.display.update()
    clock.tick(FPS)



