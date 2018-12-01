from what_happens_when_the_combination_arrives import what_happends_when_combination_arrives
from optimum_partition_different_class import adjust_cores
#
#
#
def instance_to_set_format(instance):
    set_format = []
    for i in range( len(instance)-1 ):
        set_format.append(set([instance[i]]))
    set_format.append( instance[-1] )
    return set_format


def commit_cores(new_instance,cores):

    if cores == []:
        cores.append(instance_to_set_format(new_instance))
        return cores

    case = what_happends_when_combination_arrives(new_instance,cores)
    
    if case == 'same class':
        print('same class')

    elif case == 'different class':
        print('different class')
        cores = adjust_cores(cores,new_instance)

    else:
        print('nothing')
        cores.append(instance_to_set_format(new_instance))
    print(cores)



#combination = (3, 7, 'B') 
#cores = []
#commit_cores(combination,cores)

#same class
combination = (3, 7, 'B') 
cores = [  [{1,4}, {6,8}, 'A']  ]
commit_cores(combination,cores)

#nothing
combination = (5, 7, 'B') 
cores = [  [{1,4}, {6,8}, 'A']  ]
commit_cores(combination,cores)

