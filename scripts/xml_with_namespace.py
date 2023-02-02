import xml.etree.ElementTree as ET

xml_text="""<?xml version="1.0"?>
        <actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
            <actor>
                <name>John Cleese</name>
                <fictional:character>Lancelot</fictional:character>
                <fictional:character>Archie Leach</fictional:character>
            </actor>
            <actor>
                <name>Eric Idle</name>
                <fictional:character>Sir Robin</fictional:character>
                <fictional:character>Gunther</fictional:character>
                <fictional:character>Commander Clement</fictional:character>
            </actor>
        </actors>
    """


root=ET.fromstring(xml_text)
#here the `xmlns:fictional` will be treated as `{http://people.example.com}fictional`
#hence if we want  fetch the fictional character then we can write it as below 


#here in this case the `xmlns` is the default `prefix` as its for the fiction
# the `default prefix` will be appended to all the `non-prefixed tag` such as `actor and name`
#but if a tag is there with thr `prefix` such as `fictional.character` then in that case we have to use the `ficitional` as the `prefix` and expand that to the uri

# for actor in root.findall("{http://people.example.com}actor"):
#     for name in actor.findall("{http://people.example.com}name"):
#         for char in actor.findall("{http://characters.example.com}character"):
#             print(' |-->', char.text)

#alternate approch to parse the XML as below 

roles={
    "default_prefix":"http://people.example.com",
    "ficitional_char":"http://characters.example.com"
}

for actor in root.findall("default_prefix:actor",roles):
    for name in actor.findall("default_prefix:name",roles):
        for char in actor.findall("ficitional_char:character",roles):
            print(char.text)




