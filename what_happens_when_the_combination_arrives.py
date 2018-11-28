#
#
#        Given a set of Rules or Cores and a new combination or pattern
#        find What happens when the combination arrives?
#        1. Intersects cores with different class
#        2. Intersects or Interacts with cores of the same category
#        3. None of the above
#
#
from find_intersect_or_interact import find_intersected_rules 
def what_happends_when_the_combination_arrives(combination,cores):
    # 1. Find which cores are intersected (same class or different class)
    [intersected_cores,same_class] =find_intersected_rules(combination,cores)
    print(intersected_cores, same_class)
    # 2. There are three posibilities:
    
    # 2.1 the combination intersects rules of different class

    # 2.2 the combination intersects or interacts with cores of the same class

    # 2.3 none of the avobe

combination = (3, 7, 'B')

cores = [
        [{1,4}, {6,8}, 'A']
        ] 

what_happends_when_the_combination_arrives(combination,cores)
