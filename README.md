# SoFAIR

T4.1 Support for the creation of annotated software mentions and disambiguations

SoFAIR Annotations Gold Standard Dataset 

The dataset to be used in the annotation process has been drawn from papers hosted by CORE. There are a total of 4058 papers split across 13 domains. All papers in the dataset have a DOI and the domain for each paper was identified from its DOI using an updated version of the methodology first introduced by [1]. 

The majority of papers have a single classification however some papers are classified with more than one label. These duplicate classifications are detailed in the duplicate_label_report contained in this repository. 

In addition to the PDF file, the following metadata is available for each paper:

core_id, 
title, 
DOI, 
domain, 
publication year. 

All papers are from 2019 onwards. 

There is a single zip file which contains 13 sub-directories, one per domain. Files are named as core_id.pdf. The zip file is too large for GitHub or GDrive storage so can be downloaded directly from CORE here: 

https://core.ac.uk/exports/SoFAIR_Annotation_Dataset.zip 

Additionally, there is a spreadsheet with the metadata for all papers included in this repository. 

[1] Waltman, Ludo, and Nees Jan Van Eck. "A new methodology for constructing a publication‐level classification system of science." Journal of the American Society for Information Science and Technology 63.12 (2012): 2378-2392.
