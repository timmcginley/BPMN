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

    # this is used to get the process names for below...
    
    # get the collaborations
    if (obj.tag =='collaboration'):
        for parti in obj:
            print('\t{} : {} | '.format(parti.get('name'),parti.get('id')))

# TODO : switch pro anc object naming -> its the wrong way round!!!

for obj in tree.getroot():
    # get the processes
    if (obj.tag=='process'):
        
        # need to get the name by matching the participant id above......
        
        print('############## NEW PROCESS : {} ###################### '.format(obj.get('name')))
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
                print('id: {}'.format(pro.get('id')))
                # the name of the task
                print('name: {}'.format(pro.get('name')))
                for flow in pro:
                    if (flow.tag=='incoming'):
                        print('{} : {}'.format(flow.tag,flow.text) )
                    elif (flow.tag=='outgoing'):
                        print('{} : {}'.format(flow.tag,flow.text) )
                
            elif (pro.tag =='task'):
                # the id of the task
                print(pro.get('id'))
                # the name of the task
                print(pro.get('name'))
                
        print('############## END PROCESS : {} ###################### \n'.format(obj.get('name')))        


       


