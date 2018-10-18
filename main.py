
from tkinter import *
from xml.dom.minidom import Text

def cadastro() :
    janela = Tk()
    janela.geometry("800x600+100+100")
    janela.mainloop()

def cod () :

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

    dmDev.appendChild(infoComplCont)
    infoComplCont.appendChild(codCBO)

    #receive data
    ident = str(wd00.get())
    a = str (wd01.get())
    b = str (wd02.get())
    c = str (wd03.get())
    d = str (wd04.get())
    e = str (wd05.get())
    f = str (wd06.get())
    g = str (wd07.get())
    h = str (wd08.get())
    i = str (wd09.get())
    j = str (wd10.get())
    k = str (wd11.get())
    l = str (wd12.get())
    m = str (wd13.get())
    n = str (wd14.get())
    o = str (wd15.get())
    p = str (wd16.get())
    q = str (wd17.get())
    r = str (wd18.get())
    #s = wd19
    #t = wd20
    #u = wd21

    # atributes
    root.setAttribute('xmlns', 'http://www.esocial.gov.br/schema/evt/evtRemun/v02_04_02')
    evtRemun.setAttribute('Id', ident)

    # text mode in child
    txt1 =doc.createTextNode(a)
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


'''  txt22 = doc.createTextNode(itensremun[0])
    codRubr.appendChild(txt22)

    txt23 = doc.createTextNode(itensremun[1])
    ideTrabRubr.appendChild(txt23)

    txt24 = doc.createTextNode(itensremun[2])
    vrRubr.appendChild(txt24)'''

#gui

janela = Tk()

dist = 160
lb_dist = 30

wd00 = Entry(janela)
wd00.place(x=500,y=30)

lb00 = Label(janela, text = "IndRetif :",)
lb00.place(x=lb_dist,y=30)

wd01 = Entry(janela)
wd01.place(x=dist,y=30)

lb01 = Label(janela, text = "indApuracao :",)
lb01.place(x=lb_dist,y=60)

wd02 = Entry(janela)
wd02.place(x=dist,y=60)

lb02 = Label(janela, text = "perApur :",)
lb02.place(x=lb_dist,y=90)

wd03 = Entry(janela)
wd03.place(x=dist,y=90)

lb03 = Label(janela, text = "tpAmb :",)
lb03.place(x=lb_dist,y=120)

wd04 = Entry(janela)
wd04.place(x=dist,y=120)

lb04 = Label(janela, text = "procEmi :",)
lb04.place(x=lb_dist,y=150)

wd05 = Entry(janela)
wd05.place(x=dist,y=150)

lb05 = Label(janela, text = "verProc :",)
lb05.place(x=lb_dist,y=180)

wd06 = Entry(janela)
wd06.place(x=dist,y=180)

lb06 = Label(janela, text = "tpInsc :",)
lb06.place(x=lb_dist,y=210)

wd07 = Entry(janela)
wd07.place(x=dist,y=210)

lb07 = Label(janela, text = "nrInsc :",)
lb07.place(x=lb_dist,y=240)

wd08 = Entry(janela)
wd08.place(x=dist,y=240)

lb08 = Label(janela, text = "cpfTrab :",)
lb08.place(x=lb_dist,y=270)

wd09 = Entry(janela)
wd09.place(x=dist,y=270)

lb09 = Label(janela, text = "nisTrab :",)
lb09.place(x=lb_dist,y=300)

wd10 = Entry(janela)
wd10.place(x=dist,y=300)

lb10 = Label(janela, text = "nmTrab :",)
lb10.place(x=lb_dist,y=330)

wd11 = Entry(janela)
wd11.place(x=dist,y=330)

lb11 = Label(janela, text = "dtNascto :",)
lb11.place(x=lb_dist,y=360)

wd12 = Entry(janela)
wd12.place(x=dist,y=360)

lb12 = Label(janela, text = "ideDmDev :",)
lb12.place(x=lb_dist,y=390)

wd13 = Entry(janela)
wd13.place(x=dist,y=390)

lb13 = Label(janela, text = "codCateg :",)
lb13.place(x=lb_dist,y=420)

wd14 = Entry(janela)
wd14.place(x=dist,y=420)

lb14 = Label(janela, text = "tpInsc2 :",)
lb14.place(x=lb_dist,y=450)

wd15 = Entry(janela)
wd15.place(x=dist,y=450)

lb15 = Label(janela, text = "nrInsc2 :",)
lb15.place(x=lb_dist,y=480)

wd16 = Entry(janela)
wd16.place(x=dist,y=480)

lb16 = Label(janela, text = "codLotacao :",)
lb16.place(x=lb_dist,y=510)

wd17 = Entry(janela)
wd17.place(x=dist,y=510)

lb17 = Label(janela, text = "codCBO :",)
lb17.place(x=lb_dist,y=540)

wd18 = Entry(janela)
wd18.place(x=dist, y=540)

bt = Button(janela, text="Exportar", width=10, command=cadastro)
bt.place(x=500,y=100)

janela.geometry("800x600+100+100")
janela.mainloop()
