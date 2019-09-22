#coding=UTF-8
from fonction import *

for analyse in LISTE_ANALYSE:

    fichierCourant = open(analyse[0], 'r')
    ligneTempo = []

    nbDonnees = 0

    histoComplet = CREATION_histoGains()

    for ligne in fichierCourant:
        nbDonnees += 1
        ligneTempo = map(int, ligne.rstrip().split(";")) 
        for i in range(len(ligneTempo)):
            histoComplet[i][1] += ligneTempo[i]

    print("Méthode avec nombres {}".format(analyse[1]))
    print("{} simulations de {} tirages.\n".format(nbDonnees, NB_TIRAGE_SIMULE))

    AFFICHE_histogrammeGains(histoComplet)

    coutTotal = nbDonnees*NB_TIRAGE_SIMULE*MISE
    gainTotal = CALCUL_gains(histoComplet)

    print("\nSoit un coût de {}€".format(coutTotal))
    print("Pour un gain de {}€\n".format(gainTotal))
    print("Au final : {}€".format(gainTotal - coutTotal))
    print("Espérance : {}€".format((gainTotal - coutTotal)/(NB_TIRAGE_SIMULE*nbDonnees)))
    print("\n")

    fichierCourant.close()