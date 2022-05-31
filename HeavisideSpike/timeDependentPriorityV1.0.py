"""
timeDependentPriority.py

This script contains a callable function,
updatePriority, which updates the time b-
ased priority of all jobs in a list, L.

Note it uses the Heaviside Spike Model:
\[
    P = P_o + \frac{A}{\left(TFJR - MT\right)^2}
\]

Where $P$ represents the new priority of
a job, j; $P_o$ represents the initial p-
riority of a job, j; $A$ represents the 
weight of the weight of the time depende-
nt component; $TFJR$ represents the time 
from job request; and $MT$ represnts the 
maximum acceptable wait time for a job.

$TFJR$ is given by:
\[
    TFJR = TTE - RT
\]

Where $TTE$ represents the total time el-
apsed; and RT represents the request time
(i.e., the time the job was requested).

Modules required to run this script:

NONE

Jose Antonio Klautau Toffoli
2022-05-30
"""

# FUNTION: Update Priority.
def updatePriority (L, TTE, MTWI = 30, MTDT = 15, A = 6):
    """
    updatePriority (L, t)
    
    Updates the time based priority of all jobs in L.

    :PARAMETERS:

    L: lst
        List containing jobs.

    TTE: float
        Total time elapsed in seconds.

    MTWI: float
        Max time for walk in in seconds.

    MTDT: float
        Max time for drive through in seconds.

    A: float
        Parameter that indicates the weight of the time dependent component.

    :RETURNS:

    VOID FUNCTION
    """

    for i in range(len(L)):

        TFJR = TTE - L[i].RT                       # TIME FROM JOB REQUEST

        if L[i].DM == 'WI':
            if TFJR >= MTWI:
                L[i].P = float('inf')             # MAX PRIORITY
                continue
        
            L[i].P = L[i].Po + A/(TFJR - MTWI)**2  # NEW PRIORITY
        
        elif L[i].DM == 'DT':
            if TFJR >= MTDT:
                L[i].P = float('inf')             # MAX PRIORITY
                continue

            L[i].P = L[i].Po + A/(TFJR - MTDT)**2  # NEW PRIORITY



### TESTING COMPUTATIONAL TIME ############
'''
TEST:
    Time in second it takes to update the 
    priority of a list, L, containing n 
    jobs in it.

RESULTS:
    | n Jobs     | Time to update n jobs |

    | 0-200      |      0.000000s        |
    | 2.000      |      0.000100s        |
    | 20.000     |      0.005999s        |
    | 200.000    |      0.063001s        |
    | 2.000.000  |      0.610999s        |
    | 20.000.000 |      5.981997s        |

COMMENTS:
    Given we plan on using this script for 
    optimizing line production in a fastf-
    ood scnerario, we won't be seeing lis-
    ts with length of high orders of magn-
    itude. Thus, the computational time is
    acceptable given our intentions.

Jose Antonio Klautau Toffoli
2022-05-30
'''

class job ():

    def __init__(self, RT, Po, DM):
        
        self.DM = DM
        self.RT = RT
        self.Po = Po
        self.P  = Po


if __name__ == "__main__":

    import time

    L = []

    for i in range(1000):

        L.append(job(15, 2, 'WI'))
        L.append(job(15, 2, 'DT'))

    # print("ORIGINAL PRIORITY")
    # for i in range(len(L)):
    #     print(L[i].P)

    to = time.time()
    updatePriority(L, 44)
    t  = time.time()

    # print("UPDATED PRIORITY")
    # for i in range(len(L)):
    #     print(L[i].P)
    
    print(f'\nIt took {t - to}s to run.')
    quit()

    
    

