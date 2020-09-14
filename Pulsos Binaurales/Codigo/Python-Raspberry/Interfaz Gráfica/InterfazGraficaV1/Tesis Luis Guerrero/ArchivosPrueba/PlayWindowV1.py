



from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from subprocess import call
import os
import pygame
from pygame import mixer

root = Tk()
root.geometry('1920x1080')
root.configure(bg ="#13254a")


pygame.init()
pygame.mixer.music.load('Binaural0.ogg')


def play():
##        pygame.mixer.music.play()

    
def pausa():
    pygame.mixer.music.pause()
class
def contador():
    

botonplay = PhotoImage(file = 'boton-01v50px.png')
bplay = Button(root, image = botonplay, borderwidth = 0, command = play)
bplay.place(x = 935, y = 450)


    

botonpausa =  PhotoImage(file = 'boton-0250px.png')
bpause = Button(root, image = botonpausa, borderwidth = 0, command = pausa)
bpause.place(x = 800, y = 450)



    
root.mainloop()
