# -*- coding: utf-8 -*-
"""
Ce programme génère des prénoms en utilisant des syllabes stockées dans des
fichiers de corpus de noms pour différentes langues.
"""

import syllabe
import json
import random
import os


class Generateur:
    def __init__(self):
        """
        Initialise un générateur de prénoms en chargeant les syllabes par langue.
        """
        # Initialise un dictionnaire pour stocker les syllabes par langue
        self.syllabes_dict = {}

    def generate_names(self, n, langue=["francais"], genre=["m", "f", "x"],
                       max_length=8, generate_files=False, itération=False):
        """
        Génère et affiche des prénoms aléatoires basés sur les syllabes chargées.

        :param n: Le nombre de prénoms à générer.
        :param langue: Les langue des prénoms à générer
        (par défaut : "francais").
        :param genre: Les genres des prénoms à générer
        (par défaut : "m", "f", "x")
        :param max_length: La longueur maximale des prénoms générés
        (par défaut : 8).
        :param generate_files: Si vrai, génère des fichiers JSON avec les
        statistiques des syllabes (par défaut : False).
        :param itération: Si vrai, affiche le nombre d'itérations que cela a 
        pris pour générer les n prénoms
        """

        # Génére le dictionnaire selon les langues et genres
        self.syllabes_dict = self.get_syllabes_by_lang_and_sexe(
            langue, genre, generate_files)

        # Génère la liste de prénom selon les langues et genres
        liste_prenom_reels = Generateur.get_liste_prenom_by_lang_and_sexe(
            langue,
            genre)

        # Lève une erreur si il n'existe pas de syllabes pour la combinaison
        if not self.syllabes_dict:
            raise Exception(
                ("Désolé aucunes syllabes disponibles avec cette combinaison :"
                 + f"\n {langue} | {genre}"))

        # Créér un compteur
        self.itération = 0

        # Génère n prénoms
        liste_prenom = []
        while len(liste_prenom) < n:
            # Initialise le prénom
            prenom = ""

            # Choisis une syllabe de départ au hasard
            depart = random.choice(list(self.syllabes_dict.keys()))
            prenom += depart

            # Choisis la prochaine syllabe a partir de la première
            next_syllabe = random.choice(self.syllabes_dict[depart])
            prenom += next_syllabe

            # Boucle jusqu'a ce qu'il n'y est plus de prochaine syllabe disponible
            while (self.syllabes_dict.get(next_syllabe, False) and
                   len(prenom) <= max_length):
                # Sélectionne une syllabe suivante au hasard
                next_syllabe = random.choice(
                    self.syllabes_dict.get(next_syllabe))
                prenom += next_syllabe

            # Ajoute le prénom à la liste
            if prenom not in liste_prenom and prenom not in liste_prenom_reels:
                liste_prenom.append(prenom)

            # Incrémente un au compteur itération
            self.itération += 1

        # Affiche le(s) prénom(s) généré(s)
        for i, prenom in enumerate(liste_prenom, start=1):
            print(f"Prénom {i} : {prenom}")

        # Affiche les itérations si option est activé
        if itération:
            print(f"\n{n} prénoms générés en {self.itération} itérations")

    def get_liste_prenom_by_lang_and_sexe(langues_disponibles,
                                          genres_disponibles):
        """
        Charge les prénoms à partir de fichiers de prénoms par langue et genre.

        :param langues_disponible: Liste de langues dans lequel piocher les
        syllabes.
        :param genres_disponibles: Liste de genres dans lequel piocher les
        syllabes.

        :return: Une liste de prénoms selons des langues et genres.
        """

        # Initialise la liste de prénom
        liste_prenom = []

        # Recupère le nom des fichiers par rapport à : langues_disponibles
        noms_fichiers = [f for f in os.listdir(
            "Name-Corpora") if f.split(".")[0].split("-")[1] in langues_disponibles]

        # Parcours tout les fichiers prénom dans noms_fichiers
        for file in noms_fichiers:
            # Ouvre le fichier et récupère tout les prénoms selon les genres
            with open(f"Name-Corpora\\{file}", "r", encoding="ANSI") as f:
                liste_prenom.extend([line[2:].strip().lower()
                                     for line in f if line[0] in genres_disponibles])

        return liste_prenom

    def get_syllabes_by_lang_and_sexe(self,
                                      langues_disponibles,
                                      genres_disponibles,
                                      generate_files=False):
        """
        Charge les syllabes à partir de fichiers de prénoms par langue et genre.

        :param langues_disponible: Liste de langues dans lequel piocher les
        syllabes.
        :param genres_disponibles: Liste de genres dans lequel piocher les
        syllabes.
        :param generate_files: Si vrai, génère des fichiers JSON avec les
        statistiques des syllabes (par défaut : False).

        :return: Un dictionnaire de syllabes selon des langues et genres.
        """

        syllabes_dict = {}

        # Génère la liste de prénom selon les langues et genres
        liste_prenom = Generateur.get_liste_prenom_by_lang_and_sexe(
            langues_disponibles,
            genres_disponibles)

        # Parcours tout les prénoms
        for prenom in liste_prenom:
            syllabe.Syllabe(prenom)

        # Génère JSON si option est activée
        if generate_files:
            # Nom du fichier
            nom_fichier = ('-'.join(langues_disponibles)
                           + '-' + "".join(genres_disponibles))

            # Création du dossier "Syllabes"
            if not os.path.exists("Syllabes"):
                os.mkdir("Syllabes")

            # Sauvegarde les statistiques des syllabes dans un fichier JSON
            with open(f"Syllabes\\syllabes-{nom_fichier}.json", "w",
                      encoding="utf-8") as f:
                json.dump(syllabe.Syllabe.stat_syllabes, f, indent=2,
                          sort_keys=True, ensure_ascii=False)

        # Stocke les syllabes des prénoms et genres
        syllabes_dict = syllabe.Syllabe.stat_syllabes

        # Réinitialise le dictionnaire de statistiques pour la classe Syllabe
        syllabe.Syllabe.stat_syllabes = {}

        return syllabes_dict


# Exemple du générateur
if __name__ == "__main__":
    g = Generateur()
    g.generate_names(10, langue=["japonais", "allemand", "orc"], genre=[
                     "m", "f", "x"], max_length=5, generate_files=True, itération=True)
