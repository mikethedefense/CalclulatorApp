from tkinter import *
from tkinter import messagebox
import logging
import math

__version__ = '1.17' 

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
        master.geometry("470x900")
        master.resizable(False, False)
       
       # Entry
        self.answer_entry = Entry(master, textvariable = self.answer)
        self.answer_entry.grid(column = 2, row = 0, pady = 5, ipady = 10, ipadx = 20) 
        self.answer_entry.get() 
        
        # Buttons
        self.exit_button = Button(master, text = "Exit", pady = 20, padx = 20, command = master.destroy) 
        self.exit_button.grid(row = 2, column = 0) 
        self.clear_button = Button(master, text = "CE", padx = 20, pady = 20, command = self.clear_entry)
        self.clear_button.grid(row = 2, column = 1)
        self.plus_button = Button(master, text = "+", command = self.add, font = ("Helvetica", 15, "bold"))
        self.plus_button.grid(row = 2, column = 8, ipadx = 25, ipady = 25)
        self.subtract_button = Button(master, text = "-", command = self.subtract, font = ("Helvetica", 15, "bold"))
        self.subtract_button.grid(row = 3, column = 8, ipadx = 25, ipady = 25)
        self.multiply_button = Button(master, text = "x", command = self.multiply, font = ("Helvetica", 15, "bold"))
        self.multiply_button.grid(row = 4, column = 8, ipadx = 25, ipady = 25)
        self.divide_button = Button(master, text = "÷", command = self.divide, font = ("Helvetica", 15, "bold"))
        self.divide_button.grid(row = 5, column = 8, ipadx = 25, ipady = 25)
        self.sin_button = Button(master, text = "sin", command = self.sin, font = ("Helvetica", 15, "bold"))
        self.sin_button.grid(row = 6, column = 8, ipadx = 15, ipady = 25)
        self.equals_button = Button(master, text = "=", command = self.equals, font = ("Helvetica", 15, "bold"))
        self.equals_button.grid(row = 6, column = 9, ipadx = 25, ipady = 25)
        self.power_button = Button(master, text = "^", command = self.power, font = ("Helvetica", 15, "bold"))
        self.power_button.grid(row = 2, column = 9, ipadx = 25, ipady = 25)
        self.sqrt_button = Button(master, text = "√", command = self.sqrt, font = ("Helvetica", 15, "bold"))
        self.sqrt_button.grid(row = 3, column = 9, ipadx = 25, ipady = 25)
        self.pi_button = Button(master, text = "π", command = self.pie, font = ("Helvetica", 15, "bold"))
        self.pi_button.grid(row = 7, column = 8, ipadx = 15, ipady = 25)
        self.e_button = Button(master, text = "e", command = self.e, font = ("Helvetica", 15, "bold")) 
        self.e_button.grid(row = 7, column = 9, ipadx = 15, ipady = 25)
        
        for i in range(10):
            def _handler(n=i): 
                self.insert_number(n)
            btn = Button(master, text=str(i), command=_handler)
            btn.grid(row=3+i//2, column=i%2, ipadx=25, ipady=25)
            self.btns.append(btn)  
        
        # Decimal Points
        btn = Button(master, text=str('.'), command=lambda: self.insert_number('.'), font = ("Helvetica", 15, "bold"))
        btn.grid(row=8, column=0, ipadx=25, ipady=25)
        self.btns.append(btn)

        # Brackets
        left_bracket_button = Button(master, text = "(", command = lambda:self.insert_number('('), font = ("Helvetica", 15, "bold"))
        left_bracket_button.grid(row = 4, column = 9, ipadx = 25, ipady = 25)
        right_bracket_button = Button(master, text = ")", command = lambda: self.insert_number(')'), font = ("Helvetica", 15, "bold"))
        right_bracket_button.grid(row = 5, column = 9, ipadx = 25, ipady = 25)
        self.btns.append(left_bracket_button)
        self.btns.append(right_bracket_button) 

        # Enabled and disabled
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        
    # Methods
    def add(self):
        """
        Method that will add numbers
        """
        self.answer_entry.insert(100000, "+")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += '+'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def subtract(self):
        """
        Method that will subtract numbers
        """
        self.answer_entry.insert(100000, "-")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += '-'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def multiply(self):
        """
        Method that will multiply numbers
        """
        self.answer_entry.insert(100000, "×")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += '*'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = NORMAL
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
        
    def divide(self):
        """
        Method that will divide numbers
        """
        self.answer_entry.insert(10000, "÷")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += '/'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
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
        self.power_button["state"] = DISABLED
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        logging.debug(self.operation)
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
        self.power_button["state"] = NORMAL
        logging.debug(self.number) 
    
    def power(self):
        """
        Method that will raise numbers to powers
        """
        self.answer_entry.insert(10000, "^")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += '**'
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
        
    def sqrt(self):
        """
        Method that will square root numbers
        """
        self.answer_entry.insert(10000, "√(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += 'math.sqrt('
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
        
    def sin(self):
        """
        Method that will sin numbers
        """
        self.answer_entry.insert(10000, "sin(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += 'math.sin('
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        logging.debug(self.operation)
    
    def pie(self):
        self.answer_entry.insert(10000, "π")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += 'math.pi'
        self.equals_button["state"] = NORMAL
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def e(self):
        self.answer_entry.insert(10000, "e")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        self.operation += 'math.e'
        self.equals_button["state"] = NORMAL
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        logging.debug(self.operation)

# Start Program
root = Tk()
logging.debug("Program Started") 
instance = CalculatorApp(root)
root.mainloop()
logging.debug("Exit") 
