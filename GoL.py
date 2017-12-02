# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:55:49 2017

@author: Swifty
"""

import tkinter as tk
import random
import numpy as np

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=500, height=550, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 100
        self.columns = 100
        self.cellwidth = 25
        self.cellheight = 25
        self.x = 0
        self.y = 0
        self.rect = {}
        
        for column in range(20):
            for row in range(20):
                x1 = column*self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="dead")
                
    def play(self):
        a = np.zeros((20, 20))
        for (cell in self.rect.iterkeys()):
            if (self.canvas.gettags(self.rect(cell))[0] == "alive"):
                a[cell[0], cell[1]] = 1
        
            

         
    def createWidgets(self):
        self.START = Button(self)
        self.START["text"] = "Start"
        self.START["fg"] = 'blue'
        self.START["command"] = self.play
    

    def motion(self, event):
       self.x, self.y = event.x, event.y
       self.x = int(self.x/25)
       self.y = int(self.y/25)
        
        
       self.redraw(1000)
        
        
    def redraw(self, delay):
        item_id = self.rect[self.y,self.x]
        if (self.canvas.gettags(item_id)[0] == "dead"):
            self.canvas.itemconfig(item_id, tag="alive") 
        else:
            self.canvas.itemconfig(item_id, tag="dead")
        self.canvas.itemconfig("dead", fill="white")
        self.canvas.itemconfig("alive", fill="black")


        



if __name__ == "__main__":
    app = App()
    app.bind('<Button-1>', app.motion)
    app.mainloop()

    
    