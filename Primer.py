import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

D = 2
mole = []
X = []
Y = []


class Moleculas:
    def __init__(self, canvas, x, y, w, h, Yo, tipo, mass = 1, q = -1, Xo = -275, color = 'blue'):
        self.canvas = canvas


        self.x = x
        self.y = y
        self.vel = [0,0]
        self.acc = [0,0]    
        self.body = self.canvas.create_oval(x-w/2, y-h/2, x+w/2, x+h/2, fill = color)
        self.mass = mass
        self.q = q
        self.tipo = tipo
        self.Xo = Xo
        self.Yo = Yo

        self.canvas.move(self.body, -275, Yo)

    def Force(self, Px, Py):
        global D
        self.acc[0] = (self.q*Px)/(self.mass*D)
        self.acc[1] = (self.q*Py)/(self.mass*D)

    def update(self, t, P1, P2):
        self.x, self.y, *c = self.canvas.coords(self.body)

        if self.x < 595:
            self.Force(P1, P2)
            self.vel[0] = self.vel[0] + self.acc[0]*t
            self.vel[1] = self.vel[1] + self.acc[1]*t
            self.canvas.move(self.body, -self.vel[0], self.vel[1])
        else:
            if self.tipo == "S":
                X.append(self.y)
            else:
                Y.append(self.y)

            self.canvas.delete(self.body)





        





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


        


#Vista Lateral
        p1 = self.Can.create_rectangle(0, 0, 120, 1, fill ="black")
        self.Can.move(p1, 50, 220)

        p2 = self.Can.create_rectangle(0, 0, 120, 1, fill ="black")
        self.Can.move(p2, 50, 181)

        p3 = self.Can.create_rectangle(0, 0, 341, 1, fill ="black")
        self.Can.move(p3, 50, 200)

        p4 = self.Can.create_line(120, 0, 341, 129, width = 2)
        self.Can.move(p4, 50, 220)

        p5 = self.Can.create_line(120, 0, 341, -143, width = 2)
        self.Can.move(p5, 50, 181)

        p6 = self.Can.create_line(341, -156, 341, 156)
        self.Can.move(p6, 50, 194)

        p8 = self.Can.create_line(250, 31, 250, 70)
        self.Can.move(p8, -200, 150)

        #Frame para los botones
        W = Frame(self.Can, height = 300, width = 850, bg = "#F0B27A")
        W.place(x = 665, y = 520)

        fontt = tkFont.Font(family = "Century Gothic", size = 10)

        SV = Scale(W, from_=-50, to=50, tickinterval= 50, orient=HORIZONTAL, length=185, bg = '#F0B27A', bd = 0, highlightbackground = '#F0B27A', label = 'Potencial placas verticales', font = fontt)
        SV.set(0)
        SV.place(x = 10, y = 35)


        SH = Scale(W, from_=-50, to=50, tickinterval= 50, orient=HORIZONTAL, length=200, bg = '#F0B27A', bd = 0, highlightbackground = '#F0B27A', label = 'Potencial placas horizontales', font = fontt)
        SH.set(0)
        SH.place(x = 250, y = 35)

        SA = Scale(W, from_=0, to=150, tickinterval= 50, orient=HORIZONTAL, length=185, bg = '#F0B27A', bd = 0, highlightbackground = '#F0B27A', label = 'Potencial Aceleración', font = fontt)
        SA.set(0)
        SA.place(x = 10, y = 120)

#Botones



        

#Bucle de las partículas
        while True:
            try:
                self.root.update()
                Ml = Moleculas(self.Can, 350, 350, 10, 10, -149, "L")
                mole.append(Ml)
                Ms = Moleculas(self.Can, 350, 350, 10, 10, 251, "S")
                mole.append(Ms)

                while True:
                    try:
                        self.root.update()
                        #print("esta")
                        for m in mole:
                            if m.tipo == "S":
                                m.update(0.0000001, SA.get(), SH.get())
                            elif m.tipo == "L":
                                m.update(0.0000001, SA.get(), SV.get())
                    except:
                        break
                mole.clear()
            except:
                break








        self.master.mainloop()














def main():
    app = aplic()
    return(0)
        
if __name__ == '__main__':
    main()
