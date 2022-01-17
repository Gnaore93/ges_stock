

import tkinter as tk
from tkinter import*
from turtle import color, left, width





window = Tk()
window.geometry('1200x1200')
window.title("GES-STOCK")
window.configure(bg='white')

def open_menu_prodt():
   new_windown = Toplevel(window)
   new_windown.geometry('1000x600')
   new_windown.title("PRODUIT")
   new_windown.configure(bg= "white")
   lbl= menubar(new_windown,text ="ok")
   lbl.pack()

def open_menu_clt():
   new_windown_clt = Toplevel(window)
   new_windown_clt.geometry('1000x600')
   new_windown_clt.configure(bg= "white")
   lbl= menubar1(new_windown_clt,text ="ok")
   lbl.pack()


def open_menu_livsn():
   new_windown_livsn = Toplevel(window)
   new_windown_livsn.geometry('1000x600')
   new_windown_livsn.configure(bg= "white")
   lbl= menubar2(new_windown_livsn,text ="ok")
   lbl.pack()


def open_menu_hist():
   new_windown_hist = Toplevel(window)
   new_windown_hist.geometry('1000x600')
   new_windown_hist.configure(bg= "white")
   lbl= menubar3(new_windown_hist,text ="ok")
   lbl.pack()


def open_menu_stock():
   new_windown_stock = Toplevel(window)
   new_windown_stock.geometry('1000x600')
   new_windown_stock.configure(bg= "white")
   lbl= menubar4(new_windown_stock,text ="ok")
   lbl.pack()

def open_edit_clt():
   new_windown_edit_clt = Toplevel(window)
   new_windown_edit_clt.geometry('1000x600')
   new_windown_edit_clt.configure(bg= "white")
   lbl= menubar5(new_windown_edit_clt,text ="ok")
   lbl.pack()

def open_edit_prd():
   new_windown_edit_prd = Toplevel(window)
   new_windown_edit_prd.geometry('1000x600')
   new_windown_edit_prd.configure(bg= "white")
   lbl= menubar5(new_windown_edit_prd,text ="ok")
   lbl.pack()


dropdown = tk.Menu(window)
menubar=tk.Menu(dropdown,tearoff=0)
menubar.add_command(label="Ajout produit",command=open_menu_prodt)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar1=tk.Menu(dropdown,tearoff=0)
menubar1.add_command(label="Ajout client",command=open_menu_clt)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar2=tk.Menu(dropdown,tearoff=0)
menubar2.add_command(label="Effectuer livraison",command=open_menu_livsn)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar3=tk.Menu(dropdown,tearoff=0)
menubar3.add_command(label="Historique livraison",command=open_menu_hist)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar4=tk.Menu(dropdown,tearoff=0)
menubar4.add_command(label="Voir mes stock",command=open_menu_stock)
window.config(menu=dropdown)

dropdown = tk.Menu(window)
menubar5=tk.Menu(dropdown,tearoff=0)
menubar5.add_command(label="Editer client",command=open_edit_clt)
menubar5.add_command(label="Editer produit",command=open_edit_prd)
window.config(menu=dropdown)


dropdown.add_cascade(label="PRODUIT",menu= menubar)
dropdown.add_cascade(label="CLIENT",menu= menubar1)
dropdown.add_cascade(label="LIVRAISON",menu= menubar2)
dropdown.add_cascade(label="HISTORIQUE",menu= menubar3)
dropdown.add_cascade(label="GESTION DES STOCK",menu= menubar4)
dropdown.add_cascade(label="EDITER",menu= menubar5)







window.mainloop()