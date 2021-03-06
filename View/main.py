__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

from CommonAssets.main import Button as btn
from CommonAssets.main import DESIRE_GEOMETRY
from CommonAssets.main import TITLE
from tkinter import *


from tkinter import Button
from tkinter import Entry
from tkinter import END


class CalculatorGUI:

    def __init__(self, master, controller):

        self.master = master
        self.master.title(TITLE)
        self.master.geometry(DESIRE_GEOMETRY)
        self.master.resizable(width=False, height=False)  # window resizable
        self.controller = controller
        self.entry = Entry(master)
        self.entry.grid(row=0, column=0, columnspan=12, sticky= W+E)
        self.entry.focus_set()
        self.entry.bind('<KeyPress>', self.controller.keyPressed)
        self.degtoradBtnToggle=False

        #UI desing
        offsetRow=0
        row1=1
        row2=2
        row3=3
        row4=4

        offsetColumn=0
        column0=0 + offsetColumn
        column1=1 + offsetColumn
        column2=2 + offsetColumn
        column3=3 + offsetColumn
        column4=4 + offsetColumn
        column5=5 + offsetColumn
        column6=6 + offsetColumn

        #Numbers and Constants
        Button(self.master, text="7", width=6, command=lambda: self.controller.inputVal(7)).grid(row=3, column=column0)
        Button(self.master, text="4", width=6, command=lambda: self.controller.inputVal(4)).grid(row=4, column=column0)
        Button(self.master, text="1", width=6, command=lambda: self.controller.inputVal(1)).grid(row=5, column=column0)
        Button(self.master, text="8", width=6, command=lambda: self.controller.inputVal(8)).grid(row=3, column=column1)
        Button(self.master, text="5", width=6, command=lambda: self.controller.inputVal(5)).grid(row=4, column=column1)
        Button(self.master, text="2", width=6, command=lambda: self.controller.inputVal(2)).grid(row=5, column=column1)
        Button(self.master, text="0", width=6, command=lambda: self.controller.inputVal(0)).grid(row=6, column=column0)
        Button(self.master, text="9", width=6, command=lambda: self.controller.inputVal(9)).grid(row=3, column=column2)
        Button(self.master, text="6", width=6, command=lambda: self.controller.inputVal(6)).grid(row=4, column=column2)
        Button(self.master, text="3", width=6, command=lambda: self.controller.inputVal(3)).grid(row=5, column=column2)
        Button(self.master, text="e", width=6, command=lambda: self.controller.inputVal(controller.e())).grid(row=1, column=column0)
        Button(self.master, text="π", width=6, command=lambda: self.controller.inputVal(controller.pi())).grid(row=1, column=column1)


        # Math Functions
        Button(self.master, text="+", width=6, command=lambda: self.controller.inputVal('+')).grid(row=5, column=column3)
        Button(self.master, text="-", width=6, command=lambda: self.controller.inputVal('-')).grid(row=5, column=column4)
        Button(self.master, text="*", width=6, command=lambda: self.controller.inputVal('*')).grid(row=4, column=column3)
        Button(self.master, text="/", width=6, command=lambda: self.controller.inputVal('/')).grid(row=4, column=column4)
        Button(self.master, text="(", width=6, command=lambda: self.controller.inputVal('(')).grid(row=3, column=column3)
        Button(self.master, text=")", width=6, command=lambda: self.controller.inputVal(')')).grid(row=3, column=column4)
        Button(self.master, text=".", width=6, command=lambda: self.controller.inputVal('.')).grid(row=6, column=column1)


        # Behavior Functions
        Button(self.master, text='AC', width=6, command=lambda: self.controller.clearAll()).grid(row=1, column=column3)
        Button(self.master, text='C',  width=6, command=lambda: self.controller.deleteOne()).grid(row=1, column=column4)
        Button(self.master, text='-/+', width=6, command=lambda: self.controller.buttonevent(btn.minusplus)).grid(row=6, column=column2)
        Button(self.master, text='=', width=13, command=lambda: self.controller.calculate()).grid(row=6, column=column3, columnspan=12, sticky= E)
        self.degtoradBtn = Button(self.master, text="RAD", width=6, command=lambda: self.degtoradBtntoggle())
        self.degtoradBtn.grid(row=1, column=column2)

        #Elementary Functions
        Button(master, text="sin(x)",   width=6, command=lambda: self.controller.buttonevent(btn.sin)).grid(row=2, column=column0)
        Button(master, text="e^x",   width=6, command=lambda: self.controller.buttonevent(btn.epowx)).grid(row=2, column=column1)
        Button(master, text="10^x",  width=6, command=lambda: self.controller.buttonevent(btn.exp10)).grid(row=2, column=column2)
        Button(master, text="√x",     width=6, command=lambda: self.controller.buttonevent(btn.sqr)).grid(row=2, column=column3)
        Button(master, text="ln(x)", width=6, command=lambda: self.controller.buttonevent(btn.ln)).grid(row=2, column=column4)

    def degtoradBtntoggle(self):
        currentBnt = self.degtoradBtn.config('text')[-1]
        if currentBnt == 'RAD':
            self.degtoradBtn.config(text='DEG')
            self.controller.degtorad(False)
        else:
            self.degtoradBtn.config(text='RAD')
            self.controller.degtorad(True)

if __name__ == '__main__':
    pass