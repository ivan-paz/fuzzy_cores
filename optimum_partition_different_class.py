#
#
#    Algorithm that finds the optimum partition of a set
#    of CORES intersected by an instance of DIFFERENT
#    CLASS
#
#

#
#    Given a new pattern and a set of connected rules
#    find the rules intersected by the pattern
#
def same_class(r1,r2):
    if r1[-1] == r2[-1]:
        return True
    else:
        return False
#print(same_class([{1},{4},'A'],[{1},{2},'A']))
#print(same_class([{1},{4},'B'],[{1},{2},'A']))

# Create interval
def create_interval(some_input):
    if type(some_input) == int or type(some_input) == float:
        some_input = set([some_input])
    minimum = min(some_input)
    maximum = max(some_input)
    return (minimum,maximum)
#print(create_interval(1) )
#print(create_interval({4,6}))

#  True if two intervals, defined by its minimum and maximum values,
#intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
#print(interval_intersection( (1,11), (9,12) ) )
#print( interval_intersection( (2,5), (1,11) ) )

# intersection of numeric intervals
def intersection(r1,r2):
    if same_class(r1,r2):
        return False
    for i in range(len(r1)-1):
        interval1 = create_interval(r1[i])
        interval2 = create_interval(r2[i])
#        print(interval1,interval2,interval_intersection(interval1,interval2))
        if not interval_intersection(interval1,interval2):
            return False
    return True
#print( intersection( [{6,10},{4,6},'A'], (7,5,'B') ) )

def find_intersected_rules(pattern,rules):
    intersected = []
    for r in rules:
        if intersection(r,pattern):
            intersected.append(r)
    return intersected

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (7,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (8,5,'B')
#print(find_intersected_rules(pattern, rules))


#rules = [ [{1, 2}, {150}, {0.721901},'1'],[{2},{100,200},{0.721901},'1'] ]
#pattern = (   2, 120,  0.721901, '2')
#print(find_intersected_rules(pattern,rules))



# -*- coding: utf-8 -*-
"""
Function that recibes a couple of lists
labeled with different class. For example :

lists          class
(1,2,3,8,11) -> 0
(5)          -> 1

and returns tuples separated by the classes

in the example :

(1,2,3) -> 0
(5)     -> 1
(8,11)  -> 0

"""
#  create list with format [element, class]
def create_labels(_list,_class):
    labels = list()
    if type(_list) == int or type(_list) == float:
        labels = labels + [[_list,_class]]
    else:
        for element in _list:
            pair = [element,_class]
            labels = labels  + [pair]
    return labels
#  create_labels((1,2,3,8,11),0)
#---------------------------------------------------------------------
#-------------------------------------------------------------------------------
import operator
def create_sets(_list1,_list2):
    list1 = create_labels(_list1, 0)
    list2 = create_labels(_list2, 1)
    one_list = list1 + list2
    sorted_list = sorted(one_list, key = operator.itemgetter(0))
    return sorted_list
#      create_sets((1,2,3,8,11),(5,6,9))
 
def subsets(a):
    zero = []
    #one =  []
    temp = []
    
    if a[0][1] == 0:
        classe = 0
    else:
         classe = 1
    for ele in a:
        #print(ele)
        
        if ele[1] == classe:
            temp = temp + [ ele[0] ]
            #print('ele',ele,'temporal',temp)
        else:
            #print('different class')
            #if classe == 0:
            #   zero = zero + [temp]
            #else:
            #     one = one + [temp]
            zero = zero + [temp,classe]
            classe = ele[1]
            temp = []
            temp = temp + [ele[0]]
    zero = zero + [temp,classe]
    return zero

#EXAMPLES
#a = [(1, 0), (2, 0), (3, 0), (5, 1), (8, 0),(9,0)]
#subsets(a)
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0), (9, 1), (11, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (8, 0), (9, 1), (11, 0)])  

def create_subsets(set1_class1,set2_class2):
    ordered_list = create_sets(set1_class1,set2_class2)
    list_of_subsets = subsets(ordered_list)
    return list_of_subsets
#      create_subsets( (1,2,3,8,11), (5))



"""
Function that take two rules (R1, R2)
if class R1 != class R2
for each parameter, if partition is possible
create the resulting partition
it returns an array with the partition of each parameter.
"""

