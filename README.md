# CartFinder

CartFinder est un système de détection de chemin automatique (Pathfinder) fonctionnant avec un système de gestion du danger (Heatmap).

## Installation

1. Téléchargez le fichier `.zip` (bouton à côté de la section description tout en haut de la section des fichiers).
2. Décompressez-le pour obtenir le fichier `CartFinder.py`.

## Utilisation

### 1. Définir la carte
Définissez votre matrice/map sous forme de liste contenant des sous-listes pour les lignes :
* `"-0"` : Mur / Infranchissable
* `"0"` : Case sans danger
* `"1"` à `"4"` : Danger initial (`1` = petit danger, `4` = très grand danger)

```python
map_test = [
    ["0", "0", "0", "-0", "0"],
    ["0", "-0", "0", "4",  "0"],
    ["-0", "-0", "0", "0",  "0"]
]
```

### 2. Initialiser le Pathfinder
Créez l'instance de la classe en passant ces arguments : la variable de la map, le point de départ [ligne, col], des points additionnels optionnels [[l, c]], et l'arrivée [ligne, col].
```python
game = PathFinder(map_test, [0, 0], [[1, 2]], [0, 4])
```

### 3. Lancer la recherche
Lancez la fonction .Find() en spécifiant l'importance de la vitesse (pR) et l'importance de la sécurité (pS).
```python
result = game.Find(pR=2, pS=2)
```

### 4. Afficher le résultat
Vous pouvez ensuite afficher le chemin calculé ainsi que le score final.
```python
print("Chemin trouvé par le bot :", result[0] if result else "Aucun")
print("Score final :", result[1] if result else "N/A") 
``` 

## Fonctionnement
1. Propagation du danger : Dès l'initialisation, CartFinder augmente automatiquement la valeur de danger des cases situées autour des sources de danger initiales (Heatmap).
2. Génération des essais : Lors de l'appel à la méthode Find(), l'algorithme génère des tentatives pour atteindre chaque objectif l'un après l'autre.
3. Calcul du meilleur chemin : Au bout de 150 essais, il calcule le score des solutions trouvées avec la formule suivante:
$$score = -((nb\_cases \times pR) + (danger\_accumulé \times pS))$$
L'algorithme retient ensuite le chemin possédant le score le plus élevé (le moins négatif).

## License et autres
#### Ce script est sous licence GNU General Public License 3.0 (GPL 3.0).
#### La version en module sortira très bientôt

#### Contact: zedka450 (Discord) zedka.le.vrai.pro@gmail.com (e-mail)

#### Pourquoi le nom "CartFinder"?
C'est très simple: je voulais un nom simple, qui se retient, alors je me suis dit "C'est pour les cartes, alors Cart, et Finder pour pathfinder" et ça fait CartFinder.