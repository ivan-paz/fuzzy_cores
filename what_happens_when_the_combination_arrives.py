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
def what_happends_when_combination_arrives(combination,cores):
    # 1. Find which cores are affected
    # Different class intersected
    # Same class intersected or interaction with
    # All of the avobe
    # None of the avobe
    #
    #The combinations of the result below give that information
    [affected_rules, there_are_same_class] = collect_interserting_or_interacting_rules(combination,cores)
    #print(combination,affected_rules,there_are_same_class) 
    if there_are_same_class == True:
        # 1. breack the affected rules and call RuLer
        return 'same class'
        # 2. solve the contradictions
    else:
        if affected_rules:
        # 1. call find optimum partition
            return 'different class'
        else:
            return 'nothing'

