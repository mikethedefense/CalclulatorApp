import sympy
from tkinter import *

def solve(eq):
    eq = '(' + eq.split('=')[0] + ')-(' + eq.split('=')[1] + ')'
    ans = eval('sympy.solve(eq)')
    answerEntry.delete(0, END)
    answerEntry.insert(100000, str(ans))

root = Tk()
root.title("Equation Solver")
titleLabel = Label(root, text='Equation Solver')
titleLabel.grid(column=1, row=1)
eqLabel = Label(root, text='Enter equation here:')
eqLabel.grid(column=1, row=2)
eqEntry = Entry(root)
eqEntry.grid(column=2, row=2)
answerLabel = Label(root, text='Answer:')
answerLabel.grid(column=1, row=3)
answerEntry = Entry(root)
answerEntry.grid(column=2, row=3)
solveButton = Button(root, text='Solve (use x as unknown)', command=lambda: solve(eqEntry.get()))
solveButton.grid(column=1, row=4)
root.mainloop()
    
