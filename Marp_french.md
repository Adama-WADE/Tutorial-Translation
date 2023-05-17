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
## Data Loading and <br> Visualization Tutorial

---
<!-- footer: ![height:1.5cm](images/tinyPerk.jpg) ![height:1.5cm](images/tinyEbantica.jpg) "Laboratory for Percutaneous Surgery – Copyright © Queen’s University, 2022" ![height:1.5cm](images/tinySlicer.jpg) -->

# Tutorial Dataset

### Please download the following datasets:
<https://github.com/PerkLab/PerkLabBootcamp/raw/master/Data/VisualizationTutorial_HeadScene.mrb>

---
# Main user interface
![height:11cm](images/Slide-3.jpg)

---
# Load Sample MRI Data
![height:11cm](images/Slide-4.jpg)


---
# Load Sample MRI Data
![height:11cm](images/Slide-5.jpg)

---
<!-- _class: lead -->
![ bg right height:11cm](images/Slide-6.png)
## Load Sample MRI Data
###### The axial, sagittal, and coronal views automatically show  the loaded volume

---
## Adjust window/level
![bg right height:11cm](images/Slide-7.jpg)
##### Switch to window/level mouse mode

---
## Adjust window/level
![bg right height:11cm](images/Slide-8.png)
##### Adjust window/level (brightness/contrast) using the left mouse button on a slice view


---
### Switch back to view/transform mode
![height:11cm](images/Slide-9.jpg)

---
# Maximize view
![height:11cm](images/Slide-10.jpg)

---
# Slice view options
![bg right height:11cm](images/Slide-11.png)
##### Position your mouse cursor over the pin icon to display the slice view toolbar

---
# Slice view options
![ bg right height:11cm](images/Slide-12.jpg)
##### Once the slice viewer toolbar is shown, click on the “>>”.

---
# Show ruler
![height:11cm](images/Slide-13.jpg)

---
##### Rotate to volume plane
![bg right height:11cm](images/Slide-14.jpg)
###### Often, MRI volumes are not axis-aligned. To show the true axial view, click the **‘Rotate to volume plane’** button.
###### Note: This image will not be affected, but many DICOM MR images need to be aligned.

---
## Switch to conventional layout
![height:11cm](images/Slide-15.jpg)

---
# Link views
![bg right height:11cm](images/Slide-16.jpg)
After linking views, if any setting is changed in a 2D view, all others follow.

---
### Show slices in 3D
![bg right height:11cm](images/Slide-17.jpg)
Now the slice views are linked. If you click the **‘Toggle slice visibility in 3D view’** button, then all slices will show up.

---
# Show slices in 3D
![bg right height:11cm](images/Slide-18.png)
All three anatomical slices are shown in the 3D view.

---
# Navigating the 3D view
![bg right height:11cm](images/Slide-19.png)
Use the left mouse button to **rotate**, and the right mouse button to **zoom** in and out.

---
# Close the scene
![height:11cm](images/Slide-20.jpg)

---
### Part 2: 3D visualization of surface models of the brain
![height:11cm](images/Slide-21.png)

---
#### Load tutorial scene
![bg right height:11cm](images/Slide-22.jpg)
Drag and drop the file VisualizationTutorial_HeadScene.mrb into Slicer, then click **OK**.

---
# Center view
![bg right height:11cm](images/Slide-23.jpg)
Click on the small box icon to center the view, in 3D or in 2D

---
## Explore loaded data
![bg right height:11cm](images/Slide-24.jpg)
You can use the module list, or the favorite module toolbar to switch to the **Data module**

---
#### Explore loaded data
![bg right height:11cm](images/Slide-25.jpg)
###### The Data module shows all the data in the scene.
###### The data items (“nodes”) can be shown/hidden, renamed, deleted, cloned, etc.
###### Hide the **‘skin’** model by clicking the eye icon.
