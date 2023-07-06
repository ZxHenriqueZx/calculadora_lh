from tkinter import *


class Calculator:
    def __init__(self, master):
        master.title('Calculadora')
        master.geometry('400x500')
        master.resizable(False, False)
        master.config(bg='gray')

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17,bg='#fff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)


inicial = Tk()
calculator = Calculator(inicial)
inicial.mainloop()
