#!/usr/bin/python3

from jjcli import *
c=clfilter(opt="do:")

for page in c.slurp():
    nome = findall(r'<title>([\w \-]+)</title>', page)
    print(nome)
    #familiares = findall(r'<a\s+href=(.*?id=(\d+)"?)>(.*?)</a>', page)
    dataNascimento = findall(r'<div align="center">\s+(\*\s+\w+|\s+\+\s+\w+).*?<nobr>(\d+\.\d+\.\d+)</nobr>',page)
    filhos = findall(r'<LI><A HREF=pessoas.php\?id=(\d+)>\s+([\w \-]+)</A>',page)
    print("A DATA DE NASCIMENTO/MORTE É (* indica nascimento, + indica morte):")
    for data in dataNascimento:
        print(data)
    print("OS FILHOS DE "+nome[0]+" SÃO:")
    for id,nome in filhos:
        print(f"==> {id} {nome.strip()}")
    pai=findall(r'<B>Pai:</B>\s*?<A HREF=pessoas.php\?id=(\d+)>\s*?([\w \-]+)</A>',page)
    print("O PAI É:")
    for id,nome in pai:
        print(f"==> {id} {nome.strip()}")
    mae=findall(r'<B>Mãe:</B>\s*?<A HREF=pessoas.php\?id=(\d+)>\s*?([\w \-]+)</A>',page)
    print("A MAE É:")
    for id,nome in mae:
        print(f"==> {id} {nome.strip()}")
    