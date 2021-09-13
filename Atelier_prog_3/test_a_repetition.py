def test() -> None:
    """procédure de test pour a_repetition"""
    #test liste vide 
    print("resultat attendu -> False")
    print(a_repetitions([]))
    #test liste avec élément répété
    print("resultat attendu -> True")
    print(a_repetitions([5,5,6,7,8,9]))
    #test sans élément répété 
    print("resultat attendu -> False")
    print(a_repetitions([5,6,7,8,9]))
test()
