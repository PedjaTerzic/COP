'''
    This script was written in python 3.x.
    In order to run this script, please make sure your python version is 3.x or above.
    How to run:
        python COP.py
    or if it doesn't work use this one:
        python3 COP.py
    Author: Pedja <pedja.terzic@hotmail.com>
'''

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry

class Cop(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("COP")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global num
        num = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Enter a number :", width=13)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=num)
        entry1.pack(fill=X, padx=5, expand=True)

        
        frame2 = Frame(self)
        frame2.pack(fill=X)

        result = Label(frame2, textvariable=res, width=22)
        result.pack(side=LEFT, padx=86, pady=5)

		
        frame3 = Frame(self)
        frame3.pack(fill=X)

        btntest = Button(frame3, text="Test", width=8, command=self.test)
        btntest.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclear = Button(frame3, text="Clear", width=8, command=self.clear)
        btnclear.pack(side=LEFT, anchor=N, padx=5, pady=5)
		
        btnclose = Button(frame3, text="Close", width=8, command=self.quit)
        btnclose.pack(side=LEFT, anchor=N, padx=5, pady=5)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Something went wrong! Maybe invalid entries')
        
    

    def test(self):
        try:
            n = int(num.get())
            s=0
            for k in range(1,n):
                s=s+pow(2**k-1,n-1,2**n-1)
            if s%(2**n-1)==n:
                value=str(n) + " is prime"
                res.set(self.makeAsItIs(value))
            else:
                value=str(n) + " is composite"
                res.set(self.makeAsItIs(value))
          
        except:
            self.errorMsg('error')
			
    def clear(self):
        try:
            res.set('')
            num.set('')
        except:
            self.errorMsg('error')
			
    
    def makeAsItIs(self, value):
        return value

def main():
    root = Tk()
    root.geometry("300x100")
    cop = Cop(root)
    root.mainloop()

if __name__ == '__main__':
    main()
