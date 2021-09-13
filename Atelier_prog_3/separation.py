# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:25:03 2021

@author: alexa
"""
def separation(L: list):
    """Programme qui permet de separer un tableau dans un autre
    tableau et de ranger par chiffre negatif,
    chiffre positif , et les zero au centre
    input:
        L : list de chiffre non classes (pair/impair)
    output:
        une liste qui classe le tableau avec negatif, zero, positif"""
    #variables
    s = len(L)
    Lsep = []
    for i in range(s):
        t = len(Lsep)
        if L[i] < 0:
            Lsep.insert(0, L[i])
        elif L[i] > 0:
            Lsep.insert(t, L[i])
        else:
            if t % 2 == 0:
                Lsep.insert(int(t/2), L[i])
    return Lsep
print(separation([-1,2,0,8,-9,-1,4,6,0,8,-7,4,0,1,1,9,-3,0,4,-2, 2]))
