# Accord Inter-Annotateur

Contenu du dépôt :
------------------------------

Corpus : répertoire contenant les fichiers d'annotation utilisés

Scripts : répertoire contenant différents programmes :
- kappa.py et kappadistance.py : outils de visualisation des résultats simulés sous la forme de courbes
- perf.py : outil d'interpolation et de calcul de l'écart maximal entre les courbes des différents corpus
- optimisation.py : outil de calcul de l'accord inter-annotateur (kappa de Fleiss) et du taux de variation d'une annotation de référence à partir de données réelles
- graphique_res_brute.py : outil de visualisation des résultats sur données réelles et de calcul de la droite d'ajustement linéaire

Outil de simulation :
- fichiers de code : *.cpp
- fichiers d'entête : *.hpp

Mode d'emploi :
------------------------------

Pour télécharger le projet : 
  - git clone https://github.com/MateoMalidin/StageAccord.git

pour mettre à jour un dépot local :
  - git pull origin master

Pour ajouter des modifications à un dépot local : 
  - git add <nom du fichier modifié>
  - git commit -m "description"
  
Pour ajouter des modifications à un dépot distant : 
  - git push origin master
