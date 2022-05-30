"""
job.py

This script is the blue prints for a Job Class that
will be used to construct list of jobs for the knap-
sack problem.

Modules required to run this script:

* NONE

Jose Antonio Klautau Toffoli
2022-05-30
"""

### IMPORTS ###

###############

class Job () :

    def __init__(self, COT, cycleTime, P0):
        
        self.COT = COT
        self.TTC = cycleTime
        self.TOT = COT + cycleTime
        self.idleTime = 0

        self.P = P0
        
        
        self.to = 