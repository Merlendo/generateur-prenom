# -*- coding: utf-8 -*-
"""
Class qui découpe un prenom en syllabe et stocke les probabilités d'apparition
de la prochaine syllabe dans un dictionnaire.
"""

# Liste des voyelles et caractères spéciaux considérés comme voyelles
VOYELLE = "aeiouyáâãäèéêëíîïòóôöōùúûüū"


class Syllabe:
    # Dictionnaire de statistiques de syllabes
    stat_syllabes = {}

    def __init__(self, prenom):
        """
        Initialise une instance de la classe Syllabe en découpant un prénom en
        syllabes, en corrigeant la découpe si nécessaire et en collectant des
        statistiques sur les syllabes.

        :param prenom: Le prénom à analyser.
        """
        self.syllabes = Syllabe.get_syllabe(prenom)
        self.syllabes = Syllabe.correction_syllabe(self)  # Correction syllabes
        Syllabe.get_stat_syllabe(self)

    def get_syllabe(prenom):
        """
        Retourne les syllabes d'un prénom donné.

        :param prenom: Le prénom à découper en syllabes.

        :return: Une liste de syllabes.
        """
        prenom = prenom.lower()
        pos_voyelle = [i for i, v in enumerate(prenom) if v in VOYELLE]
        syllabes = []
        for i, p in enumerate(pos_voyelle):
            # Cas si la voyelle n'est pas en première position
            if p != 0:
                voyelle = prenom[p]
                if prenom[p-1] not in VOYELLE:
                    consonne_accroche = prenom[p-1]
                else:
                    consonne_accroche = ""
                queue = ""
                # Dernière voyelle
                if i == len(pos_voyelle)-1:
                    # Récupère la fin de la syllabe :
                    queue = prenom[p+1:]

                # Première voyelle
                elif i == 0 and p != len(prenom)-1:
                    # Récupère le début de la syllabe :
                    consonne_accroche = prenom[:p]
                    # Fin de la syllabe jusque à la prochaine consonne d'accroche :
                    queue = prenom[p+1:pos_voyelle[i+1]-1]

                else:
                    queue = prenom[p+1:pos_voyelle[i+1]-1]

                # Assemblage de la syllabe :
                syllabe = consonne_accroche + voyelle + queue
                syllabes.append(syllabe)

            # Cas lorsque la voyelle est en première position
            else:
                try:
                    voyelle = prenom[p]
                    queue = prenom[p+1:pos_voyelle[i+1]-1]
                    syllabe = voyelle + queue
                    syllabes.append(syllabe)
                except IndexError:
                    print(prenom)

        return syllabes

    def correction_syllabe(self):
        """
        Corrige la découpe en syllabe en fusionnant des syllabes si nécessaire.

        :return: Une liste de syllabes corrigées.
        """
        new_syllabe = []
        i = 0
        while i <= len(self.syllabes)-1:
            current_syllabe = self.syllabes[i]

            # Vérifie qu'il existe une prochaine syllabe
            try:
                next_syllabe = self.syllabes[i+1]

                # Concatenate deux syllabe si voyelle à la fin et début :
                if (current_syllabe[-1] in VOYELLE and
                        next_syllabe[0] in VOYELLE):
                    new_syllabe.append(current_syllabe+next_syllabe)
                    i += 1

                # Concatenate deux syllabe si lettre fin égal lettre début :
                elif current_syllabe[-1] == next_syllabe[0]:
                    new_syllabe.append(current_syllabe+next_syllabe)
                    i += 1

                else:
                    new_syllabe.append(current_syllabe)

            except IndexError:
                new_syllabe.append(current_syllabe)

            i += 1

        return new_syllabe

    def get_stat_syllabe(self):
        """
        Collecte des statistiques sur les syllabes du prénom.
        """
        for i in range(len(self.syllabes)-1):
            Syllabe.stat_syllabes[self.syllabes[i]] = Syllabe.stat_syllabes.get(
                self.syllabes[i], list()) + [self.syllabes[i+1]]
