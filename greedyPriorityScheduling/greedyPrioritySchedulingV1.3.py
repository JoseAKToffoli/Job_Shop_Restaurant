"""
Greedy Priority Scheduling.py

This script is a sorting algorithm that is a greedy 
solution for the knapsack problem. It can be import-
ed as a module and contains the following callable 
functions:

* GreedyPriorityScheduler - Takes in a list, L, and 
returns the list sorted based on priority. 

And the following support functions:

* getPivot - Choose the job p with the largest prior-
ity such that its TTC is maximal while less than or 
equal to TOT of the previous pivot.

* SchedulerRecursion - Recursivelly sorts jobs in L 
around its pivot, p.

Modules required to run this script:

* NONE

Jose Antonio Klautau Toffoli
2022-06-05
"""

### IMPORTS ###
import sys 
###############

# SUPPORT FUNCTION: Get Pivot.
def getPivot (L, prevPivot = None):
    """
    getPivot (L, prevPivot)
    
    Choose the job p with the largest priority such that 
    its TTC is maximal while less than or equal to TOT of
    the previous pivot. In case of multiple infinite priorities, 
    we take the order that was first requested to be of highest 
    priority. 
    
    :PARAMETERS:
    
    L: lst
        List containing jobs.
    
    prevPivot: job
        Previous pivot job, p.
    
    :RETURNS:
    
    p: job
        Privot job, p, chosen based on best fit (HOLDEN)
    """

    priorityL   = [j.priority for j in L]
    maxPriority = max(priorityL)

    indicesOfMaxP = [jPriority for jPriority in range(len(priorityL)) if priorityL[jPriority] == maxPriority]
    
    # CONDITION 1: JOBS OF INF PRIORITY.
    if maxPriority == float('inf'):

        p = L[indicesOfMaxP[0]]

        for i in range(len(indicesOfMaxP) - 1):
            if L[indicesOfMaxP[i+1]].RT < p.RT:
                p = L[indicesOfMaxP[i+1]]
        
        return p

    # CONDITION 2: JOBS OF EQUAL MAXIMUM FINITE PRIORITY.
    p = None

    for i in indicesOfMaxP:

        # NO PREVIOUS PIVOT.
        if prevPivot == None:
            
            # FIRST PIVOT.
            if p == None:
                p =  L[i]
                continue 

            elif L[i].TTC > p.TTC:
                p = L[i]
    
        # LOKING FOR FIRST PIVOT WITH A PREVIOUS PIVOT.
        elif p == None:
            if L[i].TTC <= prevPivot.TOT:
                
                p =  L[i]
            continue

        # LOOKING FOR PIVOT WITH TTC <= TOT OF PREVIOUS PIVOT.
        elif L[i].TTC <= prevPivot.TOT and L[i].TTC > p.TTC:
            p = L[i]

    # CONDITION 3: IF NO PIVOTS WERE FOUND AT GIVEN PRIORITY CYCLE THROUGH NEXT HIGHEST PRIORITY.
    if p == None:

        recurL = []

        for j in L:
            if j.priority != maxPriority:
                recurL.append(j)

        p = getPivot(recurL, prevPivot)

    return p

# SUPPORT FUNCTION: Scheduler Recursion (SOURCED FROM HOLDEN).
def SchedulerRecursion (p, capacity, L):
    """
    SchedulerRecursion (p, capacity, L)

    Recursivelly sorts jobs in L around its pivot, p.

    :PARAMETERS:

    p: job
        Privot job, p.

    capacity: float
        Knapsack capacity.

    L: lst
        List containing jobs.

    :RETURNS:
    
    outList: lst
        Sorted list around the pivot.

    """

    if capacity <= 0 or len(L) == 0:
        return []
    
    elif len(L) == 1:
        if L[0].TOT <= capacity:
            return[L[0]]

        else:
            return []

    outList = []

    q = getPivot (L, p)

    L.remove(q)

    left = SchedulerRecursion (q, q.TTC, L)

    for x in left :
        outList.append(x)

        print(len(L), x, q)
        L.remove(x)
        print(len(L))
    
    outList.append(q)

    right = SchedulerRecursion (q, capacity-q.TTC, L)

    for y in right:
        outList.append(y)
        L.remove(y)

    return outList


# FUNCTION: Greedy Priority Scheduler (SOURCED FROM HOLDEN).
def GreedyPriorityScheduler (L):
    """
    GreedyPriorityScheduler (L)

    Function that Takes in a list, L, and returns it s-
    orted based on priority. 

    :PARAMETERS:

    L: lst
        List containing jobs.

    :RETURNS:

    finalList: lst
        Sorted list, based on priority, containing all orders.
    """

    p = None
    finalList = []

    while len(L) > 0:

        p = getPivot (L, p)

        L.remove(p)

        SchedulerRecursion (p, p.TTC, L)

        finalList.append(p)

    return finalList


