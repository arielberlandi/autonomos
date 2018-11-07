from tkinter import *
import sqlite3
from datetime import *
def cadastro () :
    janela = Toplevel()
    janela.title("Cadastro")
    def get():
        if muda.get() == 1:
            return 1
        else:
            print("0")
            return 0
        return None
    muda = IntVar()
    lb_carreteiro = Checkbutton(janela, text="text", variable=muda, command=get)
    lb_carreteiro.place(x=153, y=230)
    def get_data():
        nome_func = str (nome.get())
        dtNascto_func = str(dtNascto.get())
        cpf_func = str(cpf.get())
        nis_func = str(nis.get())
        codCBO_func = str(codCBO.get())
        codCateg_func = str(codCateg.get())
        carreteiro_func = str (get())
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
    vrremun = Label(janela, text='Valor da Remuneração :')
    vrremun.place(x=10,y=260)
    wd_vrremun = Entry(janela)
    wd_vrremun.place(x=160,y=260,width=100)
    bt_salvar = Button(janela, text='Salvar', width=10, command=get_data)
    bt_salvar.place(x=410, y=255)
    janela.geometry("530x300+100+100")
    janela.focus_force()
    janela.grab_set()
    janela.mainloop()
def export_xml () :
    def cod():
        from xml.dom.minidom import Document
        conn = sqlite3.connect('autonomos.db')
        cursor = conn.cursor()
        id = int(wd_id.get())
        print(cursor.execute("select * from autonomos where id = ?;",(id,)))
        exporta_id = cursor.fetchall()
        exportado = (exporta_id[0][0:9])
        carreta = float (exportado[8])
        # document xml create
        doc = Document()
        # elements
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


#itens remun
        ideTabRubr = doc.createElement('ideTabRubr')
        ideTabRubr2 = doc.createElement('ideTabRubr')

        qtdRubr = doc.createElement('qtdRubr')
        qtdRubr2 = doc.createElement('qtdRubr')


        vrRubr = doc.createElement('vrRubr')
        vrRubr2 = doc.createElement('vrRubr')
        vrRubr3 = doc.createElement('vrRubr')

        codRubr  = doc.createElement('codRubr')
        codRubr2 = doc.createElement('codRubr')
        codRubr3 = doc.createElement('codRubr')

        itensRemun = doc.createElement('itensRemun')
        itensRemun2 = doc.createElement('itensRemun')
        itensRemun3 = doc.createElement('itensRemun')


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
        remunPerApur.appendChild(itensRemun2)
        if carreta == "1" :
            remunPerApur.appendChild(itensRemun3)

        itensRemun.appendChild(codRubr)
        itensRemun.appendChild(ideTabRubr)
        itensRemun.appendChild(qtdRubr)
        itensRemun.appendChild(vrRubr)

        itensRemun2.appendChild(codRubr2)
        itensRemun2.appendChild(ideTabRubr2)
        itensRemun2.appendChild(vrRubr2)


        dmDev.appendChild(infoComplCont)
        infoComplCont.appendChild(codCBO)



        # receive data

        def gera_id(cpf):

            id = "ID1"
            hora = str(datetime.now().strftime("%Y%m%d%H%M%S"))
            id = (id + str(cpf)+ "00" + hora + "00001")
            return id
        ident = gera_id(exportado[3])

        a = str(1)#indretif
        b = str(1)#indapuracao
        data_atual = date.today()
        c = data_atual.strftime('%Y-%m')
        d = str(1)#tpamb
        e = str(1)#procEmi
        f = str("1.0")#verProc
        g = str(1)#tpinsc
        h = str("03582844")#nrinsc
        i = str(exportado[3])#cpf
        j = str(exportado[4])#nis
        k = str(exportado[1])#nome
        nascimento =str(exportado[2])
        data = datetime.strptime(nascimento,"%Y%m%d").date()
        l = str (data)#DTNASCTO
        m = str(1)#idedmdev
        n = str(exportado[6])#codcateg
        o = str("1")#tpinsc
        p = str("03582844000186")#nrisnc
        q = str("C01S000003")#codLotacao
        r = str(exportado[5])#codcbo

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

        carreta = exportado[7]
        remuneracao = float (exportado[8])



        def remun(remuneracao, carreta):
            if carreta == "1":
                remuneracao2 = float(({}).format(remuneracao * 0.20))
                remuneracao1 = remuneracao2 * 0.11
                return remuneracao, remuneracao2, remuneracao1
            elif carreta == "0":
               
                remuneracao * 0.11
                remuneracao2 = ("{:.2f}".format(remuneracao * 0.11))
                remuneracao = ("{:.2f}".format(remuneracao))
                
                
                return remuneracao, remuneracao2
            else:
                print("ERRO")

        if carreta == "0" :
            teste = remun(remuneracao,carreta)

            print(teste)
            dd = str (teste[0])
            ddd = str (teste[1])
        else :
            teste = remun(remuneracao, carreta)
            print(teste)
            dd = str(teste[0])
            ddd = str(teste[1])
            dddd = str(teste[2])



        txt29 = doc.createTextNode("440")
        codRubr.appendChild(txt29)

        txt28 = doc.createTextNode("1")
        ideTabRubr.appendChild(txt28)

        txt33 = doc.createTextNode('11.0')
        qtdRubr.appendChild(txt33)

        txt27 = doc.createTextNode(ddd)
        vrRubr.appendChild(txt27)

        txt30 = doc.createTextNode("442")
        codRubr2.appendChild(txt30)

        txt31 = doc.createTextNode("1")
        ideTabRubr2.appendChild(txt31)

        txt32 = doc.createTextNode(dd)
        vrRubr2.appendChild(txt32)

        nomedoxml = ("01_01_s-1200_")+ ident[16:24] + "_" + ident[24:30] + ".xml"
        doc.writexml(open(nomedoxml, 'w'),
                     addindent='    ',
                     newl='\n')
        doc.unlink()
        print("Exportado com Sucesso")
    export = Toplevel ()
    a = Button(export, text="Exportar", command=cod)
    a.place(x=250,y=55)
    lb_nis = Label(export, text="ID : ")
    lb_nis.place(x=100, y=60)
    wd_id = Entry(export,width=10)
    wd_id.place(x=150,y=60)
    export.geometry("530x300+100+100")
    export.mainloop()
