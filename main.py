from lxml import etree, objectify
from io import StringIO

#tree = etree.parse("process/diagram.bpmn")
#tree = etree.parse("process/example.bpmn")
#tree = etree.parse("process/19650.bpmn")
tree = etree.parse("process/19650_v2.bpmn")
#tree = etree.parse("process/hellowall.bpmn")

print('')
 
for elem in tree.getiterator():
    if not hasattr(elem.tag, 'find'): continue  # (1)
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i+1:]
objectify.deannotate(tree, cleanup_namespaces=True)

# this loop tries to work out the context of the BPMN
# do we have no collaboration or swimlanes - (hellowall.bpmn)
# do we have many participants in a single collaboration

collab = False

for process in tree.getroot():

    # this is used to get the process names for below...
    
    # get the collaborations
    if (process.tag =='collaboration'):
        collab = True
        # ok so we could have multiple collaborations
        # multiple lane sets
       
        
        for lane in process:
            print('\t{} : {} | '.format(lane.get('name'),lane.get('id')))

print('\tModel has collaboration : {}\n'.format(collab))

for element in tree.getroot():
    # get the processes
    if (element.tag=='process'):
        
        # need to get the name by matching the participant id above......
        
        print('############## NEW PROCESS : {} ###################### \n'.format(element.get('name')))

        for obj in element:
            dash = '\t --'+('-'*len(obj.tag))
            print(dash)
            print('\t| {} |'.format(obj.tag))
            print(dash)
            
            if (obj.tag =='startEvent'):
                # the id of the outgoing connection / sequenceFlow(i think)
                for flow in obj:
                    if (flow.tag=='outgoing'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )
                
            elif (obj.tag =='task' or obj.tag =='exclusiveGateway'):
                # the id of the task
                print('\t\tid: {}'.format(obj.get('id')))
                # the name of the task
                print('\t\tname: {}'.format(obj.get('name')))
                for flow in obj:
                    if (flow.tag=='incoming'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )
                    elif (flow.tag=='outgoing'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )
                        
            elif (obj.tag =='scriptTask'):
                # the id of the task
                print('\t\tid: {}'.format(obj.get('id')))
                # if of the sourceRef
                print('\t\tname: {}'.format(obj.get('name')))
                # if of the targetRef
                print('\t\tscriptFormat: {}'.format(obj.get('scriptFormat')))
                for flow in obj:
                    if (flow.tag=='incoming'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )
                    elif (flow.tag=='outgoing'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )   
                    # ####### CARFUL WITH HOW YOU HANDLE THIS ELEMENT #############    
                    elif (flow.tag=='script'):
                        print('\t\t{} : {}'.format(flow.tag,flow.text) )
            
            elif (obj.tag =='sequenceFlow'):
                # the id of the task
                print('\t\tid: {}'.format(obj.get('id')))
                # if of the sourceRef
                print('\t\tsourceRef: {}'.format(obj.get('sourceRef')))
                # if of the targetRef
                print('\t\ttargetRef: {}'.format(obj.get('targetRef')))
                
            elif (obj.tag =='association'):
                # the id of the task
                print('\t\tid: {}'.format(obj.get('id')))
                
                print('\t\tassociationDirection: {}'.format(obj.get('associationDirection')))
                # if of the sourceRef
                print('\t\tsourceRef: {}'.format(obj.get('sourceRef')))
                # if of the targetRef
                print('\t\ttargetRef: {}'.format(obj.get('targetRef')))
            
            
            # elif (obj.tag =='task'):
                # # the id of the task
                # print(obj.get('id'))
                # # the name of the task
                # print(obj.get('name'))
                
        print('\n############## END PROCESS : {} ###################### \n'.format(element.get('name')))        


       


