# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:55:49 2017

@author: Swifty
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.flag = True
        self.buttonIsPressed = False
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
        self.flag = True
        self.buttonIsPressed = True
        a = np.zeros((20, 20))
        for cell in self.rect.keys():
            if (self.canvas.gettags(self.rect[cell[1], cell[0]])[0] == "alive"):
                a[cell[1], cell[0]] = 1
                
        a = self.next_generation(a)
    
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                if(a[i, j] == 1.0):
                    self.canvas.itemconfig(self.rect[i, j], tag="alive")
                else:
                    self.canvas.itemconfig(self.rect[i, j], tag="dead")
        self.redrawAfterPlay(1000)
           
      
    def spaseship(self):
        a = np.zeros((30, 30))

        a[14, 16] = 1
        a[15:17, 14] = 1
        a[17, 15:17] = 1
        a[15:17, 17] = 1
        
        ims = []
        fig = plt.figure() 
        
        for next in range(150):
            nextGenerationArray = self.next_generation(a)
            ims.append((plt.imshow(np.copy(nextGenerationArray)),))
        
        ims = animation.ArtistAnimation(fig,ims,interval=150,repeat=False) 
        
        plt.show()
   
    
    
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
            
    
    def createWidgets(self):
        self.START = tk.Button(self)
        self.START["text"] = "Next Generation"
        self.START["fg"] = 'black'
        self.START["command"] = self.play
        self.START["width"] = 10
        self.START.bind('<Enter>', self.enterWidget)
        self.START.bind('<Leave>', self.leftWidget)     
        
        self.START.pack({"side":"left"})
        
        self.STOP = tk.Button(self)
        self.STOP["text"] = "Stop"
        self.STOP["fg"] = 'black'
        self.STOP["width"] = 10
        self.STOP.bind('<Enter>', self.enterWidget)
        self.STOP.bind('<Leave>', self.leftWidget) 
        self.STOP["command"] = self.destroy
        
        self.STOP.pack({"side":"right"})
        
        
        self.pattern1 = tk.Button(self)
        self.pattern1["text"] = "Buterfly"
        self.pattern1["fg"] = 'black'
        self.pattern1["width"] = 10
        self.pattern1.bind('<Enter>', self.enterWidget)
        self.pattern1.bind('<Leave>', self.leftWidget) 
        #self.pattern1["command"] = self.destroy
        
        self.pattern1.pack({"side":"bottom"})
        
        
        self.pattern2 = tk.Button(self)
        self.pattern2["text"] = "Spaceship"
        self.pattern2["fg"] = 'black'
        self.pattern2["width"] = 10
        self.pattern2.bind('<Enter>', self.enterWidget)
        self.pattern2.bind('<Leave>', self.leftWidget) 
        #self.pattern2["command"] = self.spaseship
        
        self.pattern2.pack({"side":"bottom"})
    

    def motion(self, event):
        print ("{},{}".format(event.x, event.y))
        if(event.y  < 500 and self.flag):
            self.x, self.y = event.x, event.y
            self.x = int(self.x/25)
            self.y = int(self.y/25)  
            self.redraw(0)
        
      
        
    def enterWidget(self, event):
        self.flag = False
        self.y = 500

        
    def leftWidget(self, event):
        self.flag = True
        
        
    def redraw(self, delay):
        if(self.buttonIsPressed == False):
            item_id = self.rect[self.y,self.x]
            if (self.canvas.gettags(item_id)[0] == "dead"):
                self.canvas.itemconfig(item_id, tag="alive") 
            else:
                self.canvas.itemconfig(item_id, tag="dead")
            self.canvas.itemconfig("dead", fill="white")
            self.canvas.itemconfig("alive", fill="black")
        #self.after(delay, lambda: self.redraw(delay))
            
            
      
    
    def redrawAfterPlay(self,delay):
        self.canvas.itemconfig("dead", fill="white")
        self.canvas.itemconfig("alive", fill="black")
        self.after(delay, lambda: self.redrawAfterPlay(delay))
        


        



if __name__ == "__main__":
    app = App()
    app.bind('<Button-1>', app.motion)
    app.createWidgets()
    app.mainloop()

    
    
