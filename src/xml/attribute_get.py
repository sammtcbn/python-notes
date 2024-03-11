import xml.etree.ElementTree as ET

xml_content = '''
<doc>
    <MyData val="1234" />
</doc>
'''

root = ET.fromstring(xml_content)

# method 1
valattrib = root.find('.//MyData').attrib['val']
print(valattrib)

# method 2
mydata_element = root.find('.//MyData')
if mydata_element is not None:
    val = mydata_element.get('val')
    print(val)
else:
    print("not found")
