from tkinter import *
from PIL import Image,ImageTk

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		#Setup Menu
		
		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)
		
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class StartPage():
	def __init__(self, parent, controller):
		

		root = Tk()
		root.geometry('1920x1080')
                root.configure(bg ="#13254a")

                load = Image.open('boton-05.png')
                render = ImageTk.PhotoImage(load)
                image = Label(root, image = render)
                image.place(x = 318, y = 200)
                boton = PhotoImage(file = 'boton-01v290px.png')
                b = Button(root, image = boton, borderwidth = 0)
                b.place(x = 915, y = 600)

                botonoffmain =  PhotoImage(file = 'boton-0330px2.png')
                b2 = Button(root, image = botonoffmain , borderwidth = 0, command = root.destroy)
                b2.place(x = 1800, y = 10)

class PageOne(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text="Page One")
		label.pack(padx=10, pady=10)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_two = Button(self, text="Page Two", command=lambda:controller.show_frame(PageTwo))
		page_two.pack()

class PageTwo(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text="Page Two")
		label.pack(padx=10, pady=10)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()




app = App()
app.mainloop()