# SoFAIR Dataset

This repository belongs to the Work Package T4.1, "Support for the creation of annotated software mentions and disambiguations"

### SoFAIR Gold Standard Dataset 

Description: 

* `documents/` contains the selection of scientific articles used in the annotation process. 

* `guidelines/` 

* `benchmarks/`

The documents are organized as follow: 

* `documents/tei-pre-annotated/`: the articles in XML, extracted from the PDF, with software mentions pre-annotated by the SoftCite Software Mentions Recognizer. Pre-annotations are only present to help the annotaters, they have to be checked entirely, and non pre-annotated passages must also be examinedandannotated. 

* `documents/tei-annotated/`: the articles manually annoated in XML format, as expected by the Softcite Software Mention Recognizer to train machine learning models

* `documents/tei-annotated/`: the articles afer manual expert validation and enrichment, this will be used as final gol standard corpus to be published

* `documents/metadata/`: the metadata information required for attribution under the CC-BY license, to be added in the final dataset for publication. 

* `documents/grobid/`: the full TEI XML extraction from PDF as produced by GROBID, to be used to compile the final dataset.

* `documents/test/`: a small test set that should be ignored. 

#### Selection of articles

This repository contains the selection of scientific articles to be used in the annotation process. 

These articles has been drawn from documents hosted by CORE. The document are split across 13 domains. All papers in the dataset have a DOI and the domain for each paper was identified from its DOI using an updated version of the methodology first introduced by [1]. 

The majority of papers have a single domain classification, however some papers are classified with more than one domain. These duplicate domain classifications are detailed in the file duplicate_label_report_all_domains.csv contained in this repository. 

In addition to the PDF file, the following metadata is available for each paper:

core_id, 
title, 
DOI, 
domain, 
publication year. 

All papers are from 2019 onwards. 

* first set of articles: 

There is a single zip file which contains 13 sub-directories, one per domain. Files are named as core_id.pdf. The zip file is too large for GitHub or GDrive storage so can be downloaded directly from CORE here: 

https://core.ac.uk/exports/SoFAIR_Annotation_Dataset.zip 

Warning: this set contains many non CC-BY articles that are not sharable and cannot be modified. The subset of CC-BY articles is available in the file `documents/SoFAIR-corpus-first-subset-cc-by.json` and only this subset should be considered for annotation. The non CC-BY articles must be ignored. 

* Extension articles: 

A second set of articles (called `extension`) to the above dataset can be downloaded from the following link:

https:://core.ac.uk/exports/SoFAIR_Annotation_Dataset_Extension.zip

This additional file contains an additional 1265 papers from 4 domains (Medicine, Physics, Biochemistry and Engineering, all distributed under CC-BY. 

* Humanities Articles

A collection of articles from the Humanities has been gathered from the following domains: 
  General Arts and Humanities
  Culteral Studies
  Language and Linguistics
  Sociology and Political Science

https://core.ac.uk/exports/SoFAIR_Humanities_Papers.zip

All papers have a cc-by license.

### References

[1] Waltman, Ludo, and Nees Jan Van Eck. "A new methodology for constructing a publication‐level classification system of science." Journal of the American Society for Information Science and Technology 63.12 (2012): 2378-2392.
