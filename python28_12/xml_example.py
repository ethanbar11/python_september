import xml.etree.ElementTree as ET
import csv

xml_path = "garden.xml"
tree = ET.parse(xml_path)
root = tree.getroot()
for element in root:
    if element.tag == "animal":
        element_found = element.find("name")
        print(element_found.text)
