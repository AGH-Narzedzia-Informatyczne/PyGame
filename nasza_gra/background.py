import pygame
from pygame import mixer

pygame.mixer.init()

mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(0.05)
mixer.music.play(-1)
while pygame.mixer.music.get_busy(): pygame.time.Clock().tick(10)
