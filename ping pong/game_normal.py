import pygame
from pathlib import Path
import main
import random

# Pathing

assests_path = Path(__file__).parent/ "assests"
game_path = assests_path/ "game"

# Sprites

sprite_ball = pygame.image.load(game_path/ "Ball.png")
sprite_ball_rect = sprite_ball.get_rect()
sprite_ball_rect.center = (640,320)
digits_sprite = pygame.image.load(game_path/ "digits.png")
paddle_sprite_left = pygame.image.load(game_path/ "paddle.png")
paddle_sprite_left_rect = paddle_sprite_left.get_rect()
paddle_sprite_left_rect.center = (200,320)
digits_sprite_2 = digits_sprite.copy()
paddle_sprite_right = pygame.transform.flip(paddle_sprite_left, True, False)
paddle_sprite_right_rect = paddle_sprite_right.get_rect()
paddle_sprite_right_rect.center = (1080,320)
p2_win_sprite = pygame.image.load(game_path/"p2wins_gif.png")
p1_win_sprite = pygame.image.load(game_path/"p1wins_gif.png")

# For C O M P

check_zone = pygame.Rect(560, 0, 720, 640)
random_dead_zone = pygame.Rect(950, 0, 280, 640)

# Other Stuff

game_normal_comp_running = False
game_normal_frnd_running = False
k = 1
j = 1
n = 4
score_right = 0
score_left = 0
frame = 0
last_update = pygame.time.get_ticks()
just_hit = False
rdz_code = 0
def game_normal_frnd(display):
    global game_normal_frnd_running
    global j
    global k
    global score_right
    global score_left
    global frame
    global last_update
    global n
    left_line = pygame.draw.line(display, (255, 255, 255), (180, 0), (180, 640), 2)
    right_line = pygame.draw.line(display, (255, 255, 255), (1100, 0), (1100, 640), 2)
    

    keys = pygame.key.get_pressed()

    if not game_normal_frnd_running and score_right < 9 and score_left < 9:
     if keys[pygame.K_SPACE]:          
          game_normal_frnd_running = True
    if score_left >= 9 or score_right >= 9:
       game_normal_frnd_running = False
       if keys[pygame.K_SPACE]:
           score_right = 0
           score_left = 0
           main.main("main_menu")
    
    # Inputs    

    if keys[pygame.K_w] and paddle_sprite_left_rect.top > 0:
        paddle_sprite_left_rect.centery -= 4
    if keys[pygame.K_s] and paddle_sprite_left_rect.bottom <= 640:
        paddle_sprite_left_rect.centery += 4
    if keys[pygame.K_UP] and paddle_sprite_right_rect.top > 0:
        paddle_sprite_right_rect.centery -= 4
    if keys[pygame.K_DOWN] and paddle_sprite_right_rect.bottom <= 640:
        paddle_sprite_right_rect.centery += 4
   
# Game Core

    if game_normal_frnd_running:      
           sprite_ball_rect.centerx += k * n
           sprite_ball_rect.centery += j * n
           if sprite_ball_rect.top <= 0:
                j = +1
           if sprite_ball_rect.bottom >= 640:
                sprite_ball_rect.bottom = 640
                j = -1  
           if sprite_ball_rect.colliderect(left_line):
                score_right += 1     
                n = 4
                game_normal_frnd_running = False

                sprite_ball_rect.center = (640,320)
           if sprite_ball_rect.colliderect(right_line):
                score_left += 1     
                n = 4
                game_normal_frnd_running = False
                sprite_ball_rect.center = (640,320)
           if sprite_ball_rect.colliderect(paddle_sprite_left_rect):
                k = +1
                n += 1
           if sprite_ball_rect.colliderect(paddle_sprite_right_rect):
                k = -1
                n += 1

# Victory Gif

    if score_left == 9:
       display.blit(p1_win_sprite.subsurface((0, frame * 72, 360, 72)), (460, 120))
       if pygame.time.get_ticks() - last_update >= 1000:
        frame += 1
        last_update = pygame.time.get_ticks()

        if frame >= 2:
            frame = 0

    if score_right == 9:
       display.blit(p2_win_sprite.subsurface((0, frame * 72, 360, 72)), (460, 120))
       if pygame.time.get_ticks() - last_update >= 1000:
        frame += 1
        last_update = pygame.time.get_ticks()

        if frame >= 2:
            frame = 0


# Blitz 
   
    display.blit(paddle_sprite_right,paddle_sprite_right_rect)
    display.blit(paddle_sprite_left,paddle_sprite_left_rect)
    display.blit(sprite_ball,sprite_ball_rect) 
    display.blit(digits_sprite, (50,50), (score_left * 16, 0, 12, 20))
    display.blit(digits_sprite_2, (1220,50), (score_right * 16, 0, 12, 20))

