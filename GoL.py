# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:55:49 2017

@author: Swifty
"""

import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.pack()
        #self.createWidgets()
        
        self.flag = True
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
        for i in range(50):
            for cell in self.rect.keys():
                if (self.canvas.gettags(self.rect[cell[0], cell[1]])[0] == "alive"):
                    a[cell[0], cell[1]] = 1
            
            a = self.next_generation(a)            
            for i in range(a.shape[0]):
                for j in range(a.shape[1]):
                    if(a[i, j] == 1.0):
                        self.canvas.itemconfig(self.rect[i, j], tag="alive")
                    else:
                        self.canvas.itemconfig(self.rect[i, j], tag="dead")
            
   
    
    
    def next_generation(self, a):
        a_new = np.lib.pad(a, ((1, 1), (1, 1)), 'wrap')
        for i in range(1, a.shape[0]+1):
            for j in range(1, a.shape[1]+1):
                population = np.sum(a_new[i-1:i+2, j-1:j+2])
                if (population == 3):
                   a[i-1, j-1] = 1
                elif(population == 4):
                    if(a_new[i, j] == 1):
                        a[i-1, j-1] = 1
                else:
                    a[i-1, j-1] = 0
        return a
            
    
    def stop(self):
        self.flag = False
         
    def createWidgets(self):
        self.START = tk.Button(self)
        self.START["text"] = "Start"
        self.START["fg"] = 'black'
        self.START["command"] = self.play
        
        self.START.pack({"side":"left"})
        
        self.STOP = tk.Button(self)
        self.STOP["text"] = "Stop"
        self.STOP["fg"] = 'black'
        self.STOP["command"] = self.stop
        
        self.STOP.pack({"side":"right"})
    

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
    
    def redrawAfterPlay(self):
        self.canvas.itemconfig("dead", fill="white")
        self.canvas.itemconfig("alive", fill="black")


        



if __name__ == "__main__":
    app = App()
    app.bind('<Button-1>', app.motion)
    app.createWidgets()
    app.mainloop()

    
    
