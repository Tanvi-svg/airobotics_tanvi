from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init(22050,-16,2,512)#library give python control music devices,frquency,no of channels

def play_song(pushbutton):
    music= [pushbutton]
    
    if not pygame.mixer.get_busy():
        music.play()
    
    elif music.get_num_channels():
        music.stop()

b_s= {
    Button(14) : Sound("infinity.mp3"),#key value pair, seperated by comma
    Button(15) : Sound("NG.mp3")
}

for button, sound in b_s.items():
    button.when_pressed= play_song

try:
    pause()

except KeyboardInterrupt:
    for button, sound in b_s.items():
        button.close()
    pygame.mixer.stop()