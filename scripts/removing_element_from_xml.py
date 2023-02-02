import xml.etree.ElementTree as ET

tree=ET.parse("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\output.xml")

root=tree.getroot()

for country in root.findall("country"):
    for rank in country.findall("rank"):
        text_rank=rank.text
        if int(text_rank)>50:
            # print("done")
            country.remove(rank)

tree.write("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\new_output.xml")