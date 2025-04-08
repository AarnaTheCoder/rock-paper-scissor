import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)       
FONTSIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

font = pygame.font.Font(None, FONTSIZE)
choices= ["rock", "paper", "scissors"]

def get_winner(player_choice, computer_choice):
          if player_choice == computer_choice:
              return "It's a tie!"
          elif (player_choice=="rock" and computer_choice == "scissors") or \
                    (player_choice=="paper"and computer_choice == "rock") or \
                    (player_choice=="scissors"and computer_choice == "paper"):
                      return "You win!"
          else:
                              return "you lose!"
          
def main():
        running=True
        player_choice = None
        computer_choice = None
        result=""
        while running:
                for event in pygame.event.get():
                        if event.type ==pygame.QUIT:
                                running=False
                        if event.type == pygame.KEYDOWN:
                                if event.key==pygame.k.r:
                                        player_choice="rock"
                              elif event.key ==pygame.k.p:
                                        player_choice="paper"
                              elif event.key==pygame.k.s:
                                        player_choice="scissors"
                              if player_choice:
                                computer_choice=random.choice(choices)
                                result=get_winner(player_choice,computer_choice)

                              screen.fill(WHITE)
                        if player_choice:
                                player_text=font.render(f"you choose:{player_choice}",True,computer_choice,true(BLACK))
               
                                
                        
                                                 
                                                            
    