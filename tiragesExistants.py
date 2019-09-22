# coding=UTF-8
from fonction import *
import os

###########################
## DEFINITIONS GENERALES ##
###########################

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

date = ""

# On récupère tous les tirages déjà effectués
listeTirage = CREATION_donneesDepuisFichier(NOM_FICHIER_TIRAGES)
positionTirage = 0


##################################
##################################
### AVEC TIRAGE DEJA EFFECTUES ###
##################################
##################################


# On ne joue pas le premier coup pour avoir des données
grilleFinale = listeTirage[positionTirage][0]
histoBoules = MAJ_histoBoules(grilleFinale, histoBoules)

grilleConstante = CREATION_grilleHasard()  # On génère la grille constante

positionTirage += 1

while(positionTirage < len(listeTirage)):

    histoBoulesTrie = TRIE_histoBoules(histoBoules)

    grilleChaud, grilleFroid = CREATION_grillesChaudFroid(histoBoulesTrie)
    grilleHasard = CREATION_grilleHasard()

    grilleFinale = listeTirage[positionTirage][0]
    date = listeTirage[positionTirage][1]

    histoGainsChaud, gainsChauds = MAJ_histoGain_GAIN(
        grilleChaud, grilleFinale, histoGainsChaud, gainsChauds)
    histoGainsFroid, gainsFroids = MAJ_histoGain_GAIN(
        grilleFroid, grilleFinale, histoGainsFroid, gainsFroids)
    histoGainsHasard, gainsHasards = MAJ_histoGain_GAIN(
        grilleHasard, grilleFinale, histoGainsHasard, gainsHasards)
    histoGainsConstante, gainsConstants = MAJ_histoGain_GAIN(
        grilleConstante, grilleFinale, histoGainsConstante, gainsConstants)

    coutTotal += MISE

    # os.system("clear")

    # print("## Tirage du {} ##".format(date))
    # AFFICHE_grille(grilleFinale)

    # print("\n\n# Grille Chaude")
    # AFFICHE_grille(grilleChaud)
    # print("Gain : {} €".format(round(gainsChauds-coutTotal, 1)))

    # print("\n# Grille Froide")
    # AFFICHE_grille(grilleFroid)
    # print("Gain : {} €".format(round(gainsFroids-coutTotal, 1)))

    # print("\n# Grille Constantes")
    # AFFICHE_grille(grilleConstante)
    # print("Gain : {} €".format(round(gainsConstants-coutTotal, 1)))

    # print("\n# Grille Aléatoire")
    # AFFICHE_grille(grilleHasard)
    # print("Gain : {} €".format(round(gainsHasards-coutTotal, 1)))

    histoBoules = MAJ_histoBoules(grilleFinale, histoBoules)
    positionTirage += 1


os.system("clear")

print("## Simulation avec tirages existants ##")
print("{} grilles de jouées pour un total de {}€\n".format(
    len(listeTirage)-1, coutTotal))

print("\tChaud    -> {}€ ".format(round(gainsChauds-coutTotal, 1)))
AFFICHE_histogrammeGains(histoGainsChaud, debut="\t\t")

print("\n\tFroid    -> {}€ ".format(round(gainsFroids-coutTotal, 1)))
AFFICHE_histogrammeGains(histoGainsFroid, debut="\t\t")

print("\n\tHasard   -> {}€ ".format(round(gainsHasards-coutTotal, 1)))
AFFICHE_histogrammeGains(histoGainsHasard, debut="\t\t")

print("\n\tConstant -> {}€ ".format(round(gainsConstants-coutTotal, 1)))
AFFICHE_histogrammeGains(histoGainsConstante, debut="\t\t")
