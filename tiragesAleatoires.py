# coding=UTF-8
from fonction import *

###########################
## DEFINITIONS GENERALES ##
###########################

positionSimu = 0

while (positionSimu < 231):
    # Définition des différentes grilles
    grilleChaud = []
    grilleFroid = []
    grilleHasard = []
    grilleConstante = []

    grilleFinale = []

    # Définition des différents histogramme
    histoBoules = CREATION_histoBoules()
    histoBoulesTrie = []

    histoGainsChaud = CREATION_histoGains()
    histoGainsFroid = CREATION_histoGains()
    histoGainsHasard = CREATION_histoGains()
    histoGainsConstante = CREATION_histoGains()

    gainsChauds = 0
    gainsFroids = 0
    gainsHasards = 0
    gainsConstants = 0

    coutTotal = 0

    positionTirage = 0

    ###############################
    ###############################
    ### AVEC TIRAGES ALEATOIRES ###
    ###############################
    ###############################

    # On ne joue pas le premier coup pour avoir des données
    grilleFinale = CREATION_grilleHasard()
    histoBoules = MAJ_histoBoules(grilleFinale, histoBoules)

    grilleConstante = CREATION_grilleHasard()  # On génère la grille constante

    while (positionTirage < NB_TIRAGE_SIMULE):

        histoBoulesTrie = TRIE_histoBoules(histoBoules)

        grilleChaud, grilleFroid = CREATION_grillesChaudFroid(histoBoulesTrie)
        grilleHasard = CREATION_grilleHasard()

        grilleFinale = CREATION_grilleHasard()

        histoGainsChaud, gainsChauds = MAJ_histoGain_GAIN(
            grilleChaud, grilleFinale, histoGainsChaud, gainsChauds)
        histoGainsFroid, gainsFroids = MAJ_histoGain_GAIN(
            grilleFroid, grilleFinale, histoGainsFroid, gainsFroids)
        histoGainsHasard, gainsHasards = MAJ_histoGain_GAIN(
            grilleHasard, grilleFinale, histoGainsHasard, gainsHasards)
        histoGainsConstante, gainsConstants = MAJ_histoGain_GAIN(
            grilleConstante, grilleFinale, histoGainsConstante, gainsConstants)

        histoBoules = MAJ_histoBoules(grilleFinale, histoBoules)

        coutTotal += MISE

        if (positionTirage % 100000 == 0):
            print(positionTirage)

        # print("## Tirage n : {} ##\n".format(positionTirage))

        # print("\tChaud    -> {}€ ".format(round(gainsChauds-coutTotal, 1)))
        # AFFICHE_histogrammeGains(histoGainsChaud, debut="\t\t")

        # print("\n\tFroid    -> {}€ ".format(round(gainsFroids-coutTotal, 1)))
        # AFFICHE_histogrammeGains(histoGainsFroid, debut="\t\t")

        # print("\n\tHasard   -> {}€ ".format(round(gainsHasards-coutTotal, 1)))
        # AFFICHE_histogrammeGains(histoGainsHasard, debut="\t\t")

        # print("\n\tConstant -> {}€ ".format(round(gainsConstants-coutTotal, 1)))
        # AFFICHE_histogrammeGains(histoGainsConstante, debut="\t\t")

        positionTirage += 1

    print("## Simulation avec tirages générés ##")
    print("{} grilles de jouées pour un total de {}€\n".format(
        NB_TIRAGE_SIMULE, coutTotal))

    print("\tChaud    -> {}€ ".format(round(gainsChauds-coutTotal, 1)))
    AFFICHE_histogrammeGains(histoGainsChaud, debut="\t\t")

    print("\n\tFroid    -> {}€ ".format(round(gainsFroids-coutTotal, 1)))
    AFFICHE_histogrammeGains(histoGainsFroid, debut="\t\t")

    print("\n\tHasard   -> {}€ ".format(round(gainsHasards-coutTotal, 1)))
    AFFICHE_histogrammeGains(histoGainsHasard, debut="\t\t")

    print("\n\tConstant -> {}€ ".format(round(gainsConstants-coutTotal, 1)))
    AFFICHE_histogrammeGains(histoGainsConstante, debut="\t\t")

    ENREGISTREMENT_fichierDonneesSimulees(
        histoGainsHasard, NOM_FICHIER_ENREGISTREMENT_DONNEES_HASARDS)
    ENREGISTREMENT_fichierDonneesSimulees(
        histoGainsConstante, NOM_FICHIER_ENREGISTREMENT_DONNEES_CONSTANTS)
    ENREGISTREMENT_fichierDonneesSimulees(
        histoGainsChaud, NOM_FICHIER_ENREGISTREMENT_DONNEES_CHAUDS)
    ENREGISTREMENT_fichierDonneesSimulees(
        histoGainsFroid, NOM_FICHIER_ENREGISTREMENT_DONNEES_FROIDS)

    positionSimu += 1
    print("Simu {}".format(positionSimu))
