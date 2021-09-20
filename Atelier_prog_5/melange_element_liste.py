# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:45:41 2021

@author: alexa
"""
import random

def mix_list(list_to_mix: list) -> list:
    """
    programme qui mélange un liste
    input:
        une liste que l'on suppose triee
    output:
        une liste autre liste melangee
    """
    #variable
    liste_melange = []
    len_liste = len(list_to_mix)
    for i in range(len_liste):
        ind = random.randint(0, len_liste-1)
        liste_melange.insert(ind, list_to_mix[i])
    return liste_melange
#print (mix_list([1,5,9,15,34,50,76,88,91]))

def test_mix_list():
    """
    programme de test pour mix_list
    """
    # Test de votre code
    lst_sorted=[i for i in range(10)]
    print('Liste triée de départ',lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print('Liste mélangée obtenue',mixed_list)
    print('Liste triée de départ après appel à mixList, elle doit être inchangée',lst_sorted)
    #assert (cf. doc en ligne) permet de vérifier qu’une condition
    #est vérifiée en mode debug (désactivable)
    assert lst_sorted != mixed_list,"Les deux listes doivent être différente après l'appel à mixList..."
test_mix_list()