# import the necessary functions
#from function_to_create_subsets import *
import copy
"""

"""
def condition(t1, t2):
    #Ckeck if t1 and t2 intersect
    set1 = set()
    set2 = set();
    if type(t1) == int or type(t1)== float:
        set1.add(t1)
    else:
        for x in t1: set1.add(x)
    if type(t2) == int or type(t2)== float:
        set2.add(t2)
    else:
        for y in t2: set2.add(y)
    if len(set1.intersection(set2)) != 0:
        return True
    else:
        return False
#condition( (4,6), 4 )
#condition((1,2,3,8,11),(9,12))

def rules_form_subsets(subsets, i, R1, R2):
    rules = [ ]
    R1 = list(R1)
    R2 = list(R2)
    for j in range(len(subsets)):
        if j%2 != 0:
            #print(subsets[j],subsets[j-1])
            if subsets[j] == 0:
                rule = copy.deepcopy(R1)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
            else:
                rule = copy.deepcopy(R2)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
    return rules
#rules_form_subsets([[1, 2, 3], 0, [5], 1, [8, 11], 0], 0, R1, R2)

def create_rule_partitions(R1, R2):
    partitions = [ ]
    if R1[-1] != R2[-1]:
        for i in range(len(R1) - 1 ):
            #print(R1[i],R2[i])
            if condition(R1[i],R2[i]) == False:
                subsets = create_subsets(R1[i],R2[i])
                rules = rules_form_subsets(subsets, i, R1, R2)
                partitions = partitions + [rules]
        return partitions
    else:
        return False

#R1 = ( (1,2,3,8,11), (4,6), 'A' )
#R2 = ( 5, 4, 'B')
#print(partitions( R1, R2 ))


#R1 = [ {1,2,3,8,11}, {4,6}, 'A' ]
#R2 = ( 5, 4, 'B')
#print(create_rule_partitions( R1, R2 ))
#
#R1 = [ {1,2,3,8,11}, {4,6}, 'A' ]
#R2 = ( 5, 5, 'B')
#print(create_rule_partitions( R1, R2 ))
#
#R1 = [ {6,10}, {4,6}, 'A' ]
#R2 = ( 7, 5, 'B')
#print(create_rule_partitions( R1, R2 ))

#R1 = ((9,12), 5, 'C')
#R2 = ( (1,2,3,8,11), (4,6), 'A' )
#partitions( R1, R2 )
#
import itertools

