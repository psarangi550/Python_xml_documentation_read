### <ins> Parsing XML using Element Tree Module </ins>

#### <ins> Difference Between the ElementTree class and  Element class in XML </ins>

- when we cretae the `tree` object using the `<Element Tree object>=ElementTree.parse("xml file location")` will provide the `Element Tree object`
- by using the `EletementTree object` we can create the `Element object` class object as `root=<Element Tree object>.getroot()`
- here in the above case the `root` is the `Element  object`
- we can also create the `Element object` by using the  `ElementTree class as well` by using `ET.fromString("string of the xml file")`
 

#### Navigating through the XML files

- Element.findall() finds only elements with a tag which are direct children of the current element. 
- Element.find() finds the first child with a particular tag, 
- Element.text accesses the element’s text content. 
- Element.get() accesses the element’s attributes:
- Element.attrib will provide the result in the form of `dictionary` with `key` as `attribute name` and `attribute value` as `value`
- Element.tag will provide the tag 

#### <ins> How to modify and the Existing XML Content and Write to a New XML Document

- we can access the `child Element` recursively by using `iter()` on `<Element obj>.iter("tag")` 
- once the `attribute been modified` if we =want to add any additional attribute then we need to use the `<Element obj>.set()`
- here the `Element obj.set()` takes 2 paramter  `what should be attribute and what should be the value of the attribute after updated`
- we can create a new new xml document by using it as `<Element Tree object>.write("<location of the file where we want to write >")`
- we can also remove the `Element` from the xml by using it as `<parent element object>.remove("<child element object which we want to remove>")` 

#### <ins> How to create the Element and SubElement in  XML document 

- by using the `Element()` method on the `ElementTree class` we can create the `Element object` as well 
- by using the `<sub ele obj>=<elementobj>.SubElement(<parent Element>,"<corresponding child element>")` method on the `Element object` we created we can create the `Subelement` inside the `Element` in the excel
- instead of creating a `new document` if we want to show the changes then we can use the `dump()` on `Element Tree class `
- we can write as `ElementTreeclass.dump(<Element/Element Tree object>)`

    ```
        a = ET.Element('a')
        b = ET.SubElement(a, 'b')
        c = ET.SubElement(a, 'c')
        d = ET.SubElement(c, 'd')
        ET.dump(a)
        #here is the output 
        #--------------------
        <a>
            <b />
            <c>
                <d />
            </c>
        </a>

    ```
