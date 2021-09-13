# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:25:03 2021

@author: alexa
"""
def position(L: list, e: int) ->int:
    """Programme la position d'un entier rentré
    input:
        L : une list d'entier
        e : un entier
    output:
        position de l'entier dans le tableau, ou -1 s'il n'est pas présent
    """
    s = len(L)
    a = 0
    present = False
    for i in range(s):
        if e == L[i]:
            present = True
            a = i
    if not present:
        a = -1
    return a
#print(position([5,9,12,3,6], 6))

def position2(L: list, e: int) ->int:
    """Programme la position d'un entier rentré
    input:
        L : une list d'entier
        e : un entier
    output:
        position de l'entier dans le tableau, ou -1 s'il n'est pas présent
    """
    #variable
    s = len(L)
    a = 0
    present = False
    compteur = 0
    while not present and compteur < s:
        if e == L[compteur]:
            present = True
            a = compteur
        else:
            compteur = compteur + 1
    if not present:
        a = -1
    return a
#print(position2([5,9,12,3,6], 6))

def nb_occurence(L: list, e: int):
    """Programme qui renvoie combiende fois le chiffre est présent
    input:
        L : une list d'entier
        e : un entier
    output:
        le nombre de présence du chiffre rentré
    """
    #variable
    s = len(L)
    c = 0
    for i in range(s):
        if e == L[i]:
            c = c + 1
    return c
#print(nb_occurence([5,9,6,3,6,], 7))

def est_triee(L: list) -> bool:
    """Programme qui renvoie si la liste est triée dans l'ordre croissant
    input:
        L : une list d'entier
    output:
        booleen si la liste est triée ou non
    """
    #variable
    s = len(L)
    croissant = True
    i = L[0]
    for j in range(s):
        if i > j :
            croissant = False
            i = j
    return croissant
#print(est_triee([1,2,3,5,4]))

def est_triee2(L: list):
    """Programme qui renvoie si la liste est triée dans l'ordre croissant
    input:
        L : une list d'entier
    output:
        booleen si la liste est triée ou non
    """
    #variable
    croissant = True
    i = L[0]
    while croissant:
        if L[i] < L[i+1]:
            L[i] = L[i+1]
        else:
            croissant = False
    return croissant
#print(est_triee2([1,2,3,5,4]))

def position_tri(L: list, i: int) ->int:
    """Programme qui renvoie la position d'un élément d'un tableau trié par 
    recherche dichotomique
    input:
        L : une list d'entier
        i : entier
    output:
        position de l'élément
    """
    pos = True                     # à refaire 
    j = len(L) -1
    k = 0
    while k <= j:
        m = (k + j ) // 2
        if L[m] == i:
            return pos
        elif L[m] < i:
            k = m + 1
        else:
            j = m - 1
    return pos
#print(position([5,6,7,8,9], 5))

def a_repetitions(L: list) -> bool:
    """Programme qui vérifie s'il y a des répétitions
    input:
        L : une list d'entier
        e : entier
    output:
        booleen si la liste possède des répétitions
    """
    #variable
    present = False
    s = len(L)
    elt = 0
    T = []
    while not present and elt < s:
        if not L[elt] in T:
            T.append(L[elt])
        else:
            present = True
        elt = elt + 1
    return present

def test() -> None:
    """procédure de test pour a_repetition"""
    #test liste vide 
    print("resultat attendu -> False")
    print(a_repetitions([]))
    #test liste avec lément répété
    print("resultat attendu -> True")
    print(a_repetitions([5,5,6,7,8,9]))
    #test sans élément répété 
    print("resultat attendu -> False")
    print(a_repetitions([5,6,7,8,9]))
test()
