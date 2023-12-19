import customtkinter as ctk
from tkinter import *
import qrcode


janela = ctk.CTk()
janela.geometry("300x300")
janela.title("ID do Casco")
janela.resizable(False,False)

nf = None 

def clique ():
    info = nf.get()
    img = qrcode.make(info)
    img.show()
    nf.delete(0,END)


nf = ctk.CTkEntry(janela , placeholder_text="Insira o número da NF-e:",font=("Constantia", 13), width=170)
nf.place(x = 70, y=110)


botao = ctk.CTkButton(janela, text="Gerar Qr Code", font=("Constantia",13), width=150,command=clique)
botao.place(x= 80, y=175)

janela.mainloop()