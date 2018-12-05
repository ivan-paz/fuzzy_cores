#         import the necessary functions
#
from what_happens_when_the_combination_arrives import what_happends_when_combination_arrives
from optimum_partition_different_class import adjust_cores
from ruler import ruleExtraction
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#function that converts an instance into set format
def instance_to_set_format(instance):
    set_format = []
    for i in range( len(instance)-1 ):
        set_format.append(set([instance[i]]))
    set_format.append( instance[-1] )
    return set_format
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#break the affected cores into pieces
import itertools
import copy
def expand_rule(rule):
    rule = copy.deepcopy(rule)
    expanded_rule = []
    for i in range(len(rule)):
        rule[i] = rule[i]
    for i in itertools.product(*rule):
        expanded_rule.append(i)
    return expanded_rule

#cores = [[{1, 4}, {8, 6}, 'A'], [{3}, {6}, 'A']]
def expand_cores(cores):
    expanded = []
    for c in cores:
        expanded_core = expand_rule(c)
        temporal = []
        for i in expanded_core:
            i = instance_to_set_format(i)
            temporal.append(i)
        [expanded.append(i) for i in temporal]
    return expanded
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
def commit_cores(new_instance,cores):

    if cores == []:
        cores.append(instance_to_set_format(new_instance))
        return cores

    case = what_happends_when_combination_arrives(new_instance,cores)
    
    if case == 'same class':
        print('same class')
        #break the rules
        #call ruler
        cores.append(instance_to_set_format(new_instance))
        cores = expand_cores(cores)
        print('cores for ruler:',cores) 
        cores = ruleExtraction(cores,1,0)
        #solve the contradictions

    elif case == 'different class':
        print('different class')
        cores = adjust_cores(cores,new_instance)

    else:
        print('nothing')
        cores.append(instance_to_set_format(new_instance))
    print('final cores  : ',cores)

#combination = (3, 7, 'B') 
#cores = []
#commit_cores(combination,cores)

#different class
#combination = (3, 7, 'B') 
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

#nothing
#combination = (5, 7, 'B') 
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

# same class
#combination = (3, 6, 'A') 
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