partitions =  [
[
[[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A']], 
[[{10, 6}, (4,), 'A'], [8, (5,), 'B'], [{10, 6}, (6,), 'A']]
], 
[[[{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A']]]
]

def create_combinations_from_rule_partitions(partitions):
    combinations = list(itertools.product(*partitions))
    #[print(c) for c in combinations]
    return combinations
#print(create_combinations_from_rule_partitions(partitions)) 
#
#
#
#
#         Functions to calculate the volume of a set of rules 
#
#
#
#
from operator import itemgetter

#    FUNCTION TO CALCULATE THE VOLUME OF A PARAMETER
def parameter_volume(parameter):
    if type(parameter) == int or type(parameter) == float:
        minimum = maximum = parameter
    else:
        minimum = min(parameter)
        maximum = max(parameter)
    volume = abs(maximum - minimum)
    return volume
#print(parameter_volume((5,)))
#print(parameter_volume((11,13,16)))
#print(parameter_volume({11,13,16}))

#Function to calculate the volume of a rule
def rule_volume(rule):
    volume = []
    dimension = 0
    for parameter in range(0,len(rule) -1 ):
        parameter_contribution = parameter_volume(rule[parameter])
        if parameter_contribution != 0:
            dimension = dimension + 1
            volume = volume + [parameter_contribution]
            #print('volume:',volume)
    volume = sum(volume)
    return [volume,dimension]
#print(rule_volume([{12}, {10, 13}, 'B']))
#print(rule_volume([{12,13}, {10, 13}, 'B']))
#print(rule_volume([{8}, (3,), 'A']))
#print(rule_volume([8, (5,), 'B']))
#print(rule_volume([{8}, (7,), 'A']))



#-------------------------------------------------------------------
# Function that receives an array with the [volume,dimension] for a set of rules
# and return the global [volume, dimension] for each dimension
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
#    [   VOLUME,  DIMENSION  ]
def sum_equal_dimensions(volumes):
    dimensions = {}
    result = []
 #   print(volumes)
    for volume in volumes:
        key = str(volume[1])
 #       print(type(key))
 #       print(key)
        if key not in dimensions:
            dimensions[key] = [0,int(key)]
#    print('the dimensions are:',dimensions)
    while len(volumes) > 0:
        temporal = volumes[0]
        volumes.remove(temporal)
        temporalkey = str(temporal[1])
        suma = dimensions[temporalkey]
        suma[0] = suma[0] + temporal[0]
        dimensions[temporalkey] = suma
    #print(dimensions)
    for key in dimensions:
        result.append(dimensions[key])
    return result    
#print(sum_equal_dimensions( [ [4.0, 2], [3.0, 1], [1.0, 1]  ] ) )
#print(sum_equal_dimensions([[3.0, 1], [4.0, 2], [1.0, 1]]) )
#print(sum_equal_dimensions([[0,0],[0,0],[0,0]]))
#print(sum_equal_dimensions([[2, 1], [0, 0], [2, 1], [0, 0], [0, 0], [0, 0]]))
#-------------------------------------------------------------------
#Function that takes an array of arrays and sort them by its second entrance
#from operator import itemgetter

def sort_volumes(volumes):
    volumes = sorted(volumes,key=itemgetter(1))
    return volumes
#sort_volumes([[4.0, 1], [4.0, 2]])
#sort_volumes([[4.0, 2], [4.0, 1]])
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]))
#print(sort_volumes([[1.0, 2], [3.0, 2], [4.0, 4]]) )
#print(sort_volumes([[0, 0]]))
#-------------------------------------------------------------------
#Function to calculate the volume of a set of rules
# For each rule in the set
    #calculate its volume
#retur the sum of the volumes
def volume_of_the_ruleset(rules):
    volumes = []
    for rule in rules:
#        print(rule)
        volume = rule_volume(rule)
#        print('aportacion de la regla', volume)
        volumes = volumes + [volume]
#    print('volumes',volumes)
    volumes = sum_equal_dimensions(volumes)
    volumes = sort_volumes(volumes)
    return volumes
#print(partition_volume([[(12,), {10, 13}, 'B'], [{11, 13}, {11, 13}, 'D'], [{12,13},(10,),'B'] ]))
#print(volume_of_the_ruleset( [[(6,), {4, 6}, 'A'], [(8,), 5, 'B'], [(10,), {4, 6}, 'A'], [{8}, (3,), 'A'], [8, (5,), 'B'], [{8}, (7,), 'A'] ] ) )
#
#from calculate_volume_of_a_ruleset import volume_of_the_ruleset, sum_equal_dimensions
def partition_volumes(combinations):
    combinations_volumes = []
    for combination in combinations:
        combination_volume = []
        #print('combination\n', combination)
        # Each partition is the partition of a rule
        for partition in combination:
            volume_of_the_partition = volume_of_the_ruleset(partition)
            [combination_volume.append(x) for x in volume_of_the_partition]
#        print('combination volume',combination_volume)
        combination_volume = sum_equal_dimensions(combination_volume)
#        print('combination volume',combination_volume)
        combinations_volumes.append(combination_volume)
    return combinations_volumes
# -*- coding: utf-8 -*-
"""

Function that takes a set of sets of rules, each one corresponding
to a different partition of an original connected set

e.g set1, set2, set3 . . .

and return the set (partition) with greater "volume".


"""
from copy import deepcopy
#-----------------------------------------------
# Function "compare" takes two single volumes
# that could have different volume and dimension
# [volume1, dimension1] [volume2, domension2]
# and returns the maximum considering volume
# and dimension.
#-----------------------------------------------
def compare(vol1,vol2):
    if vol1[1] > vol2[1]:
        return 1
    elif vol1[1] < vol2[1]:
        return 2
    elif vol1[0] > vol2[0]:
        return 1
    elif vol1[0] < vol2[0]:
        return 2
    else:
        return 3

#print(compare([4,1],[3,1]))

#-------------------------------------------------
#  This function takes two volumes (one beguins being the
#  winner and the other the contendent) that may have
#  different dimensions e.g [[0,0],[2,1],[2,4]] and [[3,1],[1,4]]
#  and returns:
#  1  if the winner has the bigger volume.
#  2  if the contendent has the bigger volume.
#  3  if they are tie .
#  They fight to see which one winns.
#-------------------------------------------------
def fight(winner, contendent):
    winner_copy = deepcopy(winner)
    contendent_copy = deepcopy(contendent)

    hand1 = winner[-1]
    hand2 = contendent[-1]
    result = 3

    while result == 3 and len(winner) > 0 and len(contendent) > 0:
        hand1 = winner[-1]
        del winner[-1]
        hand2 = contendent[-1]
        del contendent[-1]

        result = compare(hand1, hand2)
        if result == 1:
            return winner_copy
        if result == 2:
            return contendent_copy
        if result == 3:
            result = 3
    if result == 3:
        return winner_copy
    else:
        return result
#print( fight( [[0,0],[5,1],[4,2]], [[10,1],[4,2]]) )
#print(fight([[0,0],[1,2]],[[0,0]]))
#print(fight( [[4, 1], [0, 0]], [[8, 1], [0, 0]]))

#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#   This function receives an array with the volumes of the different
#   combinations created from the different partitions of the rules 
#   -the different ways of solving the contradictions-
#   and return the index of the bigest one
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#def find_combination_with_maximum_volume(volumes_of_the_combinations):
#    if volumes_of_the_combinations:
#        maximum_volume = volumes_of_the_combinations[0]
#    for i in range(len(volumes_of_the_combinations)):
#        maximum_volume = fight(maximum_volume,volumes_of_the_combinations[i])
#    for i, j in enumerate(volumes_of_the_combinations):
#        if j == maximum_volume:
#            index = i
#    print(i)
#    return i
def find_combination_with_maximum_volume(volumes_of_the_combinations):
    if volumes_of_the_combinations:
        maximum_volume = volumes_of_the_combinations[0]
    if len(volumes_of_the_combinations)==1:
        return 0
    for i in range(len(volumes_of_the_combinations)):
        maximum_volume = fight(maximum_volume,volumes_of_the_combinations[i])
    for i, j in enumerate(volumes_of_the_combinations):
        if j == maximum_volume:
            index = i
    return i

#
#
#       Given ( cores, new coming pattern)        
#       adjust the cores to incorporate the new instance 
#       such that the resulting cores have the maximum possible volume
#
#
#from find_intersected_rules import find_intersected_rules
#from create_rule_partitions import create_rule_partitions
#from create_combinations_from_rule_partitions import create_combinations_from_rule_partitions
#from partitions_volumes import partition_volumes
#from compare_partitions_volumes import find_combination_with_maximum_volume

def Diff(li1, li2): 
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
        return li_dif

def adjust_cores(cores,pattern):
    partitions = []
    # 1. find intersected rules
    intersected_rules = find_intersected_rules(pattern, cores)
    # 2. for each intersected rule create rule partitions
    [partitions.append(create_rule_partitions(rule,pattern)) for rule in intersected_rules]
    #print('these the partitions of the intersected rules: ')
    #[print(partition) for partition in partitions]
    # 3. create all the combinations
    combinations = create_combinations_from_rule_partitions(partitions)
    #print('C O M B I N A T I O N S of the partitions ','\n',combinations)
    # 4. find the combination with maximum volume
    # 4.1 calculate the volume of each combination
    volumes_of_the_combinations = partition_volumes(combinations) 
    #print('volumes_of_the_combinations',volumes_of_the_combinations)
    index_of_max_volume = find_combination_with_maximum_volume(volumes_of_the_combinations)
    result = combinations[index_of_max_volume]
    #print('....................................')
    adjusted_cores = []
    [adjusted_cores.append(rule) for combination in result for rule in combination if rule not in adjusted_cores]
#    print(adjusted_cores)
    # add to the result the cores that were not affected
    result = Diff(cores,intersected_rules)
#    print(result)
    [result.append(c) for c in adjusted_cores]
#    print(result)
    return result

##    If the pattern intersects a core of different class, there are two possibilities:
##    1. inside the core
##    One dimension
#Example 1
#rules = [ [{8},{3,5},'A'] ]
#pattern =  (8,   4,  'B')
#print(adjust_cores(rules,pattern))

##Example 2
#rules = [ [{8},{3,5,7},'A'] ]
#pattern =  (8,   4,  'B')
##    Two dimensions
##Example 3
#rules = [ [{8,11},{3,5},'A'] ]
#pattern =  (9,   4,  'B')
##Example 4
#rules = [ [{8,11,14},{3,5},'A'] ]
#pattern =  (9,   4,  'B')
#
##    2. on the border
##Example 5 -- note that the rule is cut by one of the two dimensions
#rules = [ [{8,10},{3,5,7},'A'] ]
#pattern =  (9,  3,  'B')
#
## Two rules intersected by a new pattern inside the cores.
##Example 6
#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (8,5,'B')
#
##Example 7 (not on the notebook)
##  an intersected rule of different class and a non intersected rule
#rules = [ [{8},{3,5},'A'], [{2},{6},'A'] ]
#pattern =  (8,   4,  'B')
#
#
#
#
#print(adjust_cores(rules,pattern))
#
