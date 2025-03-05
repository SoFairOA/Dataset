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
        softwares = set()

        for rs in root.findall(".//tei:rs[@type='software']", NAMESPACE):
            software_name = rs.text.strip() if rs.text else "[No Name]"
            softwares.add(software_name)

        return softwares

    except (ET.ParseError, UnicodeDecodeError) as e:
        print(f"Error processing {xml_file}: {e}")
        return set()  # Return empty set if error occurs


def process_directory(directory):
    """Builds a deduplicated list of software names from all XML files."""
    if not os.path.isdir(directory):
        print("Invalid directory path")
        return set()

    unique_softwares = set()
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            file_path = os.path.join(directory, filename)
            unique_softwares.update(extract_software_from_rs(file_path))

    return sorted(unique_softwares)  # Return sorted list for consistency


def check_untagged(directory, software_list):
    """Checks if software names appear untagged in XML files."""
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_file = os.path.join(directory, filename)

            # Extract tagged software from XML
            tagged_software = extract_software_from_rs(xml_file)

            # Read the full XML content as text
            with open(xml_file, "r", encoding="utf-8") as file:
                text_content = file.read()

            for software in software_list:
                # Use regex to match software as a whole word
                pattern = rf"\b{re.escape(software)}\b"

                if re.search(pattern, text_content):  # If found in text
                    if software not in tagged_software and software not in ["code","codes", "scripts"]:  # But not tagged
                        print(f"⚠️ Missed: '{software}' in {filename}")


# Run the script
directory_path = "./SoFAIR_AD_Medicine_papers"
software_list = process_directory(directory_path)
check_untagged(directory_path, software_list)
