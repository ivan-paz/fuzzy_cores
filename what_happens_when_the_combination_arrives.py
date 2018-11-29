#
#
#        Given a set of Rules or Cores and a new combination or pattern
#        find What happens when the combination arrives?
#        1. Intersects cores with different class
#        2. Intersects or Interacts with cores of the same category
#        3. both of the above
#        4. None of the above
#
#
from find_intersect_or_interact import collect_interserting_or_interacting_rules

def what_happends_when_the_combination_arrives(combination,cores):
    # 1. Find which cores are affected
    # Different class intersected
    # Same class intersected or interaction with
    # All of the avobe
    # None of the avobe
    #
    #The combinations of the result below give that information
    [affected_rules, there_are_same_class] = collect_interserting_or_interacting_rules(combination,cores)
    print(affected_rules,there_are_same_class) 

combination = (3, 7, 'B')
cores = [  [{1,4}, {6,8}, 'A']  ] 
what_happends_when_the_combination_arrives(combination,cores)

combination = (3, 7, 'B')
cores = [  [{1,4}, {6,8}, 'B']  ] 
what_happends_when_the_combination_arrives(combination,cores)

combination = (3, 7, 'B')
cores = [  [{1,4}, {6,8}, 'A'], [{3},{10},'B']  ] 
what_happends_when_the_combination_arrives(combination,cores)


combination = (3, 7, 'B')
cores = [  [{1,4}, {10}, 'A']  ] 
what_happends_when_the_combination_arrives(combination,cores)

