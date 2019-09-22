# coding=UTF-8
MISE = 2.2
JACKPOT = 8*10**6

NB_BOULES_NORMALES = 5

NUM_BOULE_MIN = 1

NUM_BOULE_MAX_NORMAL = 49
NUM_BOULE_MAX_COMP = 10

NOM_DOSSIER = "resultats"

NOM_FICHIER_TIRAGES = "{}/tiragesExistants.csv".format(NOM_DOSSIER)

NOM_FICHIER_ENREGISTREMENT_DONNEES_CHAUDS = "{}/hasardTiragesChauds.txt".format(
    NOM_DOSSIER)
NOM_FICHIER_ENREGISTREMENT_DONNEES_FROIDS = "{}/hasardTiragesFroids.txt".format(
    NOM_DOSSIER)
NOM_FICHIER_ENREGISTREMENT_DONNEES_HASARDS = "{}/hasardTiragesHasards.txt".format(
    NOM_DOSSIER)
NOM_FICHIER_ENREGISTREMENT_DONNEES_CONSTANTS = "{}/hasardTiragesContants.txt".format(
    NOM_DOSSIER)

LISTE_ANALYSE = [
    [NOM_FICHIER_ENREGISTREMENT_DONNEES_CHAUDS, "chauds"],
    [NOM_FICHIER_ENREGISTREMENT_DONNEES_FROIDS, "froids"],
    [NOM_FICHIER_ENREGISTREMENT_DONNEES_HASARDS, "hasards"],
    [NOM_FICHIER_ENREGISTREMENT_DONNEES_CONSTANTS, "constants"]
]

HISTOGRAMME_GAIN_VIERGE = [
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

NB_TIRAGE_SIMULE = 1*10**6
