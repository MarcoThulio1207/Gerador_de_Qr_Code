import customtkinter as ctk
from tkinter import *
import qrcode


janela = ctk.CTk()
janela.geometry("300x300")
janela.title("Gerador")
janela.resizable(False,False)

gerador = None 

def clique ():
    info = gerador.get()
    img = qrcode.make(info)
    img.show()
    nf.delete(0,END)


gerador = ctk.CTkEntry(janela , placeholder_text="Insira seu texto aqui!!!:",font=("Constantia", 13), width=170)
gerador.place(x = 70, y=110)


botao = ctk.CTkButton(janela, text="Gerar Qr Code", font=("Constantia",13), width=150,command=clique)
botao.place(x= 80, y=175)

janela.mainloop()
