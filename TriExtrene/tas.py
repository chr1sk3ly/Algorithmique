class Tas :
    def __init__(self, tas) :
        self.length = 0
        self.tas = self._creerTas(tas)

    def _creerTas(self, tab) :
        # Créer un tas vide
        tas = []

        # ajouter dans le tas un élément
        for i in range(len(tab)) :
            self.ajouter(tas, tab[i])

        return tas

    def ajouter(self, tas , elem) :
        # ajouter l'élément à la fin du tas
        tas += [elem]
        self.length += 1
        # Cas où c'est le seul élement
        if (len(tas) == 1) :
            return tas

        # Sinon
        else :
            # remonter l'élément tant que c'est possible

            indice = len(tas) - 1
            # Si l'indice est impair (pour des langages à 0-base index), on est au fils gache (Les fils sont 2*i+1 et 2*i+2)
            if (indice & 1) :
                indice_pere = (indice - 1) // 2
            else :
                indice_pere = (indice - 2) // 2

            while(indice!=0 and tas[indice_pere]>tas[indice]) :
                # Permuter le père et le fils
                tas[indice],tas[indice_pere] = tas[indice_pere], tas[indice]

                # Mettre à jour indice et indice_père
                indice = indice_pere
                if(indice & 1) :
                    indice_pere = (indice - 1) // 2
                else :
                    indice_pere = (indice - 2) // 2

            return tas
        
    def ajout_au_tas(self, elem) :
        self.tas = self.ajouter(self.tas, elem)

    def cueillir_racine(self) :
        racine = self.tas[0]
        p = self.length - 1
        self.tas[0] = self.tas[p]
        # Faire remonter les fils
        i = 0
        fini = False
        while (i < p//2 and not fini) :
            if (p == 2*i + 1 or self.tas[2*i+1] < self.tas[2*i + 2]) :
                j = 2*i + 1
            else :
                j = 2*i + 2

            if self.tas[i] > self.tas[j] :
                self.tas[i], self.tas[j] = self.tas[j], self.tas[i]
                i = j
            else :
                fini = True
        self.tas.pop(-1)
        self.length -= 1
        return racine

    def print(self):
        def _print_arbre(t, i=0, s="",n=self.length) :
            if (i < len(t) and t[i] is not None) :
                _print_arbre(t, 2*i + 2,s+"\t")
                print(f"{s}{t[i]}")
                _print_arbre(t, 2*i + 1,s+"\t")
                
        _print_arbre(self.tas)


if __name__ == '__main__' :

    tas = Tas([5,8,6,4,2,9,3,10,22,32,15])

    tas.ajout_au_tas(1)

    tas.print()