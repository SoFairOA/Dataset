import os
import xml.etree.ElementTree as ET
import re  # Import regex library

# Define TEI namespace
NAMESPACE = {"tei": "http://www.tei-c.org/ns/1.0"}


def extract_software_from_rs(xml_file):
    """Extracts all tagged software names from an XML file."""
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        softwares = {}

        for rs in root.findall(".//tei:rs[@type='software']", NAMESPACE):
            if rs.attrib.get('subtype') not in ['environment', 'component','implicit']:
                if '{http://www.w3.org/XML/1998/namespace}id' not in rs.attrib:
                    print(f"not xml:id for {rs.attrib} in {xml_file}")
                software_name = rs.text.strip()
                if software_name in softwares:
                    softwares[software_name].append(xml_file)  # Append new source file
                else:
                    softwares[software_name] = [xml_file]  # Store first occurrence

        return softwares  # Dictionary {software_name: [list of source_files]}

    except (ET.ParseError, UnicodeDecodeError) as e:
        print(f"Error processing {xml_file}: {e}")
        return {}  # Return empty dict if error occurs


def process_directory(directory):
    """Builds a deduplicated list of software names from all XML files."""
    if not os.path.isdir(directory):
        print("Invalid directory path")
        return {}

    software_sources = {}  # Dictionary to track software origins
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            extracted = extract_software_from_rs(file_path)

            # Merge occurrences
            for software, files in extracted.items():
                if software in software_sources:
                    software_sources[software].extend(files)
                else:
                    software_sources[software] = files

    return software_sources  # {software_name: [list of source_files]}


def check_untagged(directory, software_sources):
    """Checks if software names appear untagged in XML files."""
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_file = os.path.join(directory, filename)

            # Extract tagged software from current XML
            tagged_software = extract_software_from_rs(xml_file).keys()

            # Read the full XML content as text
            with open(xml_file, "r", encoding="utf-8") as file:
                text_content = file.read()

            for software, source_files in software_sources.items():
                # Use regex to match software as a whole word
                pattern = rf"\b{re.escape(software)}\b"

                if re.search(pattern, text_content):  # If found in text
                    if software not in tagged_software and software not in ["code", "codes", "scripts"]:
                        origin_files = ", ".join(os.path.basename(f) for f in source_files)
                        #print(f"⚠️ Missed: '{software}' in {filename} (Originally tagged in: {origin_files})")
                        print(f"⚠️ Missed: '{software}' in {filename} (Originally tagged in: {source_files[:1]})")



# Run the script
directory_path = "./SoFAIR_AD_Physics_papers"
software_sources = process_directory(directory_path)
check_untagged(directory_path, software_sources)
