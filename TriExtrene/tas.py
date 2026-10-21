class Tas :
    def __init__(self, tas : list[int]) :
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

    def print(self):
        def _print_arbre(t, i=0, s="") :
            if (i < len(t) and t[i] is not None) :
                _print_arbre(t, 2*i + 2,s+"\t")
                print(f"{s}{t[i]}")
                _print_arbre(t, 2*i + 1,s+"\t")
                
        _print_arbre(self.tas)


if __name__ == '__main__' :

    tas = Tas([5,8,6,4,2,9,3,10,22,32,15])

    tas.print()