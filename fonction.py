# coding=UTF-8
from constantes import *
import random as r

# Grille
# [num1, num2, num3, num4, num5, numComp]


def MAJ_histoGain_GAIN(grilleJoueur, tirageOfficiel, histoGains, gains):
    # Calcul le gain pour un tirage et met à jour l'histogramme des gains

    # Input -> la grille jouée par le joueur et le tirage officiel
    # Output -> Le gain du joueur et l'histogramme

    bonNumero = 0
    numComp = False

    for g in range(0, NB_BOULES_NORMALES, 1):
        for t in range(0, NB_BOULES_NORMALES, 1):
            if grilleJoueur[g] == tirageOfficiel[t]:
                bonNumero += 1

    if grilleJoueur[NB_BOULES_NORMALES] == tirageOfficiel[NB_BOULES_NORMALES]:
        numComp = True

    if (bonNumero == 5 and numComp):
        histoGains[0][1] += 1
        gains += histoGains[0][0]
    elif (bonNumero == 5):
        histoGains[1][1] += 1
        gains += histoGains[1][0]

    elif (bonNumero == 4 and numComp):
        histoGains[2][1] += 1
        gains += histoGains[2][0]
    elif (bonNumero == 4):
        histoGains[3][1] += 1
        gains += histoGains[3][0]

    elif (bonNumero == 3 and numComp):
        histoGains[4][1] += 1
        gains += histoGains[4][0]
    elif (bonNumero == 3):
        histoGains[5][1] += 1
        gains += histoGains[5][0]

    elif (bonNumero == 2 and numComp):
        histoGains[6][1] += 1
        gains += histoGains[6][0]
    elif (bonNumero == 2):
        histoGains[7][1] += 1
        gains += histoGains[7][0]

    elif (bonNumero == 1 and numComp):
        histoGains[8][1] += 1
        gains += histoGains[8][0]
    elif (numComp):
        histoGains[8][1] += 1
        gains += histoGains[8][0]

    return(histoGains, gains)


def CREATION_histoGains():
    # Crée un histogramme des gains vierge
    histoGainVierge = [
        [JACKPOT, 0],
        [100000, 0],
        [1000, 0],
        [500, 0],
        [50, 0],
        [20, 0],
        [10, 0],
        [5, 0],
        [MISE, 0],
    ]
    return(histoGainVierge)


def MAJ_histoBoules(tirageOfficiel, histoBoules):
    # Mise à jour de l'histogramme des boules

    # Input -> le tirage officiel et l'ancien histogramme des boules
    # Output -> Nouvel histogramme des boules

    for i in range(0, NB_BOULES_NORMALES, 1):
        histoBoules[0][tirageOfficiel[i]-1][1] += 1
    histoBoules[1][tirageOfficiel[NB_BOULES_NORMALES]-1][1] += 1

    return(histoBoules)


def CREATION_histoBoules():
    # Crée un histogramme des boules vierge

    HISTOGRAMME_BOULE_VIERGE = [
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL + 1, 1)],
        [[i, 0] for i in range(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP + 1, 1)]
    ]
    return(HISTOGRAMME_BOULE_VIERGE)


def TRIE_histoBoules(histoBoules):
    # Trie un histogramme selon un ordre croissant

    # Input -> Histogramme boules non trié
    # Output -> Histogramme boules trié

    histoBoulesTrie = []  # Copie l'histogramme des boules sans liens
    histoBoulesTrie += [[[i[0], i[1]] for i in histoBoules[0]]]
    histoBoulesTrie += [[[i[0], i[1]] for i in histoBoules[1]]]

    histoBoulesTrie[0].sort(key=gestionTrieHisto, reverse=True)
    histoBoulesTrie[1].sort(key=gestionTrieHisto, reverse=True)

    return(histoBoulesTrie)


def gestionTrieHisto(val):
    # Gere le trie d'un histogramme via le 2nd elements

    return(val[1])


