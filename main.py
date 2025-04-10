import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)
BLACK= (0,0,0)       
FONTSIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

font = pygame.font.Font(None, FONTSIZE)
choices= ["rock", "paper", "scissors"]

def get_winner(player, computer):
          if player == computer:
              return "It's a tie!"
          elif (player=="rock" and computer == "scissors") or \
                    (player=="paper"and computer == "rock") or \
                    (player=="scissors"and computer == "paper"):
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
                                if event.key==pygame.K_r:
                                        player_choice="rock"
                                elif event.key ==pygame.K_p:
                                        player_choice="paper"
                                elif event.key==pygame.K_s:
                                        player_choice="scissors"
                                if player_choice:
                                        computer_choice=random.choice(choices)
                                        result=get_winner(player_choice,computer_choice)

                screen.fill(WHITE)
                if player_choice:
                                player_text=font.render(f"you choose:{player_choice}",True,BLACK)
                                computer_text=font.render(f"computer choose:{computer_choice}",True,BLACK)

                                result_text=font.render(result,True,BLACK)
                                screen.blit(player_text,(50,50))
                                screen.blit(computer_text,(50,100))
                                screen.blit(result_text,(50,150))
                                
                pygame.display.flip()
                pygame.time.Clock().tick(FPS)
        pygame.quit()

if __name__=="__main__":
        main()

                                
               
                                
                        
                                                 
                                                            
    