import xml.etree.ElementTree as ET

# tree=ET.parse("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\sample.xml")

# root=tree.getroot()

# print(root.tag)

# fetching all the xml content from the string after reading as below 

with open("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\sample.xml","r") as xml_file:
    data=xml_file.read()

root=ET.fromstring(data)

# print(root.attrib)

#to visualize all the attribute we can use the dump() on the  ET i.e the ElementTree class 

# ET.dump(root)

# uiterating therouigh the direct child over here 

for country in root.findall("country"):
    print(country.get("name"))
    print(country.find("year").text)
    for  rank in country.findall("rank"):
        print("#"*10)
        all_neighbor=country.findall("neighbor")
        for item in all_neighbor:
            print(item.attrib)