def CREATION_grillesChaudFroid(histoBoulesTrie):
    # Crée les grilles Chaud / Froid grâce à l'histo des boules triés par ordre croissant

    # Input -> Histogramme boules trié
    # Output -> Grilles selon la méthode : Nombre chaud, Nombre froid

    grilleChaud = []
    grilleFroid = []

    for i in range(0, NB_BOULES_NORMALES, 1):
        grilleChaud += [histoBoulesTrie[0][i][0]]
    grilleChaud += [histoBoulesTrie[1][0][0]]

    for i in range(NUM_BOULE_MAX_NORMAL-1, NUM_BOULE_MAX_NORMAL - 1 - NB_BOULES_NORMALES, -1):
        grilleFroid += [histoBoulesTrie[0][i][0]]
    grilleFroid += [histoBoulesTrie[1][NUM_BOULE_MAX_COMP-1][0]]

    return(grilleChaud, grilleFroid)


def CREATION_grilleHasard():
    # Crée une grille avec des numéros aux hasards

    numeroTempo = 0
    grilleHasard = []

    for i in range(0, NB_BOULES_NORMALES, 1):
        numeroTempo = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        while TEST_presence(grilleHasard, numeroTempo):
            numeroTempo = r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_NORMAL)
        grilleHasard += [numeroTempo]
    grilleHasard += [r.randint(NUM_BOULE_MIN, NUM_BOULE_MAX_COMP)]

    return(grilleHasard)


def TEST_presence(grille, numero):
    # Test si un numéro est présent dans la grille

    # Input -> La grille et le numéro
    # Output -> True / False

    for i in grille:
        if i == numero:
            return(True)
    return(False)


def CREATION_donneesDepuisFichier(nomFichier):
    # Crée une liste avec tous les tirages effectués

    # Input -> Nom du fichier contenant les tirages
    # Output -> Liste avec les tirages

    listeTirage = []
    f = open(nomFichier, "r")

    for ligne in f:
        listeTirage += [[
            map(int, ligne.rstrip().split(";")[:6]),
            ligne.rstrip().split(";")[6]
        ]]

    f.close()
    return(listeTirage)


def CALCUL_gains(histoGains):
    gain = 0
    for i in histoGains:
        gain += i[0]*i[1]
    return(gain)


def ENREGISTREMENT_fichierDonneesSimulees(histoGains, nomFichier):
    fichier = open(nomFichier, "a")

    fichier.write("{};{};{};{};{};{};{};{};{}\n".format(
        histoGains[0][1],
        histoGains[1][1],
        histoGains[2][1],
        histoGains[3][1],
        histoGains[4][1],
        histoGains[5][1],
        histoGains[6][1],
        histoGains[7][1],
        histoGains[8][1])
    )

    fichier.close()


def AFFICHE_histogrammeGains(histoGains, debut=""):
    # Affiche un histogramme de gains

    print("{}{} -> {}".format(debut, histoGains[0][0], histoGains[0][1]))
    print("{} {} -> {}".format(debut, histoGains[1][0], histoGains[1][1]))
    print("{}   {} -> {}".format(debut, histoGains[2][0], histoGains[2][1]))
    print("{}    {} -> {}".format(debut, histoGains[3][0], histoGains[3][1]))
    print("{}     {} -> {}".format(debut, histoGains[4][0], histoGains[4][1]))
    print("{}     {} -> {}".format(debut, histoGains[5][0], histoGains[5][1]))
    print("{}     {} -> {}".format(debut, histoGains[6][0], histoGains[6][1]))
    print("{}      {} -> {}".format(debut, histoGains[7][0], histoGains[7][1]))
    print("{}    {} -> {}".format(debut, histoGains[8][0], histoGains[8][1]))


def AFFICHE_grille(grille):
    grilleTrie = sorted(grille[:NB_BOULES_NORMALES]) + \
        [grille[NB_BOULES_NORMALES]]
    print("{} {} {} {} {} + {} ".format(grilleTrie[0], grilleTrie[1],
                                        grilleTrie[2], grilleTrie[3], grilleTrie[4], grilleTrie[5]))