# Spain without S

def game_normal_comp(display):
    global game_normal_comp_running
    global j
    global k
    global score_right
    global score_left
    global frame
    global last_update
    global just_hit
    global n
    global rdz_code
    debug_mode = False
    left_line = pygame.draw.line(display, (255, 255, 255), (180, 0), (180, 640), 2)
    right_line = pygame.draw.line(display, (255, 255, 255), (1100, 0), (1100, 640), 2)
    dead_zone = pygame.Rect(paddle_sprite_right_rect.left - 50, paddle_sprite_right_rect.top - 10, 50, paddle_sprite_right_rect.height + 10)

    keys = pygame.key.get_pressed()

    if not game_normal_comp_running and score_right < 9 and score_left < 9:
     if keys[pygame.K_SPACE]:          
          rdz_code = 0
          game_normal_comp_running = True
    if score_left >= 9 or score_right >= 9:
       game_normal_comp_running = False
       if keys[pygame.K_SPACE]:
           score_right = 0
           score_left = 0
           main.main("main_menu")
    
    # P1 Inputs    

    if keys[pygame.K_w] and paddle_sprite_left_rect.top > 0:
        paddle_sprite_left_rect.centery -= 4
    if keys[pygame.K_s] and paddle_sprite_left_rect.bottom <= 640:
        paddle_sprite_left_rect.centery += 4

    # The C O M P
    if paddle_sprite_right_rect.top <= 0:
        paddle_sprite_right_rect.top = 0
    if paddle_sprite_right_rect.bottom >= 640:
        paddle_sprite_right_rect.bottom = 640
    if sprite_ball_rect.colliderect(dead_zone) == False:
      if sprite_ball_rect.colliderect(check_zone) and just_hit == False:
            if paddle_sprite_right_rect.centery < sprite_ball_rect.centery:
                 paddle_sprite_right_rect.centery += 4
            if paddle_sprite_right_rect.centery > sprite_ball_rect.centery:
                 paddle_sprite_right_rect.centery -= 4
    if sprite_ball_rect.colliderect(random_dead_zone) and rdz_code == 10:
        just_hit = True
    if debug_mode == True:
        pygame.draw.rect(display, (255, 0, 0), dead_zone, 2)
        pygame.draw.rect(display, (255, 0, 0), random_dead_zone, 2)
           
    
    # Game Core 2

    if game_normal_comp_running:      
           sprite_ball_rect.centerx += k * 4
           sprite_ball_rect.centery += j * 4
           if sprite_ball_rect.top <= 0:
                j = +1
           if sprite_ball_rect.bottom >= 640:
                sprite_ball_rect.bottom = 640
                j = -1  
           if sprite_ball_rect.colliderect(left_line):
                score_right += 1
                just_hit = False   
                n = 4  
                game_normal_comp_running = False
                sprite_ball_rect.center = (640,320)
           if sprite_ball_rect.colliderect(right_line):
                score_left += 1     
                just_hit = False
                n = 4
                game_normal_comp_running = False
                sprite_ball_rect.center = (640,320)
           if sprite_ball_rect.colliderect(paddle_sprite_left_rect):
                k = +1
                n += 1
                just_hit = False
                rdz_code = random.randint(1,10)
           if sprite_ball_rect.colliderect(paddle_sprite_right_rect):
                k = -1
                n += 1
                just_hit = True
                rdz_code = random.randint(1,10)
                
           
                            


    # Victory Gif (Im not making another sprite for comp winning)

    if score_left == 9:
       display.blit(p1_win_sprite.subsurface((0, frame * 72, 360, 72)), (460, 120))
       if pygame.time.get_ticks() - last_update >= 1000:
        frame += 1
        last_update = pygame.time.get_ticks()

        if frame >= 2:
            frame = 0

    if score_right == 9:
       display.blit(p2_win_sprite.subsurface((0, frame * 72, 360, 72)), (460, 120))
       if pygame.time.get_ticks() - last_update >= 1000:
        frame += 1
        last_update = pygame.time.get_ticks()

        if frame >= 2:
            frame = 0
    
    # Blitz 2
   
    display.blit(paddle_sprite_right,paddle_sprite_right_rect)
    display.blit(paddle_sprite_left,paddle_sprite_left_rect)
    display.blit(sprite_ball,sprite_ball_rect) 
    display.blit(digits_sprite, (50,50), (score_left * 16, 0, 12, 20))
    display.blit(digits_sprite_2, (1220,50), (score_right * 16, 0, 12, 20))
    