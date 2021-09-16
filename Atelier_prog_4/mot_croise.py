# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:51:29 2021

@author: alexa
"""
def mots_nlettres(lst_mot :list, num:int) ->list:
    """programme qui renvoie les mots d'une liste dont la longueuer est égal à num
    input:
        une liste de mots
        un nombre qui représente la taille des mots à récupérer
    output:
        renvoie la liste de mot dont la longueur est égal à num
    """
    #variable
    lst_mot_n = []
    for mot in lst_mot:
        if len(mot) == num:
            lst_mot_n.append(mot)
    return lst_mot_n

def commence_par(mot: str, prefixe: str) -> bool:
    """
    programme qui définit par un booleen si le mot contient le prefixe entré
    input:
        on donne un mot et un prefixe
    output:
        renvoie true sur le mot contient le prefixe, sinon false
    """
    #variables
    commence = True
    len_prefixe = len(prefixe)
    compteur = 0
    while  commence and compteur < len_prefixe:
        if not mot[compteur] == prefixe[compteur]:
            commence = False
        compteur = compteur + 1
    return commence

def finit_par(mot: str, suffixe: str) -> bool:
    """
    programme qui définit par un booleen si le mot contient le suffixe entré
    input:
        on donne un mot et un suffixe
    output:
        renvoie true sur le mot contient le sufixz, sinon false
    """
    #variables
    len_mot = len(mot)
    len_suffixe = len(suffixe)
    finit = True
    soustraction = len_mot - len_suffixe
    compteur = 0
    while finit and soustraction < len_mot:
        if not mot[soustraction] == suffixe[compteur]:
            finit = False
        soustraction = soustraction + 1
        compteur = compteur + 1
    return finit

def commencent_par(lst_mot: list, prefixe: str) -> list:
    """
    programme qui va renvoyer l'ensemble des mots de la liste qui possède le prefixe
    input:
        on rentre une liste de mot et un prefixe
    output:
        nous renvoie une liste de mot qui commence par le prefixe donné
    """
    #variables
    len_liste = len(lst_mot)
    liste = []
    for i in range(len_liste):
        mot = lst_mot[i]
        if commence_par(mot, prefixe):
            liste.append(mot)
    return liste


def finissent_par(lst_mot: list, suffixe: str) -> list:
    """
    programme qui va renvoyer l'ensemble des mots de la liste qui possède le suffixe
    input:
        on rentre une liste de mot et un suffixe
    output:
        nous renvoie une liste de mot qui possède le suffixe
    """
    #variables
    len_liste = len(lst_mot)
    liste = []
    for i in range(len_liste):
        mot = lst_mot[i]
        if finit_par(mot, suffixe):
            liste.append(mot)
    return liste

def liste_mots(lst_mot: list,prefixe: str,suffixe :str, num: int) -> list:
    """
    programme qui renvoie une liste de mot dont les mots possèdent le prefixe et
    le suffixe et contenant le num

    input:
        on donne une liste de mot, suivit d'un prefixe et d'un suffixe, et de num
        la taille du mot recherché
    output:
        renvoie la liste de mot qui commence par le prefixe donné, se finissant
        par le suffixe et comportant le nombre de lettre donné par num
    """
    return mots_nlettres(commencent_par(finissent_par(lst_mot, suffixe), prefixe), num)

def dictionnaire(fichier: str) -> list:
    """
    programme
    input:
        un fichier
    output:
        une liste de mot
    """    
    #Exemple d’affichage du contenu d’un fichier de noms (profs.txt) comportant un nom par ligne)
    # ouverture du fichier en lecture (r=read)
    f=open(fichier,"r", encoding=("utf-8"))
    c=f.readline() #lecture d'une ligne dans une chaine
    # de caractères
    print("** Contenu du fichier **")
    while c!="" :
        print(c)
        c=f.readline()
    print("** fin **")
dictionnaire("littre.txt")
def test_execice1():
    """
        procédure de test
    """
    #variable
    lst_mot = ["jouer","bonjour", "punir", "jour", "aurevoir", "revoir","pouvoir", 
               "cour", "abajour","finir", "aimer"]
    mot_1 = str(input("rentrer un mot commencant par le prefixe jou :"))
    mot_2 = str(input("rentrer un mot ne commencant pas par le prefixe jou :"))
    prefixe = str(input("veuillez rentrer un prefixe :"))
    suffixe = str(input("veuillez rentrer un suffixe :"))
    num = int(input("veilllez entrer la taille du mot :"))
    #tests
    print("Résultat attendu : True")
    print(commence_par(mot_1, prefixe))
    print("Résultat attendu : False")
    print(commence_par(mot_2, prefixe))
    print(commencent_par(lst_mot, prefixe))
    print(finissent_par(lst_mot, suffixe))
    print(mots_nlettres(lst_mot, num))
    print(liste_mots(lst_mot, prefixe, suffixe, num))
#test_execice1()
