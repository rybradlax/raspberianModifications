# Import the Necessary Packages
import pygame
import time
# Start the player
pygame.mixer.init()
while True:
    try:
        in1 = input("Insert mp3 file or playable file here (provide the file pathway to the file, then the file itself): ")
        pygame.mixer.music.load(in1)
        pygame.mixer.music.play()
        in2 = input("Press enter to redo: ")
    except:
        print("Insert a proper playable file")
        pass
