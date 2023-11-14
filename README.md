# Générateur de Prénoms

Ce programme Python permet de générer des prénoms en utilisant des syllabes stockées dans des fichiers de corpus de noms pour différentes langues. Il découpe les prénoms en syllabes, corrige la découpe si nécessaire, et collecte des statistiques sur les syllabes pour ensuite générer des prénoms aléatoires.

## Table des matières

- [Description](#description)
- [Prérequis](#prérequis)
- [Utilisation](#utilisation)
- [Exemple d'utilisation](#exemple-dutilisation)

## Description

Ce programme est composé de deux classes principales :

1. **Syllabe** : Cette classe découpe un prénom en syllabes, corrige la découpe si nécessaire, et stocke les probabilités d'apparition de la prochaine syllabe dans un dictionnaire.

2. **Generateur** : Cette classe charge les syllabes par langues et genre à partir de fichiers de prénoms, puis génère des prénoms aléatoires en utilisant les syllabes disponibles.

## Prérequis

Avant d'utiliser ce programme, assurez-vous d'avoir les prérequis suivants :

- Python 3.8 ou plus installé sur votre système.
- Les fichiers de corpus de prénoms pour les langues souhaitées.

## Utilisation

Pour utiliser le générateur de prénoms, suivez les étapes suivantes :

1. Importez les classes `Syllabe` et `Generateur` dans votre code Python.

2. Créez une instance de la classe `Generateur`.

3. Utilisez la méthode `generate_names` pour générer des prénoms en spécifiant le nombre de prénoms à générer, la langue, le genre, la longueur maximale, et si vous souhaitez générer des fichiers JSON avec les statistiques des syllabes.

4. Les arguments langue et genre de la méthode `generate_names` doivent être passés sous forme de liste.

5. Les prénoms générés sont uniques. Vous pouvez afficher le nombres d'itération que cela à pris pour générer le nombre de prénom demandés. Pour cela activer le paramètre `itération=True` dans `generate_names`.

5. Vous pouvez rajouter de nouvelle liste de prénoms si vous suivez la même structure que `Name-Corpora`

## Exemple d'utilisation

Voici un exemple d'utilisation du générateur de prénoms :

```python
# Exemple du générateur
if __name__ == "__main__":
    g = Generateur()
    g.generate_names(10, langue=["allemand", "arabe", "orc"], genre=["m"], max_length=8, generate_files=True)
```

output :

```
Prénom 1 : maknok
Prénom 2 : wodwórg
Prénom 3 : ogrul
Prénom 4 : oussamazorn
Prénom 5 : ayoub
Prénom 6 : bruder
Prénom 7 : taimim
Prénom 8 : morbash
Prénom 9 : dumbuk
Prénom 10 : gustav
```
