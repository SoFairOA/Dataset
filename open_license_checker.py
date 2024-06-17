import json
import os
import csv
import shutil

#create a list of every pre-annotated documents
list_pre_annotated_doc = []
base_path = 'documents/tei-pre-annotated'
for directory in os.listdir(base_path):
    dir_path = os.path.join(base_path, directory)
    if os.path.isdir(dir_path):
        list_pre_annotated_doc.extend(os.listdir(dir_path))
print('all pre-annotated xml files: ',len(list_pre_annotated_doc))

#create a dict with the {DOI : ID} in the full corpus
id_doi_dict = {}
path_list = [
    'documents/SoFAIR_Annotation_Dataset_Paper_Data_Extension.csv',
    'documents/SoFAIR_Annotation_Dataset_Paper_Data_first.csv'
]
nb = 0
duplicates = set()

for path in path_list:
    with open(path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nb += 1
            doi = row['DOI']
            id = row['ID']
            if doi in id_doi_dict:
                if not id_doi_dict[doi]==id:
                    print(f"Duplicate found: DOI={doi} (Previous ID={id_doi_dict[doi]}, New ID={id})")
                duplicates.add(doi)
            id_doi_dict[doi] = id

print(f'dict DOI=ID: {len(id_doi_dict)}/{nb} (duplicates:{len(duplicates)})')

#create a list of every DOI with a cc-by license
list_doi = []
with open('documents/SoFAIR-corpus-first-subset-cc-by.json', 'r') as file:
    license = []
    for line in file:
        data = json.loads(line)
        list_doi.append(data['doi'])
with open('documents/SoFAIR_Annotation_Dataset_Paper_Data_Extension.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        list_doi.append(row['DOI'])

print('doi cc-by: ', len(list_doi))

list_fileid_ccby = []
list_fileid_whitout_ccby = []
for doi,id in id_doi_dict.items():
    if doi in list_doi:
        list_fileid_ccby.append(id)
print('all fileid_ccby: ',len(list_fileid_ccby))

nb = 0
base_path = 'documents/tei-pre-annotated'
destination_directory = 'file_whitout_ccby'

for category_directy in list(os.listdir(base_path)):
    category_directy_path = os.path.join(base_path, category_directy)
    for file_to_check in os.listdir(category_directy_path):
        if file_to_check.replace(".training.tei.xml", '') not in list_fileid_ccby:
            list_fileid_whitout_ccby.append(file_to_check.replace(".training.tei.xml", ''))
        else:
            nb += 1
print('nb of files to move:', len(list_fileid_whitout_ccby))
print('nb of files with a ccby license:', nb)