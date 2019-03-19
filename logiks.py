#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:00:04 2019

@author: sku35268
"""

from os.path import basename, splitext
import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry
import random

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = 'Logik'
    
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.barvy = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 "\
                    "#dd9900 #ffffff".split()
        self.sirka = 30
        self.vyska = 20
        
        #skryté pole
        self.skryteBarvy = []
        for sloupec in range(5):
            c = tk.Canvas(self, background='black', width=self.sirka, height=self.vyska)
            c.grid(column=sloupec,row=0)
            self.skryteBarvy.append(c)
        #titulek
        tk.Label(self, text=u"Logik").grid(columnspan=5)
        #pole s hádanou barvou
        self.hadaneBarvy = []
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = tk.Canvas(self, background='lightgray', width=self.sirka, height=self.vyska)
                c.grid(column=sloupec,row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)
        
        
        #odpověď programu 
        odpovedProgramu = []
        for radek in range(10):
            lbl=tk.Label(self,text="-/-")
            lbl.grid(column=6,row=radek+2)
            odpovedProgramu.append(lbl)
            
            
        #oddělovací čára
        c = tk.Canvas( background='#777', 
                width=6*self.sirka, height=8)
        c.grid(column=0,row=12, columnspan=5)
    
    
        #tlačítka
        for radek,barva in enumerate(self.barvy):
            for sloupec in range(5):
                def akce(r=radek, s=sloupec):
                    self.click(r,s)
                b = tk.Button(width=self.sirka, height=self.vyska,
                bitmap="gray12",
                activebackground=barva,activeforeground=barva,
                bg=barva, fg=barva, command=akce)
                b.grid(row = radek+12, column= sloupec)
    
    
        
    def click(self, r, s):
        print(r,s)
        aktivniRadek = 9 #zatim
        self.hadaneBarvy[aktivniRadek][s].config(background=self.barvy[r]) 
   
    
        self.hadanka = []
        for x in range(5):
            while 1:
                nahodnaBarva=self.barvy[random.randint(0,len(self.barvy)-1)]
                if not nahodnaBarva in self.hadanka:
                    break
            self.hadanka.append(nahodnaBarva)
        return self.hadanka
        
    def quit(self, event=None):
        super().quit()




app = Application()
app.mainloop()
    