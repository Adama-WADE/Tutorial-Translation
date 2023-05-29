---
marp: true
theme: uncover
paginate: true
style: |
    section{
      width: 32cm;
      height: 19cm;
      justify-content: flex-start;
    }
    section.lead h6 {text-align: bottom;}
    section.lead header {font-weight: bold;}
    
---

[comment]: <> (Header ends here)

![3d slicer logo](images/3D-Slicer-logo.jpg)
# 3D Slicer

Now the slice views are linked. If you click the **‘Basculez la visibilité dans la vue 3D’** button.
Ainsi toutes les coupes s'afficheront.


## Tutoriel de chargement et de visualisation de données

---
<!-- footer: ![height:1.5cm](images/tinyPerk.jpg) ![height:1.5cm](images/tinyEbantica.jpg) "Laboratory for Percutaneous Surgery – Copyright © Queen’s University, 2022" ![height:1.5cm](images/tinySlicer.jpg) -->

# Jeu de donées du tutoriel

### Veuillez télécharger les jeux de données suivants:
<https://github.com/PerkLab/PerkLabBootcamp/raw/master/Data/VisualizationTutorial_HeadScene.mrb>

---
# Interface principale
![height:11cm](images/Slide-3.jpg)

---
# Charger l'échantillon de données IRM
![height:11cm](images/Slide-4.jpg)


---
# Charger l'échantillon de données IRM
![height:11cm](images/Slide-5.jpg)

---
<!-- _class: lead -->
![ bg right height:11cm](images/Slide-6.png)
## Charger l'échantillon de données IRM
###### Les vues axiales,sagittales, et coronales affichent automatiquement le volume

---
## Ajuster le paramètre fenêtre/niveau
![bg right height:11cm](images/Slide-7.jpg)
##### Passer au mode fenêtre/niveau souris

---
## Ajuster le paramètre fenêtre/niveau
![bg right height:11cm](images/Slide-8.png)
##### Ajuster le paramètre fenêtre/niveau (brightness/contrast) using the left mouse button on a slice view


---
### Retournez au mode vue/transformation
![height:11cm](images/Slide-9.jpg)

---
# Maximisez ma vue
![height:11cm](images/Slide-10.jpg)

---
# Options de la vue de la couipe
![bg right height:11cm](images/Slide-11.png)
##### Placez le curseur sur l'icone de la punaise pour afficher la barre d'outils de la vue

---
# Options de la vue de la couipe
![ bg right height:11cm](images/Slide-12.jpg)
##### Une fois la barre d'outils affichée, cliquez sur  “>>”.

---
# Afficher la règle
![height:11cm](images/Slide-13.jpg)

---
##### Tournez le plan du volume
![bg right height:11cm](images/Slide-14.jpg)
###### Often, MRI volumes are not axis-aligned. To show the true axial view, click the **‘Tournez le plan du volume’** button.
###### Note: Cette image ne sera âs affectée, mais plusieurs images ?R DICOM doivent être alignées.

---
## Retour à la vue conventionnelle
![height:11cm](images/Slide-15.jpg)

---
# Connecter les vues
![bg right height:11cm](images/Slide-16.jpg)
After linking views, if any setting is changed in a 2D view, all others follow.

---
### Afficher les vues 3D
![bg right height:11cm](images/Slide-17.jpg)
Now the slice views are linked. If you click the **‘Basculez la visibilité dans la vue 3D’** button, then all slices will show up.

---
# Afficher les vues 3D
![bg right height:11cm](images/Slide-18.png)
All three anatomical slices are shown in the 3D view.

---
# Naviguer entre les vues 3D
![bg right height:11cm](images/Slide-19.png)
Use the left mouse button to **rotate**, and the right mouse button to **zoom** in and out.

---
# Fermer la scène
![height:11cm](images/Slide-20.jpg)

---
### Partie 2: Visualisation 3D des modèles de surface du cerveau
![height:11cm](images/Slide-21.png)

---
#### Charger la scène du tutoriel
![bg right height:11cm](images/Slide-22.jpg)
Drag and drop the file VisualizationTutorial_HeadScene.mrb into Slicer, then click **OK**.

---
# Centrer la vue
![bg right height:11cm](images/Slide-23.jpg)
Click on the small box icon to center the view, in 3D or in 2D

---
## Explorer les données chargées
![bg right height:11cm](images/Slide-24.jpg)
You can use the module list, or the favorite module toolbar to switch to the **Data module**

---
#### Explorer les données chargées
![bg right height:11cm](images/Slide-25.jpg)
###### Le module Data affiche toutes les données de la scène.
###### Les noeuds peuvent être affichés ou cachés, renommés, supprimés, clonés, etc.
###### Cachez le modèle  **‘peau’** en cliquant sur l'icone de l'oeil.
