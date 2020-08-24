

from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from subprocess import call
import os

root = Tk()
root.geometry('1920x1080')
root.configure(bg ="#13254a")

def open_file():
    os.system('SEGUNDAPAGINA.py')
    
load = Image.open('boton-05.png')
render = ImageTk.PhotoImage(load)
image = Label(root, image = render)
image.place(x = 318, y = 200)
boton = PhotoImage(file = 'boton-01v290px.png')
b = Button(root, image = boton, borderwidth = 0, command = open_file)
b.place(x = 915, y = 600)


    

botonoffmain =  PhotoImage(file = 'boton-0330px2.png')
b2 = Button(root, image = botonoffmain , borderwidth = 0, command = root.destroy)
b2.place(x = 1800, y = 10)



    
root.mainloop()











