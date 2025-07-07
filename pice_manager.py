import pygame
import pice
from helper import debug
debuger = debug.Debuger()
debuger.start_log()

class Pice_manager():
    def __init__(self, screen):
        self.pices = []
        self.screen = screen
        self.selected_piece = None

    def add_pice(self, pice):
        self.pices.append(pice)

    def update(self):
        for i in self.pices:
            if self.selected_piece == i:
                i.update(select=True)
            else:
                i.update()
        #self.select()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.select_pice(mouse_pos)
        
        debuger.log("seectet pice", f"id:{self.selected_piece}")
    
    def add_board(self):
        
        for x in range(8):
            self.pices.append(pice.Pice(self.screen, "Pawn", pos=(x + 1, 1 + 1), side="player"))

        
        player_back_row = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for x, name in enumerate(player_back_row):
            self.pices.append(pice.Pice(self.screen, name, pos=(x + 1, 0 + 1), side="player"))


        
        for x in range(8):
            self.pices.append(pice.Pice(self.screen, "Pawn", pos=(x + 1, 6 + 1), side="enemy"))

        enemy_back_row = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
        for x, name in enumerate(enemy_back_row):
            self.pices.append(pice.Pice(self.screen, name, pos=(x + 1, 7 + 1), side="enemy"))

    def select_pice(self, mouse):
        mouse = mouse[0], mouse[1] -100
        for i_pice in self.pices:
            if i_pice.check_select(mouse):
                self.selected_piece = i_pice

