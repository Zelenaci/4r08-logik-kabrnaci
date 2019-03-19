#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:07:40 2019

@author: vyk35227
"""

from os.path import basename, splitext
import tkinter as tk
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Logik"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.barvy = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 "\
                     "#dd9900 #ffffff".split()
        self.sirka = 30
        self.vyska = 20
        ### skrytá pole ###
        self.skryteBarvy=[]
        for sloupec in range(5):
            c = tk.Canvas(self, background="black", width=self.sirka, height=self.vyska)
            c.grid(column=sloupec,row=0)
            self.skryteBarvy.append(c)
        ### titulek ###
        tk.Label(self, text="Logik").grid(columnspan=5)
        tk.Label(self, text="barva/pozice").grid(row=1,column=6)
        ### pole s hádanou barvou ###
        self.hadaneBarvy=[]
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = tk.Canvas(self, background="gray65", width=self.sirka, height=self.vyska)
                c.grid(column=sloupec, row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)

        
        ### statistika ###        
        odpovedProgramu = []
        for radek in range(10):
            l = tk.Label(self, text="- / -")
            l.grid(column=6,row=radek+2)
            odpovedProgramu.append(l)

        ### oddělovací čára ###
        tk.Canvas(self, background="black", width=6*self.sirka, height=5).grid(column=0, row=12, columnspan=5)
        
        ### tlačítka barev ###
        #tlacitka = []
        for radek, barva in enumerate(self.barvy):
            for sloupec in range(5):
                def akce(r=radek, s=sloupec):
                    self.click(r, s)
                b = tk.Button(self, width=self.sirka, height=self.vyska,\
                              bg=barva, fg=barva, bitmap="gray12",\
                              activebackground="gray65", activeforeground="gray65",\
                              command=akce)
                b.grid(row=radek+13, column=sloupec)
        
    def click(self, r, s):
        print(r,s)
        aktivniRadek = 9 #zatim
        self.hadaneBarvy[aktivniRadek][s].config(background=self.barvy[r])

   
        
        # self.bind("<Escape>", self.quit)
        # self.lbl = tk.Label(self, text="Hello World")
        # self.lbl.pack()
        # self.btn = tk.Button(self, text='Quit', command=self.quit)
        # self.btn.pack()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
