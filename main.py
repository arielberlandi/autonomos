from tkinter import *
import sqlite3
def cadastro () :

    def get_data():
        nome_func = nome.get()
        dtNascto_func = str(dtNascto.get())
        cpf_func = str(cpf.get())
        nis_func = str(nis.get())
        codCBO_func = str(codCBO.get())
        codCateg_func = str(codCateg.get())
        carreteiro_func = str (get())  # SE FOR 1 É CARRETEIRO
        vrremun_func = str (wd_vrremun.get())
        conn = sqlite3.connect('autonomos.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO autonomos (nome, dtnscto, cpf, nis, codcbo, codcateg, carreteiro, vrremun)
        VALUES (?,?,?,?,?,?,?,?)
        """, (nome_func, dtNascto_func, cpf_func, nis_func, codCBO_func, codCateg_func, carreteiro_func, vrremun_func))
        conn.commit()
        print('Dados inseridos com sucesso.')
        conn.close()
        janela.destroy()
    def get():
        if a.get() == 1:
            return "1"
        else:
            return "0"
    janela = Tk()
    janela.title("Cadastro")
    nome = Entry(janela)
    nome.place(x=100, y=50, width=420)
    lb_nome = Label(janela, text="Nome :")
    lb_nome.place(x=10, y=50)
    dtNascto = Entry(janela)
    dtNascto.place(x=160, y=80)
    lb_dtNascto = Label(janela, text="Data de Nascimento : ")
    lb_dtNascto.place(x=10, y=80)
    cpf = Entry(janela)
    cpf.place(x=160, y=110)
    lb_cpf = Label(janela, text="CPF : ")
    lb_cpf.place(x=10, y=110)
    nis = Entry(janela)
    nis.place(x=160, y=140)
    lb_nis = Label(janela, text="NIS : ")
    lb_nis.place(x=10, y=140)
    codCBO = Entry(janela)
    codCBO.place(x=160, y=170, width=100)
    lb_codCBO = Label(janela, text="Código CBO : ")
    lb_codCBO.place(x=10, y=170)
    codCateg = Entry(janela)
    codCateg.place(x=160, y=200, width=80)
    lb_codCateg = Label(janela, text="Código Categoria :")
    lb_codCateg.place(x=10, y=200)
    carreteiro = Label(janela, text="Carreteiro / Frete :")
    carreteiro.place(x=10, y=230)
    a = IntVar()
    lb_carreteiro = Checkbutton(janela, variable=a, command=get)
    lb_carreteiro.place(x=153, y=230)
    vrremun = Label(janela, text='Valor da Remuneração :')
    vrremun.place(x=10,y=260)
    wd_vrremun = Entry(janela)
    wd_vrremun.place(x=160,y=260,width=100)
    bt_salvar = Button(janela, text='Salvar', width=10, command=get_data)
    bt_salvar.place(x=410, y=255)
    janela.geometry("530x300+100+100")
    janela.mainloop()
    janela.destroy()
def export_xml () :


    def cod():
        from xml.dom.minidom import Document

        # document create
        doc = Document()

        # element
        root = doc.createElement('esocial')
        evtRemun = doc.createElement('evtRemun')
        ideEvento = doc.createElement('ideEvento')
        indRetif = doc.createElement('indRetif')
        indApuracao = doc.createElement('indApuracao')
        perApur = doc.createElement('perApur')
        tpAmb = doc.createElement('tpAmb')
        procEmi = doc.createElement('procEmi')
        verProc = doc.createElement('verProc')
        ideEmpregador = doc.createElement('ideEmpregador')
        tpInsc = doc.createElement('tpInsc')
        nrInsc = doc.createElement('nrInsc')
        ideTrabalhador = doc.createElement('ideTrabalhador')
        cpfTrab = doc.createElement('cpfTrab')
        nisTrab = doc.createElement('nisTrab')
        infoComplem = doc.createElement('infoComplem')
        nmTrab = doc.createElement('nmTrab')
        dtNascto = doc.createElement('dtNascto')
        dmDev = doc.createElement('dmDev')
        ideDmDev = doc.createElement('ideDmDev')
        codCateg = doc.createElement('codCateg')
        infoPerApur = doc.createElement('infoPerApur')
        ideEstabLot = doc.createElement('ideEstabLot')

        tpInsc2 = doc.createElement('tpInsc')
        nrInsc2 = doc.createElement('nrInsc')
        codLotacao = doc.createElement('codLotacao')
        remunPerApur = doc.createElement('remunPerApur')
        itensRemun = doc.createElement('itensRemun')

        codRubr = doc.createElement('codRubr')
        ideTrabRubr = doc.createElement('ideTrabRubr')
        vrRubr = doc.createElement('vrRubr')

        infoComplCont = doc.createElement('infoComplCont')
        codCBO = doc.createElement('codCBO')

        # child
        doc.appendChild(root)
        root.appendChild(evtRemun)

        evtRemun.appendChild(ideEvento)
        ideEvento.appendChild(indRetif)
        ideEvento.appendChild(indApuracao)
        ideEvento.appendChild(perApur)
        ideEvento.appendChild(tpAmb)
        ideEvento.appendChild(procEmi)
        ideEvento.appendChild(verProc)

        evtRemun.appendChild(ideEmpregador)
        ideEmpregador.appendChild(tpInsc)
        ideEmpregador.appendChild(nrInsc)

        evtRemun.appendChild(ideTrabalhador)
        ideTrabalhador.appendChild(cpfTrab)
        ideTrabalhador.appendChild(nisTrab)
        ideTrabalhador.appendChild(infoComplem)
        infoComplem.appendChild(nmTrab)
        infoComplem.appendChild(dtNascto)

        evtRemun.appendChild(dmDev)
        dmDev.appendChild(ideDmDev)
        dmDev.appendChild(codCateg)
        dmDev.appendChild(infoPerApur)
        infoPerApur.appendChild(ideEstabLot)
        ideEstabLot.appendChild(tpInsc2)
        ideEstabLot.appendChild(nrInsc2)
        ideEstabLot.appendChild(codLotacao)

        ideEstabLot.appendChild(remunPerApur)
        remunPerApur.appendChild(itensRemun)

        itensRemun.appendChild(codRubr)
        itensRemun.appendChild(ideTrabRubr)
        itensRemun.appendChild(vrRubr)

        itensRemun.appendChild(codRubr)
        itensRemun.appendChild(ideTrabRubr)
        itensRemun.appendChild(vrRubr)

        dmDev.appendChild(infoComplCont)
        infoComplCont.appendChild(codCBO)

        # receive data
        ident = str(1)
        a = str(1)
        b = str(1)
        c = str(1)
        d = str(1)
        e = str(1)
        f = str(1)
        g = str(1)
        h = str(1)
        i = str(1)
        j = str(1)
        k = str(1)
        l = str(1)
        m = str(1)
        n = str(1)
        o = str(1)
        p = str(1)
        q = str(1)
        r = str(1)


        # atributes
        root.setAttribute('xmlns', 'http://www.esocial.gov.br/schema/evt/evtRemun/v02_04_02')
        evtRemun.setAttribute('Id', ident)

        # text mode in child
        txt1 = doc.createTextNode(a)
        indRetif.appendChild(txt1)

        txt2 = doc.createTextNode(b)
        indApuracao.appendChild(txt2)

        txt3 = doc.createTextNode(c)
        perApur.appendChild(txt3)

        txt4 = doc.createTextNode(d)
        tpAmb.appendChild(txt4)

        txt5 = doc.createTextNode(e)
        procEmi.appendChild(txt5)

        txt6 = doc.createTextNode(f)
        verProc.appendChild(txt6)

        txt7 = doc.createTextNode(g)
        tpInsc.appendChild(txt7)

        txt8 = doc.createTextNode(h)
        nrInsc.appendChild(txt8)

        txt9 = doc.createTextNode(i)
        cpfTrab.appendChild(txt9)

        txt10 = doc.createTextNode(j)
        nisTrab.appendChild(txt10)

        txt11 = doc.createTextNode(k)
        nmTrab.appendChild(txt11)

        txt12 = doc.createTextNode(l)
        dtNascto.appendChild(txt12)

        txt13 = doc.createTextNode(m)
        ideDmDev.appendChild(txt13)

        txt14 = doc.createTextNode(n)
        codCateg.appendChild(txt14)

        txt16 = doc.createTextNode(o)
        tpInsc2.appendChild(txt16)

        txt17 = doc.createTextNode(p)
        nrInsc2.appendChild(txt17)

        txt18 = doc.createTextNode(q)
        codLotacao.appendChild(txt18)

        txt25 = doc.createTextNode(r)
        codCBO.appendChild(txt25)

        nomedoxml = ident + ".xml"

        doc.writexml(open(nomedoxml, 'w'),
                     addindent='    ',
                     newl='\n')

        doc.unlink()
    export = Tk ()
    a = Button(export, text="Exportar", command=cod)
    a.place(x=20,y=30)
    export.geometry("530x300+100+100")
    export.mainloop()
def alterar () :
    conn = sqlite3.connect('autonomos.db')
    cursor = conn.cursor()
    alterar = Tk ()
    alterar.geometry("530x300+100+100")
    lbemails = Listbox(alterar,width=60)
    lbemails.place(x=25, y=40)
    cursor.execute("""
    SELECT * FROM autonomos;
    """)
    for linha in cursor.fetchall():
        x = 0
        lbemails.insert(x,linha)
        x = x + 1
    conn.close()
    lblMat = Label(alterar,text="Escolha o Item Abaixo :")
    lblMat.place(x=200,y=20)
    alterar.mainloop()
def excluir () :
    excluir = Tk ()
    excluir.geometry("530x300+100+100")
    excluir.mainloop()
def menu () :
    menu = Tk()
    menu.title("Programa")
    bt = Button(menu, text="Novo", width=50, command=cadastro)
    bt.place(x=50,y=100)
    bt = Button(menu, text="Alterar", width=50, command=alterar)
    bt.place(x=50,y=130)
    bt = Button(menu, text="Excluir", width=50, command=excluir)
    bt.place(x=50,y=160)
    bt = Button(menu, text="Exportar para XML", width=50, command=export_xml)
    bt.place(x=50,y=190)
    menu.geometry("530x300+100+100")
    menu.mainloop()
#programa
menu()
#export_xml ()