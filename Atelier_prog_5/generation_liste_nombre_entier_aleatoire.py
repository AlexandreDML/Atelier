# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:03:25 2021

@author: alexa
"""
import random

def gen_list_random_int(int_binf = 0, int_bsup = 10) -> list:
    """fonction qui génère une liste de nombre aléatoire
    input:
        une liste de nombre aléatoire
    output:
        une liste de nombre compris entre inf et sup sinon une liste comrpis en
        0 et 10 (10 non inclus)
    """
    #variables
    int_nbr = []
    for i in range(int_binf, int_bsup):
        int_nbr.append(random.randrange(int_binf, int_bsup))    
    return int_nbr
print(gen_list_random_int())
