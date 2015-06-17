#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

#liczba = random.randint(1, 10)
#print liczba
ileliczb = 5
liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1, 10)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

for i in range(3):
    odp = raw_input("Jaką liczbę od 1 do 10 mam na myśli? ")
    print odp

    if liczba == int(odp):
        print "Zgadłeś!"
    else:
        print "Błąd, spróbuj jeszcze raz."

print liczba
