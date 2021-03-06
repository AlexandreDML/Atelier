# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:02:02 2021

@author: alexa
"""
import random
def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int) -> list:
    """
    programme qui va extraire de manière aléatoire une quantitée de chiffre voulu
    dans une autre liste
    input:
        une liste triée
    output:
        une liste d'éléments choisi au hasard
    """
    #variable
    liste = []
    len_liste = len(list_in_which_to_choose)
    elt= 0
    while elt < int_nbr_of_element_to_extract:
        ind = random.randint(0, len_liste-1)
        liste.append(list_in_which_to_choose[ind])
        elt = elt +1
    return liste

def test_extract():
    """
    programme de test de la fonction extract_elements_list
    """
    # Test de votre code
    lst_sorted=[i for i in range(10)]
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)
test_extract()
