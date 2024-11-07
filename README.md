# BDTNet

The aim of this code base is creating a neural net capable of accuratly predicting optical and mechanical propoerties of a specific class of optomechanical device developed by F. Mayor, A. Primo, S. Malik, and S. Gyger in the Safavi-Naeini Lab at Stanford.  This device enables colocalization of high quality facotr opticla and mechanical modes which are interestign for the task of quantum transduction and frequency conversion.

This repository provides code is designed to enable rapid prediction of optical and mechanical quality facotrs of variants of the base design.  In particular, the model is trained to predict optical and mechanical properties based on displacements and scale changes in the etched crystal holes.

Due to symmetries in the crstal, only one fourth of the total crystal needs to be considered.  Every hole in the quarter of the crystal of interest is given and index and corresponding dx, dy, and scale parameters.  The blaboomerang type holes are scales in all dimensions according to the scale factor.  The boomerang-dagger holes have the length of the legs scaled according to the scale facotr.

Boomerang type hole:
![alt text](images/boomerang_type_hole.png)

Boomerange-dagger type hole:
![alt text](boomerang_dagger_type_hole.png)

Indexing and parameterization of the crystal:
![alt text](BDT parameterization.png)
