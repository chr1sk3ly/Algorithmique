#ifndef ARBRE_H

#define ARBRE_H

typedef struct Arbre{
	int val ;
	Arbre *sg, *sd, *p ;
} Arbre;

Arbre* creerArbre(int a, Arbre* a1, Arbre* a2) ;

int taille(Arbre* a) ;

int hauteur(Arbre* a) ;

void parcours_prefix(Arbre* a) ;

void parcours_infixe(Arbre* a) ;

void parcours_postfixe(Arbre* a) ;

#endif
