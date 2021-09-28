import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

D = 2
mole = []


class Moleculas:
	def __init__(self, canvas, x, y, w, h, Yo, mass = 1, q = -1, Xo = -275, color = 'blue'):
		self.canvas = canvas


		self.x = x
		self.y = y
		self.vel = [0,0]
		self.acc = [0,0]	
		self.body = self.canvas.create_oval(x-w/2, y-h/2, x+w/2, x+h/2, fill = color)
		self.mass = mass
		self.q = q

		self.canvas.move(self.body, -275, Yo)

	def Force(self, Px, Py):
		global D
		self.acc[0] = (self.q*Px)/(self.mass*D)
		self.acc[1] = (self.q*Py)/(self.mass*D)

	def update(self, t, P1, P2):
		self.x, self.y, *c = self.canvas.coords(self.body)

		self.Force(P1, P2)

		self.vel[0] = self.vel[0] + self.acc[0]*t
		self.vel[1] = self.vel[1] + self.acc[1]*t

		self.canvas.move(self.body, -self.vel[0], self.vel[1])





		





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


#Vista Superior
        p1 = self.Can.create_rectangle(0, 0, 250, 1, fill ="black")
        self.Can.move(p1, 50, 651)

        p2 = self.Can.create_rectangle(0, 0, 250, 1, fill ="black")
        self.Can.move(p2, 50, 550)

        p3 = self.Can.create_rectangle(0, 0, 550, 1, fill ="black")
        self.Can.move(p3, 50, 600)

        p4 = self.Can.create_line(250, 1, 550, 50, width = 2)
        self.Can.move(p4, 50, 650)

        p5 = self.Can.create_line(250, 1, 550, -50, width = 2)
        self.Can.move(p5, 50, 550)

        p6 = self.Can.create_line(550, -50, 550, 151)
        self.Can.move(p6, 50, 550)

        p8 = self.Can.create_line(250, 0, 250, 101)
        self.Can.move(p8, -200, 550)


        Ms = Moleculas(self.Can, 350, 350, 10, 10, 251)
        mole.append(Ms)


#Vista Lateral
        p1 = self.Can.create_rectangle(0, 0, 250, 1, fill ="black")
        self.Can.move(p1, 50, 251)

        p2 = self.Can.create_rectangle(0, 0, 250, 1, fill ="black")
        self.Can.move(p2, 50, 150)

        p3 = self.Can.create_rectangle(0, 0, 550, 1, fill ="black")
        self.Can.move(p3, 50, 200)

        p4 = self.Can.create_line(250, 1, 550, 50, width = 2)
        self.Can.move(p4, 50, 250)

        p5 = self.Can.create_line(250, 1, 550, -50, width = 2)
        self.Can.move(p5, 50, 150)

        p6 = self.Can.create_line(550, -50, 550, 151)
        self.Can.move(p6, 50, 150)

        p8 = self.Can.create_line(250, 0, 250, 101)
        self.Can.move(p8, -200, 150)


        Ml = Moleculas(self.Can, 350, 350, 10, 10, -149)
        mole.append(Ml)



        while True:
        	self.root.update()
        	print("esta")
        	for m in mole:
        		m.update(.0001, 50, 0)

        self.master.mainloop()














def main():
    app = aplic()
    return(0)
        
if __name__ == '__main__':
    main()
