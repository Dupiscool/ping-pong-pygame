import pygame
from pathlib import Path
import main

# Pathing

assests_path = Path(__file__).parent/ "assests"
main_menu_assests = assests_path/ "Menu"

# Sprites

title_ping_pong = pygame.image.load(main_menu_assests / "title_ping_pong.png")
title_ping_pong_scaled = pygame.transform.scale_by(title_ping_pong,3)
title_ping_pong_rect = title_ping_pong_scaled.get_rect()
title_ping_pong_rect.center = (640,160)
play_button = pygame.image.load(main_menu_assests/"play.png")
play_button_rect = pygame.Rect(540,400,214,84)
play_button_rect.center = (640,400)
play_dark_button = pygame.image.load(main_menu_assests/"play_dark.png")
quit_button = pygame.image.load(main_menu_assests/"quit .png")
quit_button_rect = pygame.Rect(540,550,214,84)
quit_button_rect.center = (640,500)
quit_dark_button = pygame.image.load(main_menu_assests/"quit_dark.png")
vs_comp = pygame.image.load(main_menu_assests/"vs_comp.png")
vs_comp_rect = pygame.Rect(540,400,214,84)
vs_comp_rect.center = (640,400)
vs_comp_dark = pygame.image.load(main_menu_assests/"vs_comp_dark.png")
vs_frnd = pygame.image.load(main_menu_assests/"vs_frnd.png")
vs_frnd_rect = pygame.Rect(540,400,214,84)
vs_frnd_rect.center = (640,500)
vs_frnd_dark = pygame.image.load(main_menu_assests/"vs_frnd_dark.png")
mode_normal = pygame.image.load(main_menu_assests/"mode_normal.png")
mode_normal_rect = pygame.Rect(540,400,214,84)
mode_normal_rect.center = (640,400)
mode_normal_dark = pygame.image.load(main_menu_assests/"mode_normal_dark.png")
back_button = pygame.image.load(main_menu_assests/ "back.png")
back_button_rect = back_button.get_rect()
back_button_rect.center = (800, 550)
back_button_dark = pygame.image.load(main_menu_assests/"back_dark.png")

menu_state = "menu_1"

def main_menu(display, mouse_pos):
  global menu_state

  # Blitz
  

  display.blit(title_ping_pong_scaled,title_ping_pong_rect)
  if menu_state == 'menu_1':
    if play_button_rect.collidepoint(mouse_pos) == True:
        display.blit(play_dark_button,play_button_rect)
    if play_button_rect.collidepoint(mouse_pos) == False:
        display.blit(play_button,play_button_rect)
    if quit_button_rect.collidepoint(mouse_pos):
        display.blit(quit_dark_button,quit_button_rect)
    else:
        display.blit(quit_button,quit_button_rect)

  if menu_state == 'menu_2':
    if vs_comp_rect.collidepoint(mouse_pos):
       display.blit(vs_comp_dark,vs_comp_rect)
    else:
       display.blit(vs_comp,vs_comp_rect)
    if vs_frnd_rect.collidepoint(mouse_pos):
       display.blit(vs_frnd_dark,vs_frnd_rect)
    else:
       display.blit(vs_frnd,vs_frnd_rect)
    if back_button_rect.collidepoint(mouse_pos):
       display.blit(back_button_dark,back_button_rect)
    else:
       display.blit(back_button,back_button_rect)

  if menu_state == 'menu_3':
     if mode_normal_rect.collidepoint(mouse_pos):
        display.blit(mode_normal_dark,mode_normal_rect)
     else:
        display.blit(mode_normal,mode_normal_rect)
     if back_button_rect.collidepoint(mouse_pos):
       display.blit(back_button_dark,back_button_rect)
     else:
       display.blit(back_button,back_button_rect)

# Event Handler

def event_handler(event,mouse_pos):
   global menu_state
   if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if menu_state == 'menu_1':
         if play_button_rect.collidepoint(mouse_pos):
           menu_state = 'menu_2'
         elif quit_button_rect.collidepoint(mouse_pos):
           return "quit"

            
        elif menu_state == 'menu_2':
         if vs_comp_rect.collidepoint(mouse_pos):
            menu_state = 'menu_3'
            return "vs_comp"
         if back_button_rect.collidepoint(mouse_pos):
            menu_state = "menu_1"
         if vs_frnd_rect.collidepoint(mouse_pos):
           menu_state = 'menu_3'
           return "vs_frnd"          
        elif menu_state == 'menu_3':
           if mode_normal_rect.collidepoint(mouse_pos):
              menu_state = 'menu_1'
              return "game_normal"
           if back_button_rect.collidepoint(mouse_pos):
             menu_state = "menu_2"


