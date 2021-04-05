#!/usr/bin/python3

from jjcli import *


c=clfilter(opt="do:")

for page in c.slurp():
    nome = findall(r'<title>([\w \-]+)</title>', page)
    print("NOME: "+nome[0]+"\n")
    nomeCasamento = findall(r'Casamentos</div><div align="center"></div><div align="center" style="margin-bottom: 15px;"><A href=pessoas.php\?id=(\d+)>\s+([\w \-]+)</A>',page)
    dataCasamento = findall(r'Casamentos</div><div align="center"></div><div align="center" style="margin-bottom: 15px;"><A href=pessoas.php\?id=(\d+)>\s+([\w \-]+)</A>\s+\*\s+<nobr>(\d+\.\d+\.\d+)</nobr></div>',page)
    print("CASAMENTOS CONHECIDOS DE "+nome[0]+":\n")
    if(nomeCasamento):
        print("CASOU COM "+nomeCasamento[0][1]+"\n")
    if(dataCasamento):
        print("DATA DO CASAMENTO: "+dataCasamento[0])
    #As regex da data de nascimento e de morte não estão 100% corretas. 
    dataNascimento = findall(r'<div align="center">\s+\*\s+([\w \-]+|[\w+\, \-]+)\s+<nobr>(\d+\.\d+\.\d+)?</nobr>',page)
    dataMorte = findall(r'\s+\+\s+([\w+\,?\s+?]+)\s+<nobr>(\d+\.\d+\.\d+)</nobr>',page)
    filhos = findall(r'<LI><A HREF=pessoas.php\?id=(\d+)>\s+([\w \-]+)</A>',page)
    print("A DATA DE NASCIMENTO É:")
    i = 0
    if(dataNascimento):
        data = dataNascimento[0]
        for record in data:
            print(data[i])
            i += 1
    print("A DATA DE MORTE É:")
    i = 0
    if(dataMorte):
        data = dataMorte[0]
        for record in data:
            print(data[i])
            i += 1
    print("\n")
    print("OS FILHOS DE "+nome[0]+" SÃO:")
    for id,nome in filhos:
        print(f"==> {id} {nome.strip()}")
    print("\n")
    pai=findall(r'<B>Pai:</B>\s*?<A HREF=pessoas.php\?id=(\d+)>\s*?([\w \-]+)</A>',page)
    print("O PAI DE É:")
    for id,nomePai in pai:
        print(f"==> {id} {nomePai.strip()}")
    mae=findall(r'<B>Mãe:</B>\s*?<A HREF=pessoas.php\?id=(\d+)>\s*?([\w \-]+)</A>',page)
    print("A MAE DE É:")
    for id,nomeMae in mae:
        print(f"==> {id} {nomeMae.strip()}")