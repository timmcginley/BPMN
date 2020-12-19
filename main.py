from lxml import etree, objectify
from io import StringIO

tree = etree.parse("process/diagram.bpmn")
#tree = etree.parse("process/hellowall.bpmn")

 
for elem in tree.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i+1:]
objectify.deannotate(tree, cleanup_namespaces=True)


for obj in tree.getroot():
    # get the collaborations
    if (obj.tag =='collaboration'):
        for parti in obj:
            print('\t{} : {} | '.format(parti.get('name'),parti.get('id')))

for obj in tree.getroot():
    # get the processes
    if (obj.tag=='process'):
        print (obj.tag)
        for pro in obj:
            dash = '\t --------'+('-'*len(pro.tag))
            print(dash)
            print('\t| [PRO] {} |'.format(pro.tag))
            print(dash)
            
            if (pro.tag =='startEvent'):
                # the id of the outgoing connection / sequenceFlow(i think)
                print(pro.get('outgoing'))
            elif (pro.tag =='task'):
                # the id of the task
                print(pro.get('id'))
                # the name of the task
                print(pro.get('name'))
                


       


