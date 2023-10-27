import xml.etree.ElementTree as ET

def main():
    tree = ET.parse("setting.xml")
    root = tree.getroot()
    for child_of_root in root:
        print ("tag    -", child_of_root.tag)
        print ("text   -", child_of_root.text)
        print ("attrib -", child_of_root.attrib)
        print ("--------------------")

if __name__ == '__main__':
    main()
