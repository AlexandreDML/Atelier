def separation(L: list):
    """Programme qui permet de séparer un tableau dans un autre 
    tableau et de ranger par chiffre négatif, 
    chiffre positif , et les zéro au centre
    
    input:
        L : list de chiffre non classés (pair/impair)
    output:
        une liste qui classe le tableau avec négatif, zéro, positif"""
        
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
