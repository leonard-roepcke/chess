import pygame
pygame.init()
import pice_manager
import pice

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

board_img = pygame.image.load("assets/board.png").convert_alpha()
board_img = pygame.transform.scale(board_img, (800, 800))

pices = pice_manager.Pice_manager(screen)
pices.add_board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    
    screen.blit(board_img, (100, 100))

    pices.update()

    clock.tick(60)
    pygame.display.flip()