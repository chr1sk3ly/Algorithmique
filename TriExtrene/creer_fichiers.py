from random import randint

NB_MAX = 5

with open("fichier.txt", "w") as f :
    for _ in range(NB_MAX*2) :
        f.write(f"{randint(0,NB_MAX)}\n")