#!/usr/bin/python3

from jjcli import *
c=clfilter(opt="do:")

for page in c.slurp():
    nome = findall(r'<title>([\w \-]+)</title>', page)
    print(nome[1])