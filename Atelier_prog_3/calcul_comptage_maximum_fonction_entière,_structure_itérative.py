# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 09:25:03 2021

@author: alexa
"""
def somme_1(L :list) ->int:
    """Programme qui donne la somme d'un tableau
    input:
        L : une list d'entier
        e : un entier
    output:
        la somme des éléments du tableau
    """
    s = len(L)
    somme =  0
    for i in range(s):
        somme = somme + L[i]
    return somme

def somme_2(L :list) ->int:
    """Programme qui donne la somme d'un tableau
    input:
        L : une list d'entier
        e : un entier
    output:
        la somme du tableau
    """
    somme =  0
    for e in L:
        somme += e
    return somme

def somme_3(L :[int]) -> int:
    """Programme qui donne la somme d'un tableau
    input:
        L : une list d'entier
        e : un entier
    output:
        la somme du tableau
    """
    #variable
    somme =  0
    compteur = 0
    list_1 = len(L)
    while compteur < list_1:
        somme = somme + L[compteur]
        compteur = compteur + 1
    return somme

def test() -> None:
    """procédure de test des somme 1,2,3"""
    uneList = [5,9,12,3,6]
    print(somme_3(uneList))
#test()

def test_exercice1() ->None:
    """procédure de test"""
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme_3([]))
    #test somme 11111
    S=[1,10,100, 1000,10000]
    print("Test somme 1111 : ", somme_3(S))
#test_exercice1()

def moyenne(L: list) -> int:
    """Programme qui renvoie la moyenne de la liste
    input:
        L : une list d'entier
    output:
        renvoie la moyenne de la liste et renvoie zéro si elle est vide
    """
    if L == []:
        moyenne1 = 0.0
    else:
        s = len(L)
        moyenne1 = 0.0
        somme =  0
        for i in range(s):
            somme = somme + L[i]
        moyenne1 = somme / s
    return moyenne1

def test1() ->None:
    """procédure de test"""
    uneList = [5,9,12,3,6]
    print(moyenne(uneList))
#test1()

def nb_sup(L : list,e : float) ->list:
    """Programme qui renvoie les élements supérieur de la liste par rapport à e
    input:
        L : une list d'entier
        e : un réel
    output:
        renvoie une liste composé de tous les éléments de la liste qui sont
        supérieur à l'élément donné
    """
    s = len(L)
    compteur_sup = 0
    for i in range(s):
        if L[i] > e:
            compteur_sup = compteur_sup + 1
    return compteur_sup

def test2():
    """procédure de test"""
    uneList = [5,9,12,3,6]
    print(nb_sup(uneList, e = 5))
#test2()

def nb_sup2(L :list ,elt: float ) -> list:
    """Programme qui renvoie les élements supérieur de la liste par rapport à e
    input:
        L : une list d'entier
        e : un réel
    output:
        renvoie une liste composé de tous les éléments de la liste qui sont
        supérieur à l'élément donné
    """
    sup = []
    for e in L:
        if e > elt :
            sup.append(e)
    return sup

def test3():
    """procédure de test"""
    uneList = [5,9,12,3,6]
    print(nb_sup2(uneList, 5))
#test3()

def moy_sup(L : list,e : float)->int:
    """Programme qui renvoie la moyenne des élements supérieur de la liste par rapport à e
    input:
        L : une list d'entier
        e : un réel
    output:
        renvoie la moyenne des éléments de la liste qui sont supérieur à l'élément donné
    """
    s = len(L)
    sup = []
    for i in range(s):
        if L[i] > e:
            sup.append(L[i])
    return moyenne(sup)

def test4():
    """procédure de test"""
    uneList = [5,9,12,3,6]
    print(moy_sup(uneList, 5))
#test4()

def val_max(L : list) -> int:
    """Programme qui renvoie l'élément le plus grand de la liste
    input:
        L : une list d'entier
    output:
        int : renvoie l'élément le plus grand de la list
    """
    vmax = 0
    s = len(L)
    for i in range(s):
        if L[i] > vmax:
            vmax = L[i]
    return vmax

def ind_max(L : list) ->int:
    """Programme qui renvoie l'indice de l'élément le plus grand de la liste
    input:
        L : une list d'entier
    output:
        int : renvoie l'indice de l'élément le plus grand de la list
    """
    vmax = 0
    s = len(L)
    for i in range(s):
        if L[i] > vmax:
            vmax = i
    return vmax
    
