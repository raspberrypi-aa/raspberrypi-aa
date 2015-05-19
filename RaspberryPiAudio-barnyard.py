# must be run as superuser (e.g. "sudo python barnyard.py")
import time

# must init the display to use the mixer
import pygame
pygame.init()

# initialize the mixer for 22KHz stereo
import pygame.mixer
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)

# make sounds you would hear in a barnyard
bird = pygame.mixer.Sound("/usr/share/scratch/Media/Sounds/Animal/Bird.wav")
bird.set_volume(0.3)
bird.play(loops=6)

time.sleep(1.0)
duck = pygame.mixer.Sound("/usr/share/scratch/Media/Sounds/Animal/Duck.wav")
duck.play(loops=4)

time.sleep(0.5)
horse = pygame.mixer.Sound("/usr/share/scratch/Media/Sounds/Animal/Horse.wav")
horse.play()

time.sleep(0.5)
goose = pygame.mixer.Sound("/usr/share/scratch/Media/Sounds/Animal/Goose.wav")
goose.play(loops=2)

# don't exit until sounds have enough time to play
time.sleep(4)
