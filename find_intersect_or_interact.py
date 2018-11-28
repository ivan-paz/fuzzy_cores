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

# intersection with numeric intervals
# find if a rule is intersected by the combination
# find if they have the same of different class
def intersection(r1,r2):
    they_have_the_same_class = False
    if same_class(r1,r2):
        they_have_the_same_class = True    
    for i in range(len(r1)-1):
        interval1 = create_interval(r1[i])
        interval2 = create_interval(r2[i])
        if not interval_intersection(interval1,interval2):
            return [False, they_have_the_same_class]
    return [True,they_have_the_same_class]

# find which rules are intersected by a pattern
# return same class if at least one of those rules have the same class as the pattern
def find_intersected_rules(pattern,rules):
    intersected = []
    intersected_rules_same_class = False
    for r in rules:
        [they_intersect,they_have_same_class] = intersection(r,pattern)
        if they_intersect:
            intersected.append(r)
        if they_have_same_class:
            intersected_rules_same_class = True
    return [intersected,intersected_rules_same_class]

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (7,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#pattern = (8,5,'B')
#print(find_intersected_rules(pattern, rules))

#rules = [ [{1, 2}, {150}, {0.721901},'1'],[{2},{100,200},{0.721901},'1'] ]
#pattern = (   2, 120,  0.721901, '2')
#print(find_intersected_rules(pattern,rules))
