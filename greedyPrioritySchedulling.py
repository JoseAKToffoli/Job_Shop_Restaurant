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

# SUPPORT FUNCTION: Get Pivot One.
def getPivot (L, prevPivot):
    """
    getPivot (L, prevPivot)
    
    Choose the job p with the largest priority such t-
    hat its TTC is maximal while less than or equal to
    TOT of the previous pivot.

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

    indexesOfMaxj = [jPriority for jPriority in range(len(priorityL)) if priorityL[jPriority] == maxPriority]
    
    p = L[indexesOfMaxj[0]]
    
    if len(indexesOfMaxj) == 1:
        
        return p

    for i in range(len(indexesOfMaxj) - 1):

        if L[indexesOfMaxj[i+1]].TTC <= prevPivot.TOT and L[indexesOfMaxj[i+1]].TTC > p.TTC:

            p = L[indexesOfMaxj[i+1]]

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
