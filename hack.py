#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:10:09 2017

@author: kidiki
Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import Tkinter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Tkinter import *

def next_generation(a):
    a_new = np.lib.pad(a, ((1, 1), (1, 1)), 'wrap')
    for i in range(1, a.shape[0]+1):
        for j in range(1, a.shape[1]+1):
            population = np.sum(a_new[i-1:i+2, j-1:j+2])
            if (population == 3):
               a[i-1, j-1] = 1
            elif(population == 4):
                if(a_new[i, j] == 1):
                    a[i-1, j-1] = 1;
            else:
                a[i-1, j-1] = 0
    
    return a
    

a = np.zeros((30, 30))
a[14, 16] = 1
a[15:17, 14] = 1
a[17, 15:17] = 1
a[15:17, 17] = 1


master = Tk()

b = Button(master, text="Start", command=next_generation(a))
b.pack()

mainloop()




ims=[]
fig=plt.figure() 

for next in range(150):
    nextGenerationArray = next_generation(a)
    ims.append((plt.imshow(np.copy(nextGenerationArray)),))



imani = animation.ArtistAnimation(fig,ims,interval=150,repeat=False) 
        
#plt.clf()                
#plt.imshow(a)
plt.show()

            
            

            
        
        
