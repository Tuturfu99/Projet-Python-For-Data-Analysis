# Projet-Python-For-Data-Analysis
Projet Python For Data Analysis

Dataset : ONline news popularity

Dans ce projet, nous avons reçu un set de données concernant des articles 
d'acualités postés sur Internet. Ce set de données comprend 6 variables pour 
39 644 individus. Nous avons d'abord clarifié les données rentrées. On trouve 
parmi ces données, le nombre de partage de chaque article. 
Nous avons essayé de trouver un modèle suivant; avec un seuil de popularité 
situé à 1400 partages (les articles ayant plus de 1400 partages étant populaire,
les autres étant considérer comme non populaire), prédire la popularité d'un 
article donné. Il s'agit d'un problème de classification.

Nous avons d'abord essayé, à l'aide de différents graphiques, de repérer
des liens entre les données et la variable cible. Cela nous vous permettra
aussi de vous familiariser avec le dataset.

Ensuite, nous avons adatpé le dataset afin de pouvoir utiliser ces données
dans différents modèles de prédiction. Nous avons testé différents modèles, 
et cherché à obtenir les meilleurs paramètres à rentrer pour chacun d'entre
eux. Cette partie était assez coûteuse en temps de calcul. Enfin, nous avons 
comparé nos résultats, et nous avons gardé le modèle avec une plus grande
précision.

Notre modèle, le modèle des arbres aléatoires a une précision de 67.29%.
C'est à dire que pour 67.29% des cas, nous sommes capables de prédire la popularité
où l'impopularité d'un article. Ces chiffre paraît assez faible, d'autant plus
qu'il s'agit d'un problème de classification binaire. Cela peut être due au fait 
que d'autres facteurs agissant sur la cible n'ont pas été pris en compte. Ainsi, 
nous n'avons pas toute les informations nécessaires pour pouvoir établir le modèle.
Et enfin, une part d'aléatoire peut également jouer, notamment lorsqu'une personne
populaire partage l'article, cela peut influer sur le nombre de partage d'un 
article, et fausser notre système.

------------------------------------------------------

Déploiement de l'API :

Verifier tout d'abord que tout les fichiers nécessaires sont bien téléchargés au bon endroit :
index.html dans le dossier templates, style.css dans le dossier static et app.py et projetAPI.pickle 
dans le dossier principal.

 - Lancer le fichier app.py depuis un éxécuteur de commande (Anaconda Prompt par exemple)
 - Aller sur l'adresse web indiquée par l'éxécuteur de commande
 - Remplir le formulaire avec les données de l'article sur lequel on veut effectuer la prédiction 
   ATTENTION ( le jour de la semaine doit s'écrire avec un chiffre, Lundi=1;Mardi=2;Mercredi=3...)
 - La prédiction s'affichera dès que vous aurez appuyer sur le bouton 'Predict'
