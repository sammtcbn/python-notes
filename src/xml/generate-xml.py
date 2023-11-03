import xml.etree.ElementTree as ET

def main():
    root = ET.Element("School")

    classa = ET.SubElement(root, "ClassA")
    classb = ET.SubElement(root, "ClassB")

    ET.SubElement(classa, "student", name="sam").text = "Sam Lin"
    ET.SubElement(classa, "student", name="terry").text = "Terry Huang"

    ET.SubElement(classb, "student", name="bob").text = "Bob Lu"
    ET.SubElement(classb, "student", name="helen").text = "Helen Chen"

    tree = ET.ElementTree(root)
    tree.write("generate-xml.xml")

if __name__ == '__main__':
    main()
