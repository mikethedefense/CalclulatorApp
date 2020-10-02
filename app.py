from tkinter import *
from tkinter import messagebox
import logging

__version__ = '1.00' 

logging.basicConfig(level = logging.DEBUG)

class CalculatorApp:
    def __init__(self, master):
        # Variables
        self.master = master
        self.answer = 0
        self.number = []
        self.operation = ''
        self.btns = []

        # Title and Geometry
        master.title("Calculator")
        master.geometry("400x700")
        master.resizable(False, False)
       
       # Entry
        self.answer_entry = Entry(master, textvariable = self.answer)
        self.answer_entry.grid(column = 2, row = 0, pady = 5, ipady = 10, ipadx = 20) 
        self.answer_entry.get() 
        
        # Buttons
        self.exit_button = Button(master, text = "Exit", pady = 20, padx = 20, command = master.quit) 
        self.exit_button.grid(row = 2, column = 0) 
        self.clear_button = Button(master, text = "CE", padx = 20, pady = 20, command = self.clear_entry)
        self.clear_button.grid(row = 2, column = 1)
        self.plus_button = Button(master, text = "+", command = self.add)
        self.plus_button.grid(row = 2, column = 8, ipadx = 25, ipady = 25)
        self.subtract_button = Button(master, text = "-", command = self.subtract)
        self.subtract_button.grid(row = 3, column = 8, ipadx = 25, ipady = 25)
        self.multiply_button = Button(master, text = "x", command = self.multiply)
        self.multiply_button.grid(row = 4, column = 8, ipadx = 25, ipady = 25)
        self.divide_button = Button(master, text = "÷", command = self.divide)
        self.divide_button.grid(row = 5, column = 8, ipadx = 25, ipady = 25)
        self.equals_button = Button(master, text = "=", command = self.equals)
        self.equals_button.grid(row = 6, column = 8, ipadx = 25, ipady = 25)

        # Enabled and disabled
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        
        for i in range(10):
            def _handler(n=i): 
                self.insert_number(n)
            btn = Button(master, text=str(i), command=_handler)
            btn.grid(row=3+i//2, column=i%2, ipadx=25, ipady=25)
            self.btns.append(btn)  
    
    # Methods
    def add(self):
        """
        Method that will add numbers
        """
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.answer_entry.delete(0, END)
        self.operation += '+'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def subtract(self):
        """
        Method that will subtract numbers
        """
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.answer_entry.delete(0, END)
        self.operation += '-'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def multiply(self):
        """
        Method that will multiply numbers
        """
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.answer_entry.delete(0, END)
        self.operation += '*'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = NORMAL
        logging.debug(self.operation)
        
    def divide(self):
        """
        Method that will divide numbers
        """
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.answer_entry.delete(0, END)
        self.operation += '/'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def equals(self):
        """
        Method that will print the answer value number out on the calculator and in logging
        """
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.answer_entry.delete(0, END)
        try:
            self.answer = eval(self.operation)
        except:
            self.answer = 'Invalid Syntax'
            messagebox.showerror("Error", self.answer) 
        self.answer_entry.insert(0, self.answer)
        
        logging.debug(self.answer) 

    def clear_entry(self): 
        """
        Method that will clear numbers in the entry
        """
        self.answer_entry.delete(0, END)
        self.operation = ""
        self.number.clear() 
    
    def insert_number(self, num):
        """
        Method that will insert a number to the entry
        """
        self.answer_entry.insert(10000, num)
        self.number.append(num) 
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.equals_button["state"] = NORMAL
        logging.debug(self.number) 

# Start Program
root = Tk()
logging.debug("Program Started") 
instance = CalculatorApp(root)
root.mainloop()
logging.debug("Exit") 