def alterar () :
    def alterar_data () :
        def get_id2():
            id = wd_id.get()
            nome = str (novo_nome.get())
            nascto = novo_dtNascto.get()
            cpf = novo_cpf.get()
            nis = novo_nis.get()
            cbo = novo_codCBO.get()
            categoria = novo_codCateg.get()
            carreteiro = get2()
            remuneracao = novo_vrremun.get()
            conn = sqlite3.connect('autonomos.db')
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE autonomos
            SET nome = ?, dtnscto = ?, cpf = ?, nis = ?, codcbo = ?, codcateg = ?, carreteiro = ?, vrremun = ?
            WHERE id = ?
            """, (nome, nascto, cpf, nis, cbo, categoria, remuneracao, carreteiro, id))

            conn.commit()

            print('Dados atualizados com sucesso.')

            conn.close()
        def get2():
            if muda2.get() == 1:
                return "1"
            else:
                return "0"
        janela = Toplevel()
        janela.title("Alterar")
        wd_id = Entry(janela)
        wd_id.place(x=100,y=20)
        lb_wdid = Label(janela,text="ID :")
        lb_wdid.place(x=10,y=20)
        novo_nome = Entry(janela)
        novo_nome.place(x=100, y=50, width=420)
        lb_nome = Label(janela, text="Nome :")
        lb_nome.place(x=10, y=50)
        novo_dtNascto = Entry(janela)
        novo_dtNascto.place(x=160, y=80)
        lb_dtNascto = Label(janela, text="Data de Nascimento : ")
        lb_dtNascto.place(x=10, y=80)
        novo_cpf = Entry(janela)
        novo_cpf.place(x=160, y=110)
        lb_cpf = Label(janela, text="CPF : ")
        lb_cpf.place(x=10, y=110)
        novo_nis = Entry(janela)
        novo_nis.place(x=160, y=140)
        lb_nis = Label(janela, text="NIS : ")
        lb_nis.place(x=10, y=140)
        novo_codCBO = Entry(janela)
        novo_codCBO.place(x=160, y=170, width=100)
        lb_codCBO = Label(janela, text="Código CBO : ")
        lb_codCBO.place(x=10, y=170)
        novo_codCateg = Entry(janela)
        novo_codCateg.place(x=160, y=200, width=80)
        lb_codCateg = Label(janela, text="Código Categoria :")
        lb_codCateg.place(x=10, y=200)
        carreteiro = Label(janela, text="Carreteiro / Frete :")
        carreteiro.place(x=10, y=230)
        muda2 = IntVar()
        novo_carreteiro = Checkbutton(janela, variable=muda2, command=get2)
        novo_carreteiro.place(x=153, y=230)
        vrremun = Label(janela, text='Valor da Remuneração :')
        vrremun.place(x=10, y=260)
        novo_vrremun = Entry(janela)
        novo_vrremun.place(x=160, y=260, width=100)
        bt_salvar = Button(janela, text='Salvar', width=10, command=get_id2)
        bt_salvar.place(x=410, y=255)
        janela.geometry("530x300+100+100")
        janela.transient(menu)
        janela.focus_force()  #
        janela.grab_set()  #
        janela.mainloop()
    conn = sqlite3.connect('autonomos.db')
    cursor = conn.cursor()
    alterar = Toplevel ()
    alterar.geometry("530x300+100+100")
    lbemails = Listbox(alterar,width=60)
    lbemails.place(x=25, y=40)
    cursor.execute("""
    SELECT * FROM autonomos;
    """)
    for linha in cursor.fetchall():
        lbemails.insert(END,linha)
    conn.close()
    lblMat = Label(alterar,text="Escolha o Item Abaixo :")
    lblMat.place(x=200,y=20)
    lbemails = Button(alterar,text="Próximo >>",command=alterar_data)
    lbemails.place(x=409, y=235)
    alterar.mainloop()

def excluir () :
    excluir = Toplevel ()
    def get_id () :
        id = wd_id.get()
        conn = sqlite3.connect('autonomos.db')
        cursor = conn.cursor()
        cursor.execute("""
        DELETE from autonomos
        WHERE id = ?
        """, (id))
        conn.commit()
        print('Dados atualizados com sucesso.')
        conn.close()
    wd_id = Entry(excluir)
    wd_id.place(x=100, y=20)
    lb_wdid = Label(excluir, text="ID :")
    lb_wdid.place(x=10, y=20)
    a = Button(excluir, text="Excluir", command=get_id)
    a.place(x=250,y=55)
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
menu()
