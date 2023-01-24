# Ranking
petit projet pour le cours d'indexation web ENSAI 3A SID fait par Thomas Hilger. Le but est de coder un un ranking linéaire à aprtir d'un index.

## Quickstart 
Il faut d'abord convenir de la requête. Pour cela dans le fichier `main.py`, modifier l'argument de la fonction `launch_ranking` avec la rquête de votre choix.
Pour créer le ranking, il suffit de lancer à la racine du projet la commane `python main.py`. Le ranking nouvellement crée se trouvera dans le fichier json `results.json`. On y trouvera également quelques statistiques comme le nombre de docuemnt dans l'index et le nombre de document restant après filtrage sur la requête.

Pour lancer les tests, déplacez-vous dans le dossier test, puis lancez la commande `pytest`.

## Explication 

Le ranking est codé dans la classe Ranking. les grandes étapes sont :

- On écrit une requête.
- la requête est transformé (lowerisé, tokenisé)
- on filtre les docuemnts ayant dans leur titre les mêmes tokens que la requête
- on utilise la fonction bm25 pour créer le ranking 
- on stocke le ranking dans un fichier json à la racine du projet

