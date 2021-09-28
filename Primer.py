import tkinter as tk
from tkinter import *
import tkinter.font as tkFont




class Moleculas:
	def __init__(self, canvas, x, y, w, h, Yo, mass = 0, Xo = -275, color = 'blue'):
		self.canvas = canvas


		self.x = x
		self.y = y
		self.vel = [0,0]
		self.acc = [0,0]	
		self.body = self.canvas.create_oval(x-w/2, y-h/2, x+w/2, x+h/2, fill = color)

		self.canvas.move(self.body, -275, 275)

		





class aplic():
    #Se crea la funición principal
    def __init__(self):
        #Se crea la ventana master. A esta ventana el usuario no tiene acceso por ser la que mantiene el loop del programa
        self.master = Tk()
        self.master.geometry("1x1")
        self.master.withdraw()
        self.root = tk.Toplevel()
        w,h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.resizable(False,False)

        self.Can = Canvas(self.root, bg = 'white', height = h, width = w)
        self.Can.pack()

        p1 = self.Can.create_rectangle(50, 0, 650, 5, fill = 'black')
        self.Can.move(p1, 15, 675)

        p2 = self.Can.create_rectangle(50, 0, 650, 5, fill = 'black')
        self.Can.move(p2, 15, 575)


        m = Moleculas(self.Can, 350, 350, 10, 10, 275)




        self.master.mainloop()














def main():
    app = aplic()
    return(0)
        
if __name__ == '__main__':
    main()