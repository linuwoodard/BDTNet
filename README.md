# BDTNet

The aim of this code base is creating a neural net capable of accuratly predicting optical and mechanical propoerties of a specific class of optomechanical device developed by F. Mayor, A. Primo, S. Malik, and S. Gyger in the Safavi-Naeini Lab at Stanford.  This device enables colocalization of high quality facotr opticla and mechanical modes which are interestign for the task of quantum transduction and frequency conversion.

This repository provides code is designed to enable rapid prediction of optical and mechanical quality facotrs of variants of the base design.  In particular, the model is trained to predict optical and mechanical properties based on displacements and scale changes in the etched crystal holes.

Due to symmetries in the crstal, only one fourth of the total crystal needs to be considered.  Every hole in the quarter of the crystal of interest is given and index and corresponding dx, dy, and scale parameters.  The blaboomerang type holes are scales in all dimensions according to the scale factor.  The boomerang-dagger holes have the length of the legs scaled according to the scale facotr.

Boomerang type hole:
![boomerang_type_hole](https://github.com/user-attachments/assets/140915b9-39f3-4844-90ad-ee6167f95757)

Boomerange-dagger type hole:
![boomerang_dagger_type_hole](https://github.com/user-attachments/assets/7b8010e7-eb88-4962-be7f-e16f2a390611)

Indexing and parameterization of the crystal:
![parameter_layout](https://github.com/user-attachments/assets/9aa47127-5da9-49ee-ad4d-6e292327e275)