### TESTS ######################################
'''
TESTING GET PIVOT FUNCTION:

    TEST 01: (CONDITION 2)
        Checks if get pivot function get the 
        job with highest priority, and all its
        conditions work properly.

    TEST 02: (CONDITION 3)
        Checks if get pivot function get the 
        job with highest priority given multiple
        items of max priority, and all its
        conditions work properly.

    TEST 03: (CONDITION 1)
        Checks if get pivot function get the 
        job with highest infinite priorities, 
        and all its conditions work properly.

TESTING GREEDY PRIORITY SCHEDULER FUNCTION:

    TEST 04:

    TEST 05:

    TEST 06:

RESULTS:

    TEST 01:
        Expected results were achieved for 
        the algorithm's given set up.

    TEST 02:
        Expected results were achieved for 
        the algorithm's given set up.

    TEST 03:
        Expected results were achieved for 
        the algorithm's given set up.

    TEST 04:

    TEST 05:

    TEST 06:


COMMENTS:
    Outcomes tested seemed satisfatory. Thus,
    we shall move on and test the sorting algo-
    rythm alongside our function.
    
Jose Antonio Klautau Toffoli
2022-06-05
'''

class Job ():

    def __init__(self, Po, TTC, COT, RT):
    
        self.Po = Po
        self.priority  = Po
        self.TTC = TTC
        self.COT = COT
        self.TOT = TTC + COT
        self.RT  = RT

def getPivotTests():

    print("GET PIVOT TESTS...\n")
    
    # TEST 01: 
    '''
    => SET UP FOR TEST 01:

    JOB | P | TTC | COT | TOT | RT

    0   | 1 | 1   | 1   | 2   | 1
    1   | 3 | 2   | 1   | 3   | 1
    2   | 3 | 3   | 1   | 4   | 1
    3   | 3 | 3   | 1   | 4   | 1
    4   | 1 | 1   | 1   | 2   | 1

    => Prev Pivot:
    -1  | 4 | 1   | 1   | 2   | 1

    => Expected pivot w/ prev pivot:
        JOB 01

    => Expected pivot w/out prev pivot:
        JOB 02
    '''

    L   = []
    P   = [1, 3, 3, 3, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 1, 1]

    prevPivot = Job (
        Po  = 4,
        TTC = 1,
        COT = 1,
        RT  = 1
    )

    for i in range(len(P)):
        
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    pivot = getPivot(L, prevPivot)
    print(f"TEST 01 PIVOT JOB w/ PREV PIVOT   : {'PASS' if L.index(pivot) == 1 else 'FAIL'} | EXPECT: JOB 01")

    pivot = getPivot(L)
    print(f"TEST 01 PIVOT JOB w/out PREV PIVOT: {'PASS' if L.index(pivot) == 2 else 'FAIL'} | EXPECT: JOB 02")


    # TEST 02:
    '''
    => SET UP FOR TEST 02:

    JOB | P | TTC | COT | TOT | RT

    0   | 1 | 1   | 1   | 2   | 1
    1   | 3 | 2   | 1   | 3   | 1
    2   | 4 | 3   | 1   | 4   | 1
    3   | 4 | 3   | 1   | 4   | 1
    4   | 1 | 1   | 1   | 2   | 1

    => Prev Pivot:
    -1  | 4 | 1   | 1   | 2   | 1

    => Expected pivot w/ prev pivot:
        JOB 01

    => Expected pivot w/out prev pivot:
        JOB 02
    '''

    L   = []
    P   = [1, 3, 4, 4, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 1, 1]

    prevPivotJ = Job (
        Po  = 4,
        TTC = 1,
        COT = 1,
        RT  = 1
    )

    for i in range(len(P)):
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    pivot = getPivot(L, prevPivotJ)
    print(f"TEST 02 PIVOT JOB w/ PREV PIVOT   : {'PASS' if L.index(pivot) == 1 else 'FAIL'} | EXPECT: JOB 01")

    pivot = getPivot(L)
    print(f"TEST 02 PIVOT JOB w/out PREV PIVOT: {'PASS' if L.index(pivot) == 2 else 'FAIL'} | EXPECT: JOB 02")

    # TEST 03:
    '''
    => SET UP FOR TEST 02:

    JOB | P | TTC | COT | TOT | RT

    0   | 1 | 1   | 1   | 2   | 1
    1   | 3 | 2   | 1   | 3   | 1
    2   |inf| 3   | 1   | 4   | 1
    3   |inf| 3   | 1   | 4   | 2
    4   | 1 | 1   | 1   | 2   | 1

    => Prev Pivot:
    -1  | 4 | 1   | 1   | 2   | 1

    => Expected pivot w/ prev pivot:
        JOB 02

    => Expected pivot w/out prev pivot:
        JOB 02
    '''

    L   = []
    P   = [1, 3, float("inf"), float("inf"), 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 2, 1]

    prevPivotJ = Job (
        Po  = 4,
        TTC = 1,
        COT = 1,
        RT  = 1
    )

    for i in range(len(P)):
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    pivot = getPivot(L, prevPivotJ)
    print(f"TEST 03 PIVOT JOB w/ PREV PIVOT   : {'PASS' if L.index(pivot) == 2 else 'FAIL'} | EXPECT: JOB 02")

    pivot = getPivot(L)
    print(f"TEST 03 PIVOT JOB w/out PREV PIVOT: {'PASS' if L.index(pivot) == 2 else 'FAIL'} | EXPECT: JOB 02")

    print("\nGET PIVOT TESTS...DONE\n")

