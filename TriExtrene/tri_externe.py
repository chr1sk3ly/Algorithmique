import os
from tas import Tas
from monotonie import Monotonie

MONOTONIE_DIR = "./monotonies"

def creerMonotonies(file_path) :
    os.system(f"rm {MONOTONIE_DIR}/*")

    nb_monotonies = 0
    monotonies_list = []
    with open(file_path, "r") as file :
        elem = file.readline()
        if(elem) : last_min = int(elem)

        # Parcourir un à un les éléments du fichier à trié
        while(elem) :
            elem = int(elem)

            # Cas où on ne peut plus insérer au monotonie suivante ou c'est le premier élément
            if elem < last_min or (elem == last_min and len(monotonies_list) == 0) :
                nb_monotonies += 1
                with open(f"{MONOTONIE_DIR}/monotonie{nb_monotonies}.txt","w") as f:
                    f.write(f"{elem}\n")
                monotonies_list.append(f"{MONOTONIE_DIR}/monotonie{nb_monotonies}.txt")
                last_min = elem

            #Cas où on peut insérer l'élément à la monotonie courante
            else :
                with open(monotonies_list[-1],"a") as f:
                    f.write(f"{elem}\n")
                last_min = elem
            elem = file.readline()
    return monotonies_list

def trier_monotonie(monotonies_list) :
    fichier_trie_path = "./fichier_trie.txt"

    tab_file = [open(path) for path in monotonies_list]

    f_trie = open(fichier_trie_path, "w")

    tas = Tas([])
    
    for file in tab_file :
        elem = file.readline()
        if elem :
            # Ajout au tas
            tas.ajout_au_tas(Monotonie(int(elem), file))

    tas.print()
    print("##################################\n")
    while tas.length :
        racine = tas.cueillir_racine()

        tas.print()
        print("##################################\n")

        f_trie.write(f"{racine.elem}\n")

        file = racine.path
        elem = file.readline()
        if elem :
            # Ajout au tas
            tas.ajout_au_tas(Monotonie(int(elem), file))

        elif  file in tab_file :
            tab_file.remove(file)

        else :
            continue

    tas.print()

    for file in tab_file :
        file.close()

    f_trie.close()

if __name__ == '__main__' :
    trier_monotonie(creerMonotonies("./fichier.txt"))