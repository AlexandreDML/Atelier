# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 10:14:37 2021

@author: alexa
"""
import re

def full_name(str_arg: str)-> str:
    """
    fonction qui renvoie le nom en majuscule et la première lettre du prénom en
    minuscule.
    input:
        une chaine de caractère en minuscule
    output:
        une chaine de caractère en majuscule pour le nom et minuscule pour le
        prenom sauf la première lettre
    """
    #variables
    str_arg = "bisgambiglia paul"
    liste = str_arg.split(" ")
    #on modifie le nom et la première lettre du prenom
    liste[0] = liste[0].upper()
    liste[1] = liste[1].capitalize()
    str_arg = " ".join(liste)
    return str_arg
#print(full_name("bisgambiglia paul"))

#import re
#défini le schema d'un mail valide
REGEX = r'[A-Za-z0-9._-]+(\.[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}'
def is_mail(str_arg:str)->(int,int):
    """
    programme qui vérifie si un mail est valide
    input:
        un email
    output:
        renvoie un code erreur si le mail n'est pas valide ou un code de validité
    """
    #variables
    liste = []
    domaine = ""
    corps = ""
    erreur = (1,0)
    #on split regex en deux partie avec le @
    if not "@" in str_arg:
        erreur = (0, 2)
    else:
        liste = str_arg.split("@")
        corps = liste[0]
        domaine = liste [1]
        if not "." in domaine:
            erreur = (0, 4)
        else:
            if not re.match(r"[A-Za-z0-9._-]+(\.[A-Za-z0-9._-])*", corps):
                erreur = (0, 1)
            if not re.match(r"[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}", domaine):
                erreur = (0, 3)
    #on join les deux partie avec le @ qui a été enlevé lors du split
    str_arg = "@".join(liste)
    return erreur

def test_is_mail():
    """Procédure de test"""
    #variable
    code_mail_1 = "mael.belliard@laposte.net"
    code_mail_2 = "mael.belliard.laposte.net"
    code_mail_3 = "mael.belliard@%$ù**$.net"
    code_mail_4 = "mael.belliard@lapostenet"
    code_mail_5 = "mael.belliard@laposte.£%µ"
    code_mail_6 = "%=+@laposte.net"
    #test valide
    print("Résultat attendu : (1, 0)")
    print("Le mail", code_mail_1, "est un mail", is_mail(code_mail_1), "\n\n")
    #test sans le @
    print("Résultat attendu : (0, 2)")
    print("Le mail", code_mail_2, "est un mail", is_mail(code_mail_2), "\n\n")
    #test non de domaine non valide
    print("Résultat attendu : (0, 3)")
    print("Le mail", code_mail_3, "est un mail", is_mail(code_mail_3), "\n\n")
    #test sans le point
    print("Résultat attendu : (0, 4)")
    print("Le mail", code_mail_4, "est un mail", is_mail(code_mail_4), "\n\n")
    #test du .net
    print("Résultat attendu : (0, 3)")
    print("Le mail", code_mail_5, "est un mail", is_mail(code_mail_5), "\n\n")
    #test du corps 
    print("Résultat attendu : (0, 1)")
    print("Le mail", code_mail_6, "est un mail", is_mail(code_mail_6), "\n\n")
test_is_mail()
