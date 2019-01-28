#        -----------------------------------------------------------------------
#
#                        script to run
#
#
#
#        -----------------------------------------------------------------------

from commit_cores import commit_cores

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

data = [
        (2,3,'A'),
        (3,3,'A'),
        (3,5,'A'),
        (4,3,'B'),
        (5,4,'B'),
        (5,6,'A'),
        (6,3,'B')
#        (7,3,'A')
        ]

#data = [
#        (2,3,'A'),
#        (3,3,'A'),
#        (7,3,'A'),
#        (6,3,'B')
#        ]
#
cores = []
for datum in data:
    cores = commit_cores(datum,cores)
    if type(cores)!=list:
        print('no es una lista')
