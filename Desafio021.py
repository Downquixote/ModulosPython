# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
# Para iniciar o uso do pygame, utilize:
pygame.init()
# Para usar o mixer, utilize:
pygame.mixer.music.load('santo.mp3') # Não esqueça de adicionar a música a pasta.
# Para iniciar a música, utilize:
pygame.mixer.music.play()
# Para terminar o programa quando a música terminar, utilize:
input()
pygame.event.wait()



