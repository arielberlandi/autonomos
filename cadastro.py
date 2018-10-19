
from tkinter import *


def get():
    if a.get() == 1:
        print("S")
    else:
        return None
    return None

janela = Tk()
janela.title("Cadastro")

nome = Entry(janela)
nome.place(x=100,y=50, width=450)

lb_nome = Label(janela, text="Nome :")
lb_nome.place(x=50,y=50)

dtNascto = Entry(janela)
dtNascto.place(x=200,y=80)

lb_dtNascto = Label(janela, text="Data de Nascimento : ")
lb_dtNascto.place(x=50,y=80)

cpf = Entry(janela)
cpf.place(x=200,y=110)

lb_cpf = Label(janela, text="CPF : ")
lb_cpf.place(x=50,y=110)

nis = Entry(janela)
nis.place(x=200,y=140)

lb_nis = Label(janela, text="NIS : ")
lb_nis.place(x=50,y=140)

codCBO = Entry(janela)
codCBO.place(x=200,y=170)

lb_codCBO = Label(janela, text="Código CBO : ")
lb_codCBO.place(x=50,y=170)

codCateg = Entry(janela)
codCateg.place(x=200,y=200)

lb_codCateg = Label(janela, text="Código Categoria :")
lb_codCateg.place(x=50,y=200)

carreteiro = Label(janela, text="Carreteiro / Frete :")
carreteiro.place(x=50,y=230)

a = IntVar()
lb_carreteiro = Checkbutton(janela,variable=a,command=get)
lb_carreteiro.place(x=193,y=230)

bt_salvar = Button(janela, text='Salvar', width=10)
bt_salvar.place(x=430,y=300)

janela.geometry("600x400+100+100")
janela.mainloop()