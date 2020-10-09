from tkinter import *
from tkinter import messagebox
import logging
import math

__version__ = '1.45' 

logging.basicConfig(level = logging.DEBUG)

class CalculatorApp:
    def __init__(self, master):
        # Variables
        self.master = master
        self.answer = 0
        self.number = []
        self.operation = ''
        self.btns = []
        self.multiply_stuff = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","math.pi","math.e", ")") # Stuff you can multiply without the multiply sign
        
        # Title and Geometry
        master.title("Calculator")
        master.geometry("800x900")
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
        self.delete_button = Button(master, text = "Del", padx = 20, pady = 20, command = self.delete_entry)
        self.delete_button.grid(row = 2, column = 2, sticky=W)
        self.plus_button = Button(master, text = "+", command = self.add, font = ("Helvetica", 15, "bold"))
        self.plus_button.grid(row = 2, column = 8, ipadx = 25, ipady = 25)
        self.subtract_button = Button(master, text = "-", command = self.subtract, font = ("Helvetica", 15, "bold"))
        self.subtract_button.grid(row = 3, column = 8, ipadx = 25, ipady = 25)
        self.multiply_button = Button(master, text = "x", command = self.multiply, font = ("Helvetica", 15, "bold"))
        self.multiply_button.grid(row = 4, column = 8, ipadx = 25, ipady = 25)
        self.divide_button = Button(master, text = "÷", command = self.divide, font = ("Helvetica", 15, "bold"))
        self.divide_button.grid(row = 5, column = 8, ipadx = 25, ipady = 25)
        self.equals_button = Button(master, text = "=", command = self.equals, font = ("Helvetica", 15, "bold"))
        self.equals_button.grid(row = 9, column = 9, ipadx = 25, ipady = 25)
        self.left_bracket_button = Button(master, text = "(", command = lambda: self.insert_bracket("("), font = ("Helvetica", 15, "bold"))
        self.left_bracket_button.grid(row = 4, column = 9, ipadx = 25, ipady = 25)
        self.right_bracket_button = Button(master, text = ")", command = lambda: self.insert_bracket(")"), font = ("Helvetica", 15, "bold"))
        self.right_bracket_button.grid(row = 5, column = 9, ipadx = 25, ipady = 25)
        self.power_button = Button(master, text = "^", command = self.power, font = ("Helvetica", 15, "bold"))
        self.power_button.grid(row = 2, column = 9, ipadx = 25, ipady = 25)
        self.sqrt_button = Button(master, text = "√", command = self.sqrt, font = ("Helvetica", 15, "bold"))
        self.sqrt_button.grid(row = 3, column = 9, ipadx = 25, ipady = 25)
        self.pi_button = Button(master, text = "π", command = self.pie, font = ("Helvetica", 15, "bold"))
        self.pi_button.grid(row = 8, column = 8, ipadx = 25, ipady = 25)
        self.e_button = Button(master, text = "e", command = self.e, font = ("Helvetica", 15, "bold")) 
        self.e_button.grid(row = 8, column = 9, ipadx = 25, ipady = 25)
        self.sin_button = Button(master, text = "sin", command = self.sin, font = ("Helvetica", 15, "bold"))
        self.sin_button.grid(row = 6, column = 8, ipadx = 15, ipady = 25)
        self.cosine_button = Button(master, text = "cos", command = self.cosine, font = ("Helvetica", 15, "bold")) 
        self.cosine_button.grid(row = 6, column = 9, ipadx = 25, ipady = 25)
        self.tangent_button = Button(master, text = "tan", command = self.cosine, font = ("Helvetica", 15, "bold")) 
        self.tangent_button.grid(row = 6, column = 10, ipadx = 25, ipady = 25)
        self.inverse_sine_button = Button(master, text = "sin-1", command = self.inverse_sine, font = ("Helvetica", 15, "bold"))
        self.inverse_sine_button.grid(row = 7, column = 8, ipadx = 15, ipady = 25)
        self.inverse_cosine_button = Button(master, text = "cos-1", command = self.inverse_cosine, font = ("Helvetica", 15, "bold"))
        self.inverse_cosine_button.grid(row = 7, column = 9, ipadx = 15, ipady = 25)
        self.inverse_tangent_button = Button(master, text = "tan-1", command = self.inverse_tangent, font = ("Helvetica", 15, "bold"))
        self.inverse_tangent_button.grid(row = 7, column = 10, ipadx = 15, ipady = 25)
        self.log_button = Button(master, text = "log", command = self.log, font = ("Helvetica", 15, "bold"))
        self.log_button.grid(row = 9, column = 8, ipadx = 25, ipady = 25)
        self.ans_button = Button(master, text = "Ans", command = self.ans, font = ("Helvetica", 15, "bold"))
        self.ans_button.grid(row = 8, column = 1, ipadx = 25, ipady = 25)
        
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
        self.delete_button["state"] = DISABLED
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
    
    def ans(self):
        """
        Method that takes the previous answer and does something with it on the screen
        """
        self.answer_entry.insert(10000, "ans")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += '*'
            self.operation += str(self.answer) 
        else:
            self.operation += str(self.answer) 
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.equals_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        self.delete_button["state"] = NORMAL

    def clear_entry(self): 
        """
        Method that will clear numbers in the entry
        """
        self.answer_entry.delete(0, END)
        self.operation = ""
        self.number.clear()
        
    def delete_entry(self): 
        """
        Method that will delete numbers in the entry
        """
        if len(self.number) > 0:
            del self.number[-1]
            logging.debug(self.number)
        else:
            self.operation = self.operation[:-1]
        self.answer_entry.delete(len(self.answer_entry.get())-1, END)
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.equals_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
    
    def insert_number(self, num):
        """
        Method that will insert a number to the entry
        """
        self.answer_entry.insert(10000, num)
        if self.operation.endswith(self.multiply_stuff) and not len(self.number) > 0: 
            self.number.append("*") 
            self.number.append(num) 
        else:
            self.number.append(num)
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.equals_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        self.delete_button["state"] = NORMAL
        logging.debug(self.number) 
        logging.debug(self.operation)
    
    def insert_bracket(self, bracket):
        """
        Method that deals with brackets
        """
        self.answer_entry.insert(10000, bracket)
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff) and bracket == "(": 
            self.operation += "*" 
            self.operation += bracket 
        else:
            self.operation += bracket
    
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
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.sqrt(" 
        else:
            self.operation += "math.sqrt(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
        
    def pie(self):
        """
        Method for constant pi
        """
        self.answer_entry.insert(10000, "π")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.pi" 
        else:
            self.operation += "math.pi" 
        self.equals_button["state"] = NORMAL
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def e(self):
        """
        Method for constant e
        """
        self.answer_entry.insert(10000, "e")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.e" 
        else:
            self.operation += "math.e" 
        self.equals_button["state"] = NORMAL
        self.plus_button["state"] = NORMAL
        self.subtract_button["state"] = NORMAL
        self.multiply_button["state"] = NORMAL
        self.divide_button["state"] = NORMAL
        self.power_button["state"] = NORMAL
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def sin(self):
        """
        Method that will sin numbers
        """
        self.answer_entry.insert(10000, "sin(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.sin(" 
        else:
            self.operation += "math.sin(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def cosine(self):
        """
        Method for cosine trig function
        """
        self.answer_entry.insert(10000, "cos(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.cos(" 
        else:
            self.operation += "math.cos(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def tangent(self):
        """
        Method for tangent trig function
        """
        self.answer_entry.insert(10000, "tan(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.tan(" 
        else:
            self.operation += "math.tan(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def inverse_sine(self):
        """
        Method for inverse sine trig function
        """
        self.answer_entry.insert(10000, "sin-1(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.asin(" 
        else:
            self.operation += "math.asin(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def inverse_cosine(self):
        """
        Method for inverse cosine trig function
        """
        self.answer_entry.insert(10000, "cos-1(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.acos(" 
        else:
            self.operation += "math.acos(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)

    def inverse_tangent(self):
        """
        Method for inverse tangent trig function
        """
        self.answer_entry.insert(10000, "tan-1(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.atan(" 
        else:
            self.operation += "math.atan(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
    
    def log(self):
        """
        Method that will deal with logs
        """
        self.answer_entry.insert(10000, "log(")
        self.operation += "".join([str(i) for i in self.number])
        self.number.clear()
        if self.operation.endswith(self.multiply_stuff): 
            self.operation += "*math.log10(" 
        else:
            self.operation += "math.log10(" 
        self.plus_button["state"] = DISABLED
        self.subtract_button["state"] = DISABLED
        self.multiply_button["state"] = DISABLED
        self.divide_button["state"] = DISABLED
        self.equals_button["state"] = DISABLED
        self.power_button["state"] = DISABLED
        self.delete_button["state"] = NORMAL
        logging.debug(self.operation)
        
# Start Program
root = Tk()
logging.debug("Program Started") 
instance = CalculatorApp(root)
root.mainloop()
logging.debug("Exit") 
