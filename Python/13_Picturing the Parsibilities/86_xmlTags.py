'''
You want to create your local database containing information about the things you find the coolest. You used to store this information in xml documents, so now you need to come up with an algorithm that will convert the existing format into the new one. First you decided to choose a structure for your scheme, and to do it you want to represent xml document as a tree, i.e. gather all the tags and print them out as follows:

tag1()
 --tag1.1(attribute1, attribute2, ...)
 ----tag1.1.1(attribute1, attribute2, ...)
 ----tag1.1.2(attribute1, attribute2, ...)
 --tag1.2(attribute1, attribute2, ...)
 ----tag1.2.1(attribute1, attribute2, ...)
...
where attributes of each tag are sorted lexicographically.

You are a careful person, so the structure of the xml is neatly organized is such a way that:

there is a single tag at the root level;
each tag has a single parent tag (i.e. if there are several occurrences of tag a, and in one occurrence it's a child of tag b and in the other one it's a child of tag c, then b = c);
each appearance of the same tag belongs to the same level.
Given an xml file, return its structure as shown above. The tags of the same level should be sorted in the order they appear in xml, and the attributes should be sorted lexicographically.
Note: you are given xml representation in one line.

Example
For
xml =
"<data>
    <animal name="cat">
    	<genus>Felis</genus>
        <family name="Felidae" subfamily="Felinae"/>
        <similar name="tiger" size="bigger"/>
    </animal>
    <animal name="dog">
        <family name="Canidae" member="canid"/>
        <order>Carnivora</order>
        <similar name="fox" size="similar"/>
    </animal>
</data>"
the output should be

xmlTags(xml) =
["data()",
 "--animal(name)",
 "----genus()",
 "----family(member, name, subfamily)",
 "----similar(name, size)",
 "----order()"]

'''
import xml.etree.ElementTree as ET
def xmlTags(xml):
    root = ET.fromstring(xml)
    dictionary = dict()
    for node in root.iter():
        dictionary.setdefault(node.tag, set()).update(node.keys())
    test = process(root)
    
    final = []
    for tag in test:
        final.append('--'*test[tag] + tag + '(' + ', '.join(sorted(dictionary[tag])) + ')')
    return final
    
def process(node, tags=None, depth=None):
    tags = tags if tags is not None else OrderedDict()
    depth = depth if depth is not None else 0
    tags.setdefault(node.tag, depth)
    for child in node:
        tags.update(process(child, tags, depth+1))
    return tags



##--------------------- 
'''
def xmlTags(xml):
    import xml.etree.ElementTree as ET
    tree = ET.fromstring(xml)
    
    class Node(dict):
        COUNTER = 0
        
        def __init__(self, tag):
            self.tag = tag
            self.children = {}
            self.args = set()
            self.counter = Node.COUNTER
            Node.COUNTER += 1
            
        def __getitem__(self, k):
            return self.children.setdefault(k, Node(k))
        
        def __lt__(self, other):
            return self.counter < other.counter
        
        def format(self):
            yield self.tag + '(' + ', '.join(sorted(self.args)) + ')'
            for c in sorted(self.children.values()):
                for line in c.format():
                    yield '--' + line
            
    def helper(node, result=None):
        if result == None:
            result = Node(node.tag)
        result.args.update(node.keys())
        for child in node.getchildren():
            helper(child, result[child.tag])
        return result
    
    return list(helper(tree).format())
'''

#Almost there---->
'''# import xml.etree.ElementTree as ET
# from collections import OrderedDict
# def xmlTags(xml):
#     tree = ET.ElementTree(ET.fromstring(xml))
#     root = tree.getroot()
#     print(root.getchildren())
#     tags = OrderedDict({})
#     result = list()
    
#     for ele in root.iter():
#         if ele.tag not in tags:
#             tags[ele.tag] = set()
        
#         for att in ele.attrib.keys():
#             tags[ele.tag].add(att)
    
#     for tag in tags:
#         if tags[tag] == set():
#             result.append(str(tag +'()'))
#         else:
#             attr = ', '.join([att for att in tags[tag]])
#             result.append(str(tag)+ '('+ attr +')')
#     return result
'''
