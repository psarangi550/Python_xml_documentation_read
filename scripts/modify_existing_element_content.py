import xml.etree.ElementTree as ET

with open("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\sample.xml","r") as xml_file:
    data=xml_file.read()

tree=ET.parse("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\sample.xml")
# root=ET.fromstring(data)

root=tree.getroot()

print(type(root))

#now here we need to amend the `rank` to `rank+1`

# for rank in root.iter("rank"):
#     # print(rank.text)
#     new_rank=rank.text
#     modified_rank=int(new_rank)+1
#     print(modified_rank)
#     rank.text=str(modified_rank)
#     rank.set("updated","yes") #this will be updated as an attribute to the updated tag
# tree.write("C:\\Users\\psara\\Downloads\\python_xml_tutorial_series\\data\\output.xml")

