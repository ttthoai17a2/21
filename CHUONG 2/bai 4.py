from xml.dom.minidom import parse

doc = parse("sample.xml")
name_elements = doc.getElementsByTagName("name")

for element in name_elements:
    print(element.firstChild.data)
