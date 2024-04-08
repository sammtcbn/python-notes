import xml.etree.ElementTree as ET

def get_all_student_id(xml_file_path):
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        idlists = []
        for child in root.findall('.//Profiles/*'):
            if child.tag.endswith('_ID') and 'studentid' in child.attrib:
                idtmp = int(child.attrib['studentid'])
                idlists.append(idtmp)
        return idlists

    except (IOError, ET.ParseError) as e:
        print("Error:", e)
        return []

def main():
    idlist = get_all_student_id("show_match_attrib.xml")
    print(idlist)

if __name__ == '__main__':
    main()

"""
Result:
$ python3 show_match_attrib.py
[1, 2, 99, 45]
"""
