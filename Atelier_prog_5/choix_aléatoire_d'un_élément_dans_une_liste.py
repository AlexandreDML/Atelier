# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:39:41 2021

@author: alexa
"""
import random

def choose_element_list(list_in_which_to_choose: list) -> int:
    """
    programme qui permet de choisir un element au hasard dans une liste
    input:
        une liste d'element triee ou non
    output:
        un element de cette liste, choisi au hasard 
    """
    #variable
    len_liste = len(list_in_which_to_choose)
    int_aleatoire = 0
    
    ind = random.randint(0, len_liste-1)
    int_aleatoire = list_in_which_to_choose[ind]
    return int_aleatoire    
    
#print (choose_element_list([1,5,9,15,34,50,76,88,91]))

def test_choose_element():
    """
    programme de test
    """
    # Test de votre code
    lst_sorted=[i for i in range(10)]
    print('Liste triée de départ',lst_sorted)
    e1 = choose_element_list(lst_sorted)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = choose_element_list(lst_sorted)
    while e1 == e2:
        e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"
test_choose_element()