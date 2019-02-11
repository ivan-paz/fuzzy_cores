#        -----------------------------------------------------------------------
#
#                        script to run
#
#
#
#        -----------------------------------------------------------------------
from commit_cores import commit_cores
from commit_cores import tuple_to_set_format
#when there are no previous cores
#combination = (3, 7, 'B')
#cores = []
#print( commit_cores(combination,cores) )

# different class
#combination = (3, 7, 'B')
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

# nothing (no intersections)
#combination = (5, 7, 'B')
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

# same class
#combination = (3, 6, 'A')
#cores = [  [{1,4}, {6,8}, 'A']  ]
#commit_cores(combination,cores)

#data = [
#        (2,3,'A'),
#        (3,3,'A'),
#        (3,5,'A'),
#        (4,3,'B'),
#        (5,4,'B'),
#        (5,6,'A'),
#        (6,3,'B')
#        (7,3,'A')
#        ]

#data = [
#        (2,3,'A'),
#        (3,3,'A'),
#        (7,3,'A'),
#        (6,3,'B')
#        ]
#
#cores = []
#for datum in data:
#    cores = commit_cores(datum,cores)
#    if type(cores)!=list:
#        print('no es una lista')


#
#   debug
#
#
    #   Case 1 Empty cores and any instance.
cores = []
datum = (2,3,'A')
cores = commit_cores(datum,cores)
print(cores)

cores = [[{2}, {3}, 'A']]
datum = (3,3,'A')
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print(cores)


cores = [[[2, 3], [3], 'A']]
datum = (3,5,'A')
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print(cores)

cores = [[[2, 3], [3], 'A'], [[3], [3, 5], 'A']]
datum = (4,3,'B')
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print(cores)

cores = [[[2, 3], [3], 'A'], [[3], [3, 5], 'A'], [{4}, {3}, 'B']]
datum = (5,4,'B')
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print(cores)

cores = [[[2, 3], [3], 'A'], [[3], [3, 5], 'A'], [{4}, {3}, 'B'], [{5}, {4}, 'B']]
datum = (5,6,'A')
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print(cores)

cores = [[[2, 3], [3], 'A'], [[3], [3, 5], 'A'], [{4}, {3}, 'B'], [{5}, {4}, 'B'], [{5}, {6}, 'A']]
datum = (6,3,'B')
print('datum',datum)
cores = commit_cores(datum,cores)
temporal = []
for r in cores:
    temporal.append(tuple_to_set_format(r))
cores = temporal
print('CORES: ',cores)

#cores = [[[5], [6], 'A'], [[2, 3], [3], 'A'], [[3], [3, 5], 'A'], [[5], [4], 'B'], [[4, 6], [3], 'B']]
#datum = (7,3,'A')
#print('datum', datum)
#cores = commit_cores(datum,cores)
#temporal = []
#for r in cores:
#    temporal.append(tuple_to_set_format(r))
#cores = temporal
#print('CORES: ',cores)










