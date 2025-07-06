import pygame

def get_keys(key):
    keys_presed = {
        "w": 0,
        "a": 0,
        "s": 0,
        "d": 0,
        "+": 0,
        "-": 0,
    }
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        keys_presed["w"] = 1
    if keys[pygame.K_a]:
        keys_presed["a"] = 1
    if keys[pygame.K_s]:
        keys_presed["s"] = 1
    if keys[pygame.K_d]:
        keys_presed["d"] = 1
    if keys[pygame.K_PLUS]:
        keys_presed["+"] = 1
    if keys[pygame.K_MINUS]:
        keys_presed["-"] = 1

    return keys_presed[key]