import xml.etree.ElementTree as ET

xml_data = ET.parse('newxml.xml')
# print(xml_data)

xml_root = xml_data.getroot()
# print(xml_root)

# parse, tag, attrib, index

# print(xml_root.tag)
# print(xml_root.attrib)
# print(xml_root[0])
# print(xml_root[0].attrib)
# print(xml_root[1])
# print(xml_root[1].attrib)

# iter, find/ findall

# for child in xml_root:
#     for element in child:
#         print(element)
#     print(child)


# fromstring,m dump

# xml_str = ET.fromstring('<a>123</a>')
# print('1 - ', xml_str)
#
# print(ET.dump(xml_data))

# find, findall
print(xml_root.find('CD').attrib)
print(len(xml_root.findall('CD')))
index = 0
for i in xml_data.iter('COUNTRY'):
    index += 1
    print(i.text)
    print(i.attrib)
    i.set('index', f'{index}')
    print(i.attrib)

xml_data.write('newxml2.xml')

# xpath

for i in xml_data.findall('//*[@id]'):
    print('1 --- ', i.tag)