#
#    Given a new pattern and a set of connected rules
#    find the rules intersected by the pattern
#
def same_class(r1,r2):
    if r1[-1] == r2[-1]:
        return True
    else:
        return False

# Create interval
def create_interval(some_input):
    if type(some_input) == int or type(some_input) == float:
        some_input = set([some_input])
    minimum = min(some_input)
    maximum = max(some_input)
    return (minimum,maximum)

#  True if two intervals, defined by its minimum and maximum values,
#intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False

# Find if ALL the intervals of two rules
# INTERSECT each other (the intersection uses numeric values)
def intersection(r1,r2):
    for i in range(len(r1)-1):
        interval1 = create_interval(r1[i])
        interval2 = create_interval(r2[i])
        if not interval_intersection(interval1,interval2):
            return False
    return True

# Find if ALL intervals of two rules INTERSECT OR INTERACT
def intersects_or_interacts(pattern,r):
    for i in range(len(r)-1):
        interval1 = create_interval(pattern[i])
        interval2 = create_interval(r[i])
        if interval_intersection(interval1,interval2):
            return True 
    return False

#
#   this function collects the intersected rules and the interacting rules
#   Also, it TELLS if THERE ARE INTERACTING RULES (to apply the RuLer)
def collect_interserting_or_interacting_rules(pattern,rules):
    collected_rules = []
    the_pattern_interacts_with_at_least_one_rule = False
    for r in rules:
        if same_class(r, pattern):
            if intersects_or_interacts(pattern,r):
                collected_rules.append(r)
                the_pattern_interacts_with_at_least_one_rule = True
        else:
            if intersection(r,pattern):
                collected_rules.append(r)
    return [collected_rules, the_pattern_interacts_with_at_least_one_rule]

#def find_intersected_rules(pattern,rules):
#    intersected = []
#    intersected_rules_same_class = False
#    for r in rules:
#        [they_intersect,they_have_same_class] = intersection(r,pattern)
#        if they_intersect:
#            intersected.append(r)
#        if they_have_same_class:
#            intersected_rules_same_class = True
#    return [intersected,intersected_rules_same_class]



#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (7,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (8,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [ [{1, 2}, {150}, {0.721901},'1'],[{2},{100,200},{0.721901},'1'] ]
#pattern = (   2, 120,  0.721901, '2')
#print(find_intersected_rules(pattern,rules))
