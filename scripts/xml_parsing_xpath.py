import xml.etree.ElementTree as ET

# while declaring the string make sure the first line should have the xml data as `<?xml version="1.0"?>`

xml_data="""<?xml version="1.0"?>
        <data>
            <country name="Liechtenstein">
                <rank>1</rank>
                <year>2008</year>
                <gdppc>141100</gdppc>
                <neighbor name="Austria" direction="E"/>
                <neighbor name="Switzerland" direction="W"/>
            </country>
            <country name="Singapore">
                <rank>4</rank>
                <year>2011</year>
                <gdppc>59900</gdppc>
                <neighbor name="Malaysia" direction="N"/>
            </country>
            <country name="Panama">
                <rank>68</rank>
                <year>2011</year>
                <gdppc>13600</gdppc>
                <neighbor name="Costa Rica" direction="W"/>
                <neighbor name="Colombia" direction="E"/>
            </country>
        </data>
"""

root=ET.fromstring(xml_data)
#fetching top level element which is the data in here thats the data
all_top_level=root.find(".")
#fetching the country details over here as below 
all_country=all_top_level.findall("country")[0]

# for country in all_country:
#     print(country.get("name")) #fetching the name attribute of the Element object


#if we want to fetch the  neighbour details directly from the root then we can use as 
# for neighbor in root.findall("./country/neighbor"):
#     print(neighbor.get("name"))


# selecting all the sub-element of a element as using the `//` symbol

# for item in  root.findall(".//country[@name='Liechtenstein']//"):
#     if item.get("name")is not None:
#         print(item.get("name"))
#     else:
#         print(item.text)
    

# by using the symbol as `.` we can get the  `currenrt node` , mostly used in the start
# this will provide the info about the current tag where  we are in 

# for item in  all_country.findall("."):
#     if item.get("name")is not None:
#         print(item.get("name"))
#     else:
#         print(item.text)

# if  we want to fetch the  parent of an child then we need to use the  `..` symbol
# while fetching the parent we have to use the `/` from chiuld to parent

# for item in  root.findall(".//rank[.='1']/../../"):
#     print(item.tag)


#from  parent to child also we can mention that with the `//` which will select all the children

# for child in root.findall(".//country[@name='Panama']//"):
#     if child.get("name")is not None:
#             print(child.get("name"))
#     else:
#         print(child.text)

#fetching the country as parent from the neighbour
# for country in root.findall(".//neighbor[@name='Colombia']/.."):
#     print(country.get("name"))
    
#fetcvhing the sibling xml tag fropm one tag as below 

# for country in root.findall(".//neighbor[@name='Colombia']/..//"):
#     if country.get("name")is not None:
#         print(country.get("name"))
#     else:
#         print(country.text)


# if we are putting the symbol as `[@<attribute>]` it will  Selects all elements that have the given attribute
# if we want to find the attribute value of the name which has only name attribute we do something as this 

# for  neighbour in root.findall(".//neighbor[@name]"):
#     print(neighbour.get("name"))


# if we are using `[tag]` then it weill select all the `child element` which has that `Tag`

# for item in root.findall(".//country[rank]"):
#     print(item.get("name"))


# `[.='text']` used to provide elements whose complete text content along with their descendants

#fetching the country  with year as the value of 2011

# for country in root.findall(".//year[.='2011']/.."):
#     print(country.get("name"))

# [.!='text'] used to provide elements whose complete text  does not content along with their descendants

#fetching the country  with year as the value not of 2011

# for country in root.findall(".//year[.!='2011']/.."):
#     print(country.get("name"))

# `[tag='text']`Selects all elements that have a child named tag whose complete text content, including descendants, equals the given text.
#this will provide the current Element object
# for item in root.findall(".//country[rank='1']"):
#     print(item.get("name"))


# `[tag !='text']` Selects all elements that have a child named tag whose complete text content, including descendants, does not equal the given text.
#this will provide the current Element object
# for item in root.findall(".//country[rank!='1']"):
#     print(item.get("name"))



#if we want to fetch a specific neighbour we can use this as below 
# for neighbor in root.findall(".//*[@name='Colombia']"):
#     print(neighbor.get("name"))


#or we can fetch by using it as below 
# for neighbor in all_top_level.findall(".//*[@name='Colombia']"):
#     print(neighbor.get("name"))


# fetching the `year`` which have the country as `Liechtenstein` 
#fetching the children from speciofic parent
# for year in root.findall(".//*[@name='Liechtenstein']/year"):
#     print(year.text)



    