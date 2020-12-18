from lxml import etree, objectify
from io import StringIO

tree = etree.parse("process/diagram.bpmn")

 
for elem in tree.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i+1:]
objectify.deannotate(tree, cleanup_namespaces=True)



for obj in tree.getroot():
    if (obj.tag=='process'):
        print (obj.tag)
        for pro in obj:
            print('--- processsssessss {}'.format(pro.tag))
            if (pro.tag =='startEvent'):
                print('\t\tweve started!!!!!')
    elif (obj.tag =='collaboration'):
        print('yay collaborate!!!!')
        for parti in obj:
            print('\tparticipant {}'.format(parti.tag))

       


