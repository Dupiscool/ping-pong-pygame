import pygame
from pathlib import Path
import menu 
import game_normal
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((1280,640))
pygame.display.set_caption("Ping Pong")
global state
state = "main_menu"
def main(state):
   state = "main_menu"
   running = True
   mouse_pos = pygame.mouse.get_pos()
   while running:

# Rendering Part 1

    display.fill((0,0,0))

# Event Manager

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu_result = menu.event_handler(event, mouse_pos)
        if menu_result == "quit": 
           running = False
        if menu_result == 'vs_comp':
           game_type = "vs_comp"
        if menu_result == 'vs_frnd':
           game_type = "vs_frnd"
        if menu_result == "game_normal":
           if game_type == 'vs_comp':
              state = "game_normal_comp"
           if game_type == 'vs_frnd':
              state = 'game_normal_frnd'
            

    mouse_pos = pygame.mouse.get_pos()

# Rendering Part 2

    if state == "main_menu":
        menu.main_menu(display, mouse_pos)
    if state == "game_normal_frnd":
       game_normal.game_normal_frnd(display)
    if state == "game_normal_comp":
       game_normal.game_normal_comp(display)
    pygame.display.flip()
    clock.tick(60)  


   



if __name__ == "__main__":
    main(state)