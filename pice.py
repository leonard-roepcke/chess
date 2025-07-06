import pygame
from helper import debug


class Pice():
    def __init__(self,screen, typ="Pawn", side="enemy", pos=(1, 1)):
        self.typ = typ
        self.side = side
        self.pos = pos
        self.screen = screen
        self.pice_image = self.load_image(self.side, self.typ)
    
    def avalible_pices(self):
        print("Pawn")

    def load_image(self, side, typ):
        if side == "enemy":
            match self.typ:
                case "Pawn":
                    self.pice_image = pygame.image.load("assets/B_Pawn.png").convert_alpha()
                case "Rook":
                    self.pice_image = pygame.image.load("assets/B_Rook.png").convert_alpha()
                case "Knight":
                    self.pice_image = pygame.image.load("assets/B_Knight.png").convert_alpha()
                case "Bishop":
                    self.pice_image = pygame.image.load("assets/B_Bishop.png").convert_alpha()
                case "Queen":
                    self.pice_image = pygame.image.load("assets/B_Queen.png").convert_alpha()
                case "King":
                    self.pice_image = pygame.image.load("assets/B_King.png").convert_alpha()
                
        elif side == "player":
            match self.typ:
                case "Pawn":
                    self.pice_image = pygame.image.load("assets/W_Pawn.png").convert_alpha()
                case "Rook":
                    self.pice_image = pygame.image.load("assets/W_Rook.png").convert_alpha()
                case "Knight":
                    self.pice_image = pygame.image.load("assets/W_Knight.png").convert_alpha()
                case "Bishop":
                    self.pice_image = pygame.image.load("assets/W_Bishop.png").convert_alpha()
                case "Queen":
                    self.pice_image = pygame.image.load("assets/W_Queen.png").convert_alpha()
                case "King":
                    self.pice_image = pygame.image.load("assets/W_King.png").convert_alpha()
                
        else:
            debuger.log_force("", "Nutze etweder enemy oder player als Name für die seite eines pices")

        return self.pice_image

    def update(self):
        self.draw()

    def draw(self):
        x = 150 + ((self.pos[0] - 1.08) * 91)
        y = 950 - ((self.pos[1] + 2.12) * 91)
        print(x, ",", y)
        
        
        self.pice_image = pygame.transform.scale(self.pice_image, (80, 160))
        self.screen.blit(self.pice_image, (x, y))
