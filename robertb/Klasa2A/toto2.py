#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

ileliczb = 6
zakres = 20
liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, zakres)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

typy = set()
i = 0
while i < ileliczb:
    #kom = "Podaj liczbę "+str(i+1)+":"
    typ = raw_input("Podaj liczbę "+str(i+1)+": ")
    if typ not in typy:
        typy.add(typ)
        i = i + 1

print "Wylosowane liczby: ",liczby
print "Typowane liczby: ",typy

trafione = set(liczby) & typy
print "Trafione liczby: ",trafione
