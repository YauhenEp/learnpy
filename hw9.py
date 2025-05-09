import xml.etree.ElementTree as ET

class XmlWriter(object):
    def __init__(self, filenamePath):
        self.filenamePath = filenamePath

    def generate_xml(self):
        data = ET.parse(self.filenamePath)
        xml_text = ''
        for tag in data.iter():
            print(tag)
            xml_text += ET.tostring(tag, encoding='unicode')
            print(xml_text)
        return xml_text
