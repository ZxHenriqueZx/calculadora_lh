from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculadora")
        master.geometry("457x535+0+0")
        master.resizable(False, False)
        master.config(bg='gray')

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17,bg='#ccddff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)
        
        Button(width=9,height=4,text='(',relief='flat',bg='white',command=lambda:self.show('(')).place(x=0,y=60)
        Button(width=9,height=4,text=')',relief='flat',bg='white',command=lambda:self.show(')')).place(x=90,y=60)
        Button(width=9,height=4,text='%',relief='flat',bg='white',command=lambda:self.show('%')).place(x=205,y=60)
        Button(width=9,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x=0,y=155)
        Button(width=9,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=90,y=155)
        Button(width=9,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=205,y=155)
        Button(width=9,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0,y=250)
        Button(width=9,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=90,y=250)
        Button(width=9,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x=205,y=250)
        Button(width=9,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0,y=345)
        Button(width=9,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=205,y=345)
        Button(width=9,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=90,y=345)
        Button(width=9,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=90,y=440)
        Button(width=9,height=4,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=205,y=440)
        Button(width=9,height=4,text='+',relief='flat',bg='white',command=lambda:self.show('+')).place(x=330,y=345)
        Button(width=9,height=4,text='-',relief='flat',bg='white',command=lambda:self.show('-')).place(x=330,y=250)
        Button(width=9,height=4,text='/',relief='flat',bg='white',command=lambda:self.show('/')).place(x=330,y=60)
        Button(width=9,height=4,text='x',relief='flat',bg='white',command=lambda:self.show('*')).place(x=330,y=155)
        Button(width=9,height=4,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=330,y=440)
        Button(width=9,height=4,text='C',relief='flat',bg='white',command=self.clear).place(x=0,y=440)

    def show(self, value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()
