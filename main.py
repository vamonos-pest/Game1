from tkinter import *
import random as rdm
from PIL import Image, ImageTk

class Game(Frame):
    def __init__(self, root):
        super(Game, self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, image=imageRock, activebackground="PeachPuff2",
                     command=lambda x=1: self.btn_click(x))
        btn2 = Button(root, image=imageScissors, activebackground="PeachPuff2",
                      command=lambda x=2: self.btn_click(x))
        btn3 = Button(root, image=imagePaper, activebackground="PeachPuff2",
                      command=lambda x=3: self.btn_click(x))
        btn4 = Button(root, image=imageLizard, activebackground="PeachPuff2",
                      command=lambda x=4: self.btn_click(x))
        btn5 = Button(root, image=imageSpock, activebackground="PeachPuff2",
                      command=lambda x=5: self.btn_click(x))

        btn.place(x=20, y=110, width=110, height=110)
        btn2.place(x=165, y=110, width=110, height=110)
        btn3.place(x=310, y=110, width=110, height=110)
        btn4.place(x=90, y=250, width=110, height=110)
        btn5.place(x=250, y=250, width=110, height=110)

        self.lbl = Label(root, text="Начало игры!", bg="#FFF", justify="center",font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=500, y=350)

        self.lbl3 = Label(root, text="Соперник выбрал", bg="#FFF", font=("Times New Roman", 16, "bold"))
        self.lbl3.place(x=500, y=23)

        self.lblInstruction = Label(root, image=imageInstruction, bg="#FFF")
        self.lblInstruction.place(x=780, y=25)

        self.win = self.drow = self.lose = 0

        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                          text=f"Победы: {self.win}\nПроигрышы:"
                               f" {self.lose}\nНичьи: {self.drow}",
                          bg="#FFF")
        self.lbl2.place(x=5, y=5)


    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 5)

        if comp_choise == 1:
            self.lblRock = Label(root, image=imageRock, bg="#FFF")
            self.lblRock.place(x=540, y=100)
        elif comp_choise == 2:
            self.lblScissors = Label(root, image=imageScissors, bg="#FFF")
            self.lblScissors.place(x=540, y=100)
        elif comp_choise == 3:
            self.lblPaper = Label(root, image=imagePaper, bg="#FFF")
            self.lblPaper.place(x=540, y=100)
        elif comp_choise == 4:
            self.lblLizard = Label(root, image=imageLizard, bg="#FFF")
            self.lblLizard.place(x=540, y=100)
        else:
            self.lblSpock = Label(root, image=imageSpock, bg="#FFF")
            self.lblSpock.place(x=540, y=100)



        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Ничья", fg="black")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 4 \
                or choise == 4 and comp_choise == 5 \
                or choise == 3 and comp_choise == 1 \
                or choise == 4 and comp_choise == 1 \
                or choise == 5 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Победа", fg="green")
        else:
            self.lose += 1
            self.lbl.configure(text="Проигрыш", fg="red")

        self.lbl2.configure(text=f"Победы: {self.win}\nПроигрышы:"
                                 f" {self.lose}\nНичьи: {self.drow}")

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    imageInstruction = ImageTk.PhotoImage(file="instruction.png")
    imageRock = ImageTk.PhotoImage(file="rock.png")
    imageScissors = ImageTk.PhotoImage(file="scissors.png")
    imagePaper = ImageTk.PhotoImage(file="paper.png")
    imageLizard = ImageTk.PhotoImage(file="lizard.png")
    imageSpock = ImageTk.PhotoImage(file="spock.png")
    root.geometry("1200x450+210+210")
    root.title("Камень, ножницы, бумага, ящерица, спок")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Game(root)
    app.pack()
    root.mainloop()