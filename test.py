#
import sys
from find_intersect_or_interact import same_class
from find_intersect_or_interact import create_interval
from find_intersect_or_interact import interval_intersection
from find_intersect_or_interact import intersection
from find_intersect_or_interact import intersects_or_interacts
from find_intersect_or_interact import collect_interserting_or_interacting_rules
def test(l):
        l()
        sys.stdout.write('.')

def xxx():
    r1 = [{1,3}, {6,7}, 'A']
    r2 = [{9},   {6,7}, 'A']
    assert same_class(r1,r2) == True
test(xxx)

def xxx():
    r1 = [{1,3}, {6,7}, 'A']
    r2 = [{9},   {6,7}, 'B']
    assert same_class(r1,r2) == False
test(xxx)

def xxx():
    assert create_interval(1) == (1,1)
    assert create_interval({4,6}) == (4,6)
test(xxx)

def xxx():
    assert interval_intersection( (1,11),(9,12) ) == True
    assert interval_intersection( (2,5),(7,11) ) == False
    assert interval_intersection( (1,11), (11,15) ) == True
    assert interval_intersection( (4,4), (2,5) ) == True
    assert interval_intersection( (8,8),  (7,9)  ) == True
test(xxx)

def xxx():
    assert intersection( [{1,3},{2},'A'], (2,2,'B') ) == True
    assert intersection( [{1,3},{2},'A'], (2,3,'B') ) == False
test(xxx)

def xxx():
    #ithis intersects
    pattern = (4,8,'A')
    r = [{2,5},{7,9},'A']
    assert intersects_or_interacts(pattern,r) == True
    #this interacts
    pattern = (4,8,'A')
    r = [{4},{12},'A']
    assert intersects_or_interacts(pattern,r) == True
    # this does none of them
    pattern = (4,8,'A')
    r = [{5},{12},'A']
    assert intersects_or_interacts(pattern,r) == False
test(xxx)

def xxx():
    pattern = (4, 8, 'A')
    rules = [    [ {2,5},{7,9},'A'], [{2,5},{7,9}, 'B']    ] 
    assert collect_interserting_or_interacting_rules(pattern,rules) == [[[{2, 5}, {9, 7}, 'A'], [{2, 5}, {9, 7}, 'B']], True]
test(xxx)

#def xxx():
#    rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#    pattern = (7,5,'B')
#    assert find_intersected_rules(pattern, rules) == [ [[{6,10},{4,6},'A']],False]
#    rules = [[{6,10},{4,6},'A'],[{8},{3,7},'A']]
#    pattern = (8,5,'B')
#    assert find_intersected_rules(pattern, rules) == [ [[{6,10},{4,6},'A'],[{8},{3,7},'A']], False]
#    rules = [[{6,10},{4,6},'A']]
#    pattern = (7,5,'A')
#    assert find_intersected_rules(pattern, rules) == [ [[{6,10},{4,6},'A']],True]
#test(xxx)



print('\nAll passed!')
