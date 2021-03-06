__author__ = "The CalculatorPro Inc."
__copyright__ = "Copyright 2018, CalculatorPro"
__credits__ = ['Team A']
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Team A"
__email__ = "TeamA@mail.concordia.ca"
__status__ = "Release v1.0"

#Import GUI
from tkinter import Tk
from tkinter import END
from View.main import CalculatorGUI as View
from CommonAssets.main import Button as btn

#Import Model
from Model.sin import sin
from Model.exp import exp as epowx
from Model.log import ln
from Model.squareroot import squareroot
from Model.tentopowerx import tentopowerx as exp10
from Model.config import E, PI
from Model.config import degreeToRadian

class Controller():

    def __init__(self):
        self.root = Tk()
        self.view = View(self.root, self)
        self.currentvalue = 0
        self.rad = True

    def run(self):
        self.root.mainloop()

    def buttonevent(self,function):

        entry = self.getEntry()
        result = 0

        if (self.isWithinRange(entry)):
            if (function==btn.ln):
                result = ln(entry)
            elif (function==btn.sqr):
                result = squareroot(entry)
            elif (function==btn.exp10):
                result = exp10(entry)
            elif (function==btn.sin):
                if not self.rad:
                    entry= degreeToRadian(entry)
                result = sin(entry)
            elif (function == btn.minusplus):
                result = -1 * entry
            elif (function==btn.epowx):
                result = epowx(entry)
            else:
                pass
            self.clearEntry()
            self.writeEntry(self.formatOutput(result))
        else:
            result = 'Out of Range'
            self.clearEntry()
            self.writeEntry(result)

    def degtorad(self, rad):
        #self.rad = not self.rad;
        self.rad = rad

    def getEntry(self):
        return eval(self.view.entry.get())

    def clearEntry(self):
        self.view.entry.delete(0, END)

    def writeEntry(self,result):
        self.view.entry.insert(0, result)

    def isWithinRange(self,num):
        result = True
        if (num > 10000000000 or num < -10000000000):
            result = False
        return result

    def keyPressed(self,event):
        #print(event.char)
        if (event.keysym not in ('0','1','2','3','4','5','6','7','8','9','period','BackSpace')):
            return 'break'
        self.currentvalue = event.keysym
        #if ()
        print(self.currentvalue)

    def formatOutput(self,num):

        if isinstance(num,str):
            return num
        else:
            numStr = "{0:.7f}".format(num)
            numStrInt = int(num)
            numStrComp = "{0:.7f}".format(numStrInt)
            if(numStr==numStrComp):
                return numStrInt
            elif (numStr == '-0.0000000'):
                return '0'
            elif (numStr == '0.0000000'):
                return '0'
            elif (numStr == '-1.0000000'):
                return '1'
            elif (numStr == '1.0000000'):
                return '1'
            else:
                    return numStr

    def clearAll(self):
        self.view.entry.delete(0, END)

    def deleteOne(self):
        self.txt = self.view.entry.get()[:-1]
        self.view.entry.delete(0, END)
        self.view.entry.insert(0, self.txt)

    def inputVal(self, argi):
        self.view.entry.insert(END, argi)

    def calculate(self):

        try:
            result = self.getEntry()
            self.clearAll()
            self.writeEntry(self.formatOutput(result))
        except Exception:
            self.clearAll()
            self.view.entry.insert(0, "Value Error")


    def e(self):
        return self.formatOutput(E)

    def pi(self):
        return self.formatOutput(PI)


if __name__ == '__main__':
    Controller().run()