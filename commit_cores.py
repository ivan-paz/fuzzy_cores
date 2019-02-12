#-------------------------------------------------------------------------------------
#
#               import the necessary functions
#
#
#-------------------------------------------------------------------------------------
from what_happens_when_the_combination_arrives import what_happends_when_combination_arrives
from optimum_partition_different_class import adjust_cores
from ruler import ruleExtraction
from break_and_keep_max_volume import solve_contradictions_seek_maximum_volume
from compare_two_rule_sets import set_difference





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
def tuple_format(rule):
    in_tuple = []
    for i in range(len(rule)-1):
        in_tuple.append(tuple(rule[i]))
    in_tuple.append(rule[-1])
    print(in_tuple)
    return in_tuple
#tuple_format([{1, 4}, {8, 6}, 'A'])

#tuple to set format
def tuple_to_set_format(rule):
    in_set = []
    for i in range(len(rule)-1):
        if type(rule[i])==tuple:
            temporal = []
            [temporal.append(j) for j in rule[i]]
            in_set.append(temporal)
        else:
            in_set.append(rule[i])
    in_set.append(rule[-1])
    print(in_set)
    return in_set
#print( tuple_to_set_format( [(1, 4), (6,), 'A']))

#--------------------------------------------------------------------------
# receives a new instance and commit a set of cores

def commit_cores(new_instance,cores):
    if cores == []:
        cores.append(instance_to_set_format(new_instance))
        return cores
    
    case = what_happends_when_combination_arrives(new_instance,cores)
    
    if case == 'same class':
        print('SAME class')
        
        cores.append(instance_to_set_format(new_instance))
        #break the rules
        cores = expand_cores(cores)
        print('cores for ruler:',cores)
        #call ruler
        cores = ruleExtraction(cores,1,0)
        #solve the contradictions
        # convert the rules into tuple format
        temporal = []
        [temporal.append(tuple_format(rule)) for rule in cores]
        #print('temporal :  ',  temporal  )
        cores = solve_contradictions_seek_maximum_volume(temporal)
        print('cores after solve_contradictions', cores)
        
        rules_to_include = set_difference(temporal,cores[0])
        print('rules_to_include',rules_to_include)
        
        print('type of cores ::::::: ',type(cores))

        if type(cores) == list:
            [rules_to_include.append(r) for r in cores if r not in rules_to_include]
            
        else:
            print('cores[0]', cores)
            if len(cores[0])!=1:
                for c in cores:
                    for r in c:
                        if r not in rules_to_include:
                            rules_to_include.append(r)
            else:
                [rules_to_include.append(r) for r in cores[0] if r not in rules_to_include]

        print('RULES to include  : ', rules_to_include)
        return rules_to_include

    elif case == 'different class':
        print('different class')
        cores = adjust_cores(cores,new_instance)
    else:
        print('nothing')
        cores.append(instance_to_set_format(new_instance))

    print('final cores  : ',cores)
    return cores




