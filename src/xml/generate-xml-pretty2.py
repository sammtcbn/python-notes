import xml.etree.ElementTree as ET
from xml.dom import minidom

def main():
    root = ET.Element("School")

    classa = ET.SubElement(root, "ClassA")
    classb = ET.SubElement(root, "ClassB")

    ET.SubElement(classa, "student", name="sam").text = "Sam Lin"
    ET.SubElement(classa, "student", name="terry").text = "Terry Huang"

    ET.SubElement(classb, "student", name="bob").text = "Bob Lu"
    ET.SubElement(classb, "student", name="helen").text = "Helen Chen"

    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    with open("generate-xml-pretty2.xml", "w") as f:
        f.write(xmlstr)

if __name__ == '__main__':
    main()
