import xml.etree.ElementTree as ET

def main():
    tree = ET.parse('setting.xml')
    root = tree.getroot()

    print (root)
    # <Element 'Settings' at 0x7fd5429f2070>

    print (root.tag)
    # Settings

    print (root.attrib)
    # {}

if __name__ == '__main__':
    main()
