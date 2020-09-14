from tkinter import *
from PIL import Image,ImageTk

class Demo1:
    
    def __init__(self, master):
        global load
        self.master = master
        self.frame = tkinter.Frame(self.master)

        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)
        
        

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = Tk()
    root.geometry('1920x1080')
    root.configure(bg ="#13254a")
    load = Image.open('boton-05.png')
    render = ImageTk.PhotoImage(load)

    app = Demo1(root)

    root.mainloop()

if __name__ == '__main__':
    main()