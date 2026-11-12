from math import ceil, log2

def indice_milieu (indice) : 
    k = ceil(log2(indice + 2)) - 1

    borne_inf = 2**k - 1

    borne_sup = 2**(k+1) - 2

    milieu = (borne_inf + borne_sup) // 2

    return milieu

def indice_mirroir (indice) :
    k = ceil(log2(indice + 2)) - 1

    milieu = indice_milieu(indice)

    borne_inf_gauche = 2**k - 1

    borne_inf_droite = milieu + 1

    if indice <=  milieu :
        return borne_inf_droite + (indice - borne_inf_gauche)
    
    else :
        return borne_inf_gauche + (indice - borne_inf_droite)

def remonter_gauche(tab, indice) :
    indice_pere = (indice-1) // 2

    if indice_pere > 0 :
        if (tab[indice] < tab[indice_pere]) :
            tab[indice], tab[indice_pere] = tab[indice_pere], tab[indice]
            remonter_gauche(tab, indice_pere)

def remonter_droite(tab, indice) :
    indice_pere = (indice-1) // 2

    if indice_pere > 0 :
        if (tab[indice] > tab[indice_pere]) :
            tab[indice], tab[indice_pere] = tab[indice_pere], tab[indice]
            remonter_droite(tab, indice_pere)

def ajouterElement(tab, elem) :
    
    if len(tab) <= 1 : 
        n = len(tab)
        tab += [elem]
        return
    
    n = len(tab)
    tab += [elem]

    # Le cas où l'élément ajouté est dans le sous-arbre gauche de la racine
    if (n <= indice_milieu(n)) :
        # Si l'élément nouvellement ajouté (elem) est supérieur au père de l'élément qui devrait être à son mirroir, onn les swap
        m = indice_mirroir(n)
        indice_pere_mirroir = (m-1) // 2
        if (indice_pere_mirroir >= 1) :
            if (tab[n] > tab[indice_pere_mirroir]) :
                tab[n], tab[indice_pere_mirroir] = tab[indice_pere_mirroir], tab[n]

        # Remonter les éléments modifiés
        remonter_gauche(tab,n)
        remonter_droite(tab,indice_pere_mirroir)

    else :
        # Si l'élément nouvellement ajouté (elem) est inférieur à l'élément qui devrait être à son mirroir, onn les swap
        m = indice_mirroir(n)

        if (tab[n] < tab[m]) :
            tab[n], tab[m] = tab[m], tab[n]

        # Remonter les éléments modifiés
        remonter_gauche(tab,m)
        remonter_droite(tab,n)

def print_arbre(tas):
    def _print_arbre(t, i=0, s="",n=len(tas)) :
        if (i < len(t)) :
            _print_arbre(t, 2*i + 2,s+"\t")
            print(f"{s}{t[i]}")
            _print_arbre(t, 2*i + 1,s+"\t")
            
    _print_arbre(tas)

tas = [None]

print_arbre(tas)

ajouterElement(tas,27)

print_arbre(tas)

ajouterElement(tas,26)
print_arbre(tas)
ajouterElement(tas,43)
print_arbre(tas)
ajouterElement(tas,16)
print_arbre(tas)
ajouterElement(tas,12)
print_arbre(tas)
ajouterElement(tas,7)
print_arbre(tas)
ajouterElement(tas,4)

print_arbre(tas)
print(tas)