import pygame

pygame.init()
pygame.mixer.music.load('alarm.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

while True:
    comando = input(
        'Digite "p" para pausar, "r" para voltar, "s" para parar: ')
    if comando == "p":
        pygame.mixer.music.pause()
    elif comando == "r":
        pygame.mixer.music.unpause()
    elif comando == "s":
        pygame.mixer.music.stop()
        break
