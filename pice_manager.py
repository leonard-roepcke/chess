import pygame
import pice

class Pice_manager():
    def __init__(self, screen):
        self.pices = []
        self.screen = screen

    def add_pice(self, pice):
        self.pices.append(pice)

    def update(self):
        for i in self.pices:
            i.update()
    
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
