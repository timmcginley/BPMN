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


for obj_pro in tree.getroot():

    # this is used to get the process names for below...
    
    # get the collaborations
    if (obj_pro.tag =='collaboration'):
        for parti in obj_pro:
            print('\t{} : {} | '.format(parti.get('name'),parti.get('id')))

# TODO : switch pro anc object naming -> its the wrong way round!!!

for obj_pro in tree.getroot():
    # get the processes
    if (obj_pro.tag=='process'):
        
        # need to get the name by matching the participant id above......
        
        print('############## NEW PROCESS : {} ###################### '.format(obj_pro.get('name')))
        print (obj_pro.tag)
        for obj in obj_pro:
            dash = '\t --------'+('-'*len(obj.tag))
            print(dash)
            print('\t| [PRO] {} |'.format(obj.tag))
            print(dash)
            
            if (obj.tag =='startEvent'):
                # the id of the outgoing connection / sequenceFlow(i think)
                print(obj.get('outgoing'))
                
            elif (obj.tag =='task'):
                # the id of the task
                print('id: {}'.format(obj.get('id')))
                # the name of the task
                print('name: {}'.format(obj.get('name')))
                for flow in obj:
                    if (flow.tag=='incoming'):
                        print('{} : {}'.format(flow.tag,flow.text) )
                    elif (flow.tag=='outgoing'):
                        print('{} : {}'.format(flow.tag,flow.text) )
                
            elif (obj.tag =='task'):
                # the id of the task
                print(obj.get('id'))
                # the name of the task
                print(obj.get('name'))
                
        print('############## END PROCESS : {} ###################### \n'.format(obj_pro.get('name')))        


       


