from random import randint

NB_MAX = 20

with open("fichier.txt", "w") as f :
    for _ in range(NB_MAX) :
        f.write(f"{randint(0,NB_MAX)}\n")