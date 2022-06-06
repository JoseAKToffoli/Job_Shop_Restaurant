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
2022-05-30
"""

### IMPORTS ###

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
    
    p = L[indicesOfMaxP[0]]
    
    # CONDITION 1: ONLY ONE JOB OF MAX PRIORITY.
    if len(indicesOfMaxP) == 1:
        return p

    # CONDITION 2: MULTIPLE JOBS OF INF PRIORITY.
    elif maxPriority == float('inf'):

        for i in range(len(indicesOfMaxP) - 1):
            if L[indicesOfMaxP[i+1]].RT < p.RT:
                p = L[indicesOfMaxP[i+1]]

    # CONDITION 3: MULTIPLE JOBS OF EQUAL MAXIMUM FINITE PRIORITY.
    for i in range(len(indicesOfMaxP) - 1):

        if prevPivot == None:
            if L[indicesOfMaxP[i+1]].TTC > p.TTC:
                p = L[indicesOfMaxP[i+1]]
            continue

        elif L[indicesOfMaxP[i+1]].TTC <= prevPivot.TOT and L[indicesOfMaxP[i+1]].TTC > p.TTC:
            p = L[indicesOfMaxP[i+1]]

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
    global prevQ

    if capacity <= 0 or len(L) == 0:
        return []

    elif len(L) == 1:
        if L[0].TOT <= capacity:
            return [L[0]]
        else:
            return []
    
    outList = list()

    q    = getPivot(L, prevQ)
    left = SchedulerRecursion (q, q.TTC, L)
    L.remove(q)

    for x in left:
        outList.append(x)
        L.remove(q)

    outList.append(q)

    prevQ = q

    right = SchedulerRecursion (q, capacity - q.TTC, L)

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
    global prevP, prevQ
    
    prevP, prevQ = None, None

    finalList = list()

    while len(L) > 0:

        p = getPivot(L, prevP)
        L.remove(p)

        SchedulerRecursion (p, p.TTC, L)
        finalList.append(p)

        prevP = p
    
    return finalList


### TESTING getPivot FUNCTION ############
'''
TEST 01:
    Checks if get pivot function get the 
    job with highest priority, and all its
    conditions work properly.

TEST 02:
    Checks if greedy priority scheduler 
    schedules a list of jobs L properly 
    based on priority.

RESULTS:

    TEST 01:
        Expected results were achieved for 
        the algorithm's given set up.

    TEST 02:
        Failed due to it taking an initial 
        p for comparison (LINE 63).

COMMENTS:
    To solve the logical error in LINE 63 
    we will change the logic behind getPivot.
    
Jose Antonio Klautau Toffoli
2022-05-30
'''

class Job ():

    def __init__(self, Po, TTC, COT):
    
        self.Po = Po
        self.priority  = Po
        self.TTC = TTC
        self.COT = COT
        self.TOT = TTC + COT

if __name__ == '__main__':


    # TEST 01: 
    '''
    => SET UP FOR TEST 01:

    JOB | P | TTC | COT | TOT 

    0   | 1 | 1   | 1   | 2
    1   | 3 | 2   | 1   | 3 
    2   | 3 | 3   | 1   | 4
    3   | 3 | 3   | 1   | 4
    4   | 1 | 1   | 1   | 2

    => Prev Pivot:
    -1  | 4 | 1   | 1   | 2

    => Expected pivot w/ prev pivot:
        JOB 01

    => Expected pivot w/out prev pivot:
        JOB 02
    '''

    L   = []
    P   = [1, 3, 3, 3, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]

    prevPivot = Job (
        Po  = 4,
        TTC = 1,
        COT = 1
    )

    for i in range(len(P)):
        
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i]
            )
        )

    pivot = getPivot(L, prevPivot)
    print(f"TEST 01 PIVOT JOB w/ PREV PIVOT   : {L.index(pivot)}")

    pivot = getPivot(L)
    print(f"TEST 01 PIVOT JOB w/out PREV PIVOT: {L.index(pivot)}")


    # TEST 02:
    '''
    => SET UP FOR TEST 02:

    JOB | P | TTC | COT | TOT 

    0   | 1 | 1   | 1   | 2
    1   | 3 | 2   | 1   | 3 
    2   | 4 | 3   | 1   | 4
    3   | 4 | 3   | 1   | 4
    4   | 1 | 1   | 1   | 2

    => Prev Pivot:
    -1  | 4 | 1   | 1   | 2

    => Expected pivot w/ prev pivot:
        JOB 01

    => Expected pivot w/out prev pivot:
        JOB 02
    '''

    L   = []
    P   = [1, 3, 4, 4, 1]
    TTC = [1, 2, 3, 3, 1]
    COT = [1, 1, 1, 1, 1]

    prevPivot = Job (
        Po  = 4,
        TTC = 1,
        COT = 1
    )

    for i in range(len(P)):
        
        L.append (
            Job ( 
            Po  = P[i], 
            TTC = TTC[i], 
            COT = COT[i]
            )
        )

    pivot = getPivot(L, prevPivot)
    print(f"TEST 02 PIVOT JOB w/ PREV PIVOT   : {L.index(pivot)}")

    pivot = getPivot(L)
    print(f"TEST 02 PIVOT JOB w/out PREV PIVOT: {L.index(pivot)}")
