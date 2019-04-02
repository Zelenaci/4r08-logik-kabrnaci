#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:07:40 2019

@author: vyk35227
"""

from os.path import basename, splitext
from tkinter import messagebox, filedialog
import tkinter as tk
import random
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
        self.znova = False
        self.novaHra()
        global aktivniRadek
        aktivniRadek = 9     
        ### skrytá pole ###
        self.skryteBarvy=[]
        for sloupec in range(5):
            c = tk.Canvas(self, background="black", width=self.sirka, height=self.vyska)
            c.grid(column=sloupec,row=0)
            self.skryteBarvy.append(c)            
        ### titulek ###
        tk.Label(self, text="Logik").grid(columnspan=5, row=1)
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
        self.odpovedProgramu = []
        for radek in range(10):
            l = tk.Label(self, text="- / -")
            l.grid(column=6,row=radek+2)
            self.odpovedProgramu.append(l)

        ### oddělovací čára ###
        tk.Canvas(self, background="black", width=6*self.sirka, height=5).grid(column=0, row=12, columnspan=5)
        
        ### tlačítka hry ###
        def odeslat():
            global aktivniRadek
            global pokus
            if self.konec == True:
                self.znovu()
        
            elif "," in self.pokus:
                print("Chyba, vyberte všechna pole")
                messagebox.showerror(title="Chybný výběr polí", message="Chyba, vyberte všechna pole")
            
            elif aktivniRadek > -1:
                print(self.skryteBarvy)
                ### kontrola barev ###
                spravnaPozice = 0
                spravnaBarva = 0
                for i in range(len(self.pokus)):
                    if self.pokus[i] == self.hadanka[i]:
                        spravnaPozice += 1
                    if self.pokus[i] in self.hadanka:
                        spravnaBarva += 1
                self.odpovedProgramu[aktivniRadek].config(text="{}/{}".format(spravnaBarva,spravnaPozice))
                print(aktivniRadek)
                if spravnaBarva == 5 and spravnaPozice == 5:
                    print("Výhra")
                    messagebox.showinfo(title="Výhra", message="Vyhrál jste!")
                    for sloupec in range(5):
                        b = self.hadanka[sloupec]
                        self.skryteBarvy[sloupec].config(background=b)
                        self.konec = True
                aktivniRadek -= 1

            else:
                print("Prohra")
                for sloupec in range(5):
                        b = self.hadanka[sloupec]
                        self.skryteBarvy[sloupec].config(background=b)
                self.konec = True
                messagebox.showinfo(title="Prohra", message="Prohrál jste!")
                
            
            
        tk.Button(self, text="Odeslat", command=odeslat).grid(column=6)
        tk.Button(self, text="Znovu", command=self.znovu).grid(column=6)
        
        ### tlačítka barev ###
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
        self.hadaneBarvy[aktivniRadek][s].config(background=self.barvy[r])
        self.pokus[s] = self.barvy[r]
        print(self.pokus)
        

    def znovu(self):
        self.znova = True
        self.novaHra()

    def novaHra(self):
        self.konec = False
        global aktivniRadek
        global odpovedProgramu
        aktivniRadek=9
        self.hadanka = []
        if self.znova == True:
            for radek in range(5):
                for sloupec in range(10):
                    self.hadaneBarvy[sloupec][radek].config(background="gray65")
                for radek in range(10):
                    self.odpovedProgramu[radek].config(text=" / ")
                for sloupec in range(5):
                    self.skryteBarvy[sloupec].config(background="black") 
                    
            
        for x in range(5):
            while 1:
                nahodnaBarva=self.barvy[random.randint(0,len(self.barvy)-1)]
                if not nahodnaBarva in self.hadanka:
                    break
            self.hadanka.append(nahodnaBarva)
        print(self.hadanka)
        global pokus
        self.pokus=[","]*5
        print(self.pokus)
        return self.hadanka
        

    
   
        
        # self.bind("<Escape>", self.quit)
        # self.lbl = tk.Label(self, text="Hello World")
        # self.lbl.pack()
        # self.btn = tk.Button(self, text='Quit', command=self.quit)
        # self.btn.pack()


    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