def GreedyPrioritySchedulerTests():

    print("GREEDY PRIORITY SCHEDULLER TESTS...\n")
    
    # TEST 04: 
    '''
    => SET UP FOR TEST 04:

    JOB | P | TTC | COT | TOT | RT | EXP RES

    0   | 1 | 1   | 1   | 2   | 1  | 
    1   | 3 | 2   | 1   | 3   | 1  | 
    2   | 3 | 3   | 1   | 4   | 1  | 
    3   | 3 | 3   | 1   | 4   | 1  | 
    4   | 1 | 1   | 1   | 2   | 1  | 

    => Expected result:
        []
    '''

    L   = []
    P   = [1, 3, 3, 3, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 1, 1]

    for i in range(len(P)):
        
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    expL = []

    # sys.setrecursionlimit(1500)
    # print(f"TEST 04 SORTED LIST: {'PASS' if GreedyPriorityScheduler(L) == expL else 'FAIL'} | EXPECT: []")

    try:
        print(f"TEST 04 SORTED LIST: {'PASS' if GreedyPriorityScheduler(L) == expL else 'FAIL'} | EXPECT: []")
    except RecursionError:
        print(f'TEST 04 SORTED LIST: FAIL | CAUSE: RecursionError')

    # TEST 05:
    '''
    => SET UP FOR TEST 05:

    JOB | P | TTC | COT | TOT | RT | EXP RES

    0   | 1 | 1   | 1   | 2   | 1  |
    1   | 3 | 2   | 1   | 3   | 1  |
    2   | 4 | 3   | 1   | 4   | 1  |
    3   | 4 | 3   | 1   | 4   | 1  |
    4   | 1 | 1   | 1   | 2   | 1  |

    => Expected result:
        []
    '''

    L   = []
    P   = [1, 3, 4, 4, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 1, 1]

    for i in range(len(P)):
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    expL = []

    try:
        print(f"TEST 05 SORTED LIST: {'PASS' if GreedyPriorityScheduler(L) == expL else 'FAIL'} | EXPECT: []")
    except RecursionError:
        print(f'TEST 05 SORTED LIST: FAIL | CAUSE: RecursionError')

    # TEST 06:
    '''
    => SET UP FOR TEST 06:

    JOB | P | TTC | COT | TOT | RT | EXP RES

    0   | 1 | 1   | 1   | 2   | 1  |
    1   | 3 | 2   | 1   | 3   | 1  |
    2   |inf| 3   | 1   | 4   | 1  |
    3   |inf| 3   | 1   | 4   | 2  |
    4   | 1 | 1   | 1   | 2   | 1  |

    => Expected result:
        []
    '''

    L   = []
    P   = [1, 3, float("inf"), float("inf"), 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]
    RT  = [1, 1, 1, 2, 1]

    for i in range(len(P)):
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i],
            RT  = RT[i]
            )
        )

    expL = []

    try:
        print(f"TEST 06 SORTED LIST: {'PASS' if GreedyPriorityScheduler(L) == expL else 'FAIL'} | EXPECT: []")
    except RecursionError:
        print(f'TEST 06 SORTED LIST: FAIL | CAUSE: RecursionError')

    print("\nGREEDY PRIORITY SCHEDULLER TESTS...DONE\n")

if __name__ == '__main__':

    getPivotTests()
    GreedyPrioritySchedulerTests()

    quit()
