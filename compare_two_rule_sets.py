#    --------------------------------------------------------------------------------
#
#
#    compare two rule sets A and B
#    find which rules in A are not in B
#
#
#
#
#    --------------------------------------------------------------------------------


A = [[(5,), (6,), 'A'], [(3,), (3, 5), 'A'], [(2, 3, 7), (3,), 'A'], [(5,), (4,), 'B'], [(4, 6), (3,), 'B']]
B = [[(2, 3), (3,), 'A'], [(4, 6), (3,), 'B'], [(7,), (3,), 'A']]

def _issubset(a,b):
    if set(a).issubset(set(b)):
        return True
    else:
        return False
#print( issubset( (5,),(4,6)) )

def is_contained(r1,r2):
    if r1[-1] != r2[-1]:
        return False
    else:
        subsets = 0
        for i in range(len(r1) -1):
            if _issubset(r1[i],r2[i]):
                subsets+=1
        if subsets == len(r1)-1:
            return True
#print(is_contained( [(7,), (3,), 'A'],[(2, 3, 7), (3,), 'A']) )

def set_difference(A,B):
    difference = []
    indexes = []
    for r1 in A:
        a_rule_is_contained = False
        for r2 in B:
            if is_contained(r2,r1):
                a_rule_is_contained = True
        if a_rule_is_contained == False:
            difference.append(r1)
    return difference
#print( set_difference(A,B) )
                
