"""
machine.py

This script is the blue prints for a Machine Class that
will be used to implement our solution for the knapsack 
problem.

Modules required to run this script:

* jobVx.x.py
* floorVx.x.py

Jose Antonio Klautau Toffoli
2022-06-15
"""

### IMPORTS #######
from Job      import Job
from Operator import Operator

from enum     import Enum
###################

# ---------------- #
# STATIC VARIABLES #
# ---------------- #

global nextId

nextId = 1

# ---------------- #
# MEMBER VARIABLES #
# ---------------- #

class Status (Enum):
    Stopped      = 0
    Running      = 1 
    Idle         = 2 
    InChangeOver = 3
    Finished     = 4 
    Errored      = 5

class StatusStopped (Enum):
    Null  = 0
    entry = 1

class Machine ():

    def __init__(self, aActiveJob, aName, aFloor, aSchedule):

        global nextId

        status        = Status()
        statusStopped = StatusStopped()

        self.activeJob   = aActiveJob
        self.name        = aName
        self.id          = nextId

        nextId           += 1

        self.jobs        = Job.ArrayList()
        self.operators   = Operator.ArrayList()
        self.didAddFloor = self.setFloot(aFloor)

        if not self.didAddFloor:
            RuntimeError("Unable to create machine due to floor.")

        didAddSchedule = self.setSchedule(aSchedule)

        if not self.didAddSchedule:
            RuntimeError("Unable to create machine due to schedule.")
        
        self.setStatusStopped(StatusStopped.Null)
        self.setStatus(Status.Stopped)

'''
TO BE TRANSLATED
//------------------------
  // INTERFACE
  //------------------------

  public boolean setActiveJob(Job aActiveJob)
  {
    boolean wasSet = false;
    activeJob = aActiveJob;
    wasSet = true;
    return wasSet;
  }

  public boolean setName(String aName)
  {
    boolean wasSet = false;
    name = aName;
    wasSet = true;
    return wasSet;
  }

  public boolean setIsRunning(boolean aIsRunning)
  {
    boolean wasSet = false;
    isRunning = aIsRunning;
    wasSet = true;
    return wasSet;
  }

  public Job getActiveJob()
  {
    return activeJob;
  }

  public String getName()
  {
    return name;
  }

  public boolean getIsRunning()
  {
    return isRunning;
  }

  public int getId()
  {
    return id;
  }

  public String getStatusFullName()
  {
    String answer = status.toString();
    if (statusStopped != StatusStopped.Null) { answer += "." + statusStopped.toString(); }
    return answer;
  }

  public Status getStatus()
  {
    return status;
  }

  public StatusStopped getStatusStopped()
  {
    return statusStopped;
  }

  public boolean onStart()
  {
    boolean wasEventProcessed = false;
    
    Status aStatus = status;
    switch (aStatus)
    {
      case Stopped:
        exitStatus();
        setStatus(Status.Running);
        wasEventProcessed = true;
        break;
      default:
        // Other states do respond to this event
    }

    return wasEventProcessed;
  }

  public boolean onError()
  {
    boolean wasEventProcessed = false;
    
    Status aStatus = status;
    switch (aStatus)
    {
      case Running:
        setStatus(Status.Errored);
        wasEventProcessed = true;
        break;
      default:
        // Other states do respond to this event
    }

    return wasEventProcessed;
  }

  public boolean onStartChangeOver()
  {
    boolean wasEventProcessed = false;
    
    Status aStatus = status;
    switch (aStatus)
    {
      case Idle:
        setStatus(Status.InChangeOver);
        wasEventProcessed = true;
        break;
      default:
        // Other states do respond to this event
    }

    return wasEventProcessed;
  }

  public boolean onChangeOverComplete()
  {
    boolean wasEventProcessed = false;
    
    Status aStatus = status;
    switch (aStatus)
    {
      case InChangeOver:
        if (hasNextJob())
        {
          setStatus(Status.Stopped);
          wasEventProcessed = true;
          break;
        }
        break;
      default:
        // Other states do respond to this event
    }

    return wasEventProcessed;
  }

  private void exitStatus()
  {
    switch(status)
    {
      case Stopped:
        exitStatusStopped();
        break;
    }
  }

  private void setStatus(Status aStatus)
  {
    status = aStatus;

    // entry actions and do activities
    switch(status)
    {
      case Stopped:
        if (statusStopped == StatusStopped.Null) { setStatusStopped(StatusStopped.entry); }
        break;
    }
  }

  private void exitStatusStopped()
  {
    switch(statusStopped)
    {
      case entry:
        setStatusStopped(StatusStopped.Null);
        break;
    }
  }

  private void setStatusStopped(StatusStopped aStatusStopped)
  {
    statusStopped = aStatusStopped;
    if (status != Status.Stopped && aStatusStopped != StatusStopped.Null) { setStatus(Status.Stopped); }
  }
  /* Code from template association_GetMany */
  public Job getJob(int index)
  {
    Job aJob = jobs.get(index);
    return aJob;
  }

  public List<Job> getJobs()
  {
    List<Job> newJobs = Collections.unmodifiableList(jobs);
    return newJobs;
  }

  public int numberOfJobs()
  {
    int number = jobs.size();
    return number;
  }

  public boolean hasJobs()
  {
    boolean has = jobs.size() > 0;
    return has;
  }

  public int indexOfJob(Job aJob)
  {
    int index = jobs.indexOf(aJob);
    return index;
  }
  /* Code from template association_GetMany */
  public Operator getOperator(int index)
  {
    Operator aOperator = operators.get(index);
    return aOperator;
  }

  public List<Operator> getOperators()
  {
    List<Operator> newOperators = Collections.unmodifiableList(operators);
    return newOperators;
  }

  public int numberOfOperators()
  {
    int number = operators.size();
    return number;
  }

  public boolean hasOperators()
  {
    boolean has = operators.size() > 0;
    return has;
  }

  public int indexOfOperator(Operator aOperator)
  {
    int index = operators.indexOf(aOperator);
    return index;
  }
  /* Code from template association_GetOne */
  public Floor getFloor()
  {
    return floor;
  }
  /* Code from template association_GetOne */
  public Schedule getSchedule()
  {
    return schedule;
  }
  /* Code from template association_MinimumNumberOfMethod */
  public static int minimumNumberOfJobs()
  {
    return 0;
  }
  /* Code from template association_AddUnidirectionalMany */
  public boolean addJob(Job aJob)
  {
    boolean wasAdded = false;
    if (jobs.contains(aJob)) { return false; }
    jobs.add(aJob);
    wasAdded = true;
    return wasAdded;
  }

  public boolean removeJob(Job aJob)
  {
    boolean wasRemoved = false;
    if (jobs.contains(aJob))
    {
      jobs.remove(aJob);
      wasRemoved = true;
    }
    return wasRemoved;
  }
  /* Code from template association_AddIndexControlFunctions */
  public boolean addJobAt(Job aJob, int index)
  {  
    boolean wasAdded = false;
    if(addJob(aJob))
    {
      if(index < 0 ) { index = 0; }
      if(index > numberOfJobs()) { index = numberOfJobs() - 1; }
      jobs.remove(aJob);
      jobs.add(index, aJob);
      wasAdded = true;
    }
    return wasAdded;
  }

  public boolean addOrMoveJobAt(Job aJob, int index)
  {
    boolean wasAdded = false;
    if(jobs.contains(aJob))
    {
      if(index < 0 ) { index = 0; }
      if(index > numberOfJobs()) { index = numberOfJobs() - 1; }
      jobs.remove(aJob);
      jobs.add(index, aJob);
      wasAdded = true;
    } 
    else 
    {
      wasAdded = addJobAt(aJob, index);
    }
    return wasAdded;
  }
  /* Code from template association_MinimumNumberOfMethod */
  public static int minimumNumberOfOperators()
  {
    return 0;
  }
  /* Code from template association_AddManyToManyMethod */
  public boolean addOperator(Operator aOperator)
  {
    boolean wasAdded = false;
    if (operators.contains(aOperator)) { return false; }
    operators.add(aOperator);
    if (aOperator.indexOfMachine(this) != -1)
    {
      wasAdded = true;
    }
    else
    {
      wasAdded = aOperator.addMachine(this);
      if (!wasAdded)
      {
        operators.remove(aOperator);
      }
    }
    return wasAdded;
  }
  /* Code from template association_RemoveMany */
  public boolean removeOperator(Operator aOperator)
  {
    boolean wasRemoved = false;
    if (!operators.contains(aOperator))
    {
      return wasRemoved;
    }

    int oldIndex = operators.indexOf(aOperator);
    operators.remove(oldIndex);
    if (aOperator.indexOfMachine(this) == -1)
    {
      wasRemoved = true;
    }
    else
    {
      wasRemoved = aOperator.removeMachine(this);
      if (!wasRemoved)
      {
        operators.add(oldIndex,aOperator);
      }
    }
    return wasRemoved;
  }
  /* Code from template association_AddIndexControlFunctions */
  public boolean addOperatorAt(Operator aOperator, int index)
  {  
    boolean wasAdded = false;
    if(addOperator(aOperator))
    {
      if(index < 0 ) { index = 0; }
      if(index > numberOfOperators()) { index = numberOfOperators() - 1; }
      operators.remove(aOperator);
      operators.add(index, aOperator);
      wasAdded = true;
    }
    return wasAdded;
  }

  public boolean addOrMoveOperatorAt(Operator aOperator, int index)
  {
    boolean wasAdded = false;
    if(operators.contains(aOperator))
    {
      if(index < 0 ) { index = 0; }
      if(index > numberOfOperators()) { index = numberOfOperators() - 1; }
      operators.remove(aOperator);
      operators.add(index, aOperator);
      wasAdded = true;
    } 
    else 
    {
      wasAdded = addOperatorAt(aOperator, index);
    }
    return wasAdded;
  }
  /* Code from template association_SetOneToMany */
  public boolean setFloor(Floor aFloor)
  {
    boolean wasSet = false;
    if (aFloor == null)
    {
      return wasSet;
    }

    Floor existingFloor = floor;
    floor = aFloor;
    if (existingFloor != null && !existingFloor.equals(aFloor))
    {
      existingFloor.removeMachine(this);
    }
    floor.addMachine(this);
    wasSet = true;
    return wasSet;
  }
  /* Code from template association_SetOneToMandatoryMany */
  public boolean setSchedule(Schedule aSchedule)
  {
    boolean wasSet = false;
    //Must provide schedule to machine
    if (aSchedule == null)
    {
      return wasSet;
    }

    if (schedule != null && schedule.numberOfMachines() <= Schedule.minimumNumberOfMachines())
    {
      return wasSet;
    }

    Schedule existingSchedule = schedule;
    schedule = aSchedule;
    if (existingSchedule != null && !existingSchedule.equals(aSchedule))
    {
      boolean didRemove = existingSchedule.removeMachine(this);
      if (!didRemove)
      {
        schedule = existingSchedule;
        return wasSet;
      }
    }
    schedule.addMachine(this);
    wasSet = true;
    return wasSet;
  }

  public void delete()
  {
    jobs.clear();
    ArrayList<Operator> copyOfOperators = new ArrayList<Operator>(operators);
    operators.clear();
    for(Operator aOperator : copyOfOperators)
    {
      aOperator.removeMachine(this);
    }
    Floor placeholderFloor = floor;
    this.floor = null;
    if(placeholderFloor != null)
    {
      placeholderFloor.removeMachine(this);
    }
    Schedule placeholderSchedule = schedule;
    this.schedule = null;
    if(placeholderSchedule != null)
    {
      placeholderSchedule.removeMachine(this);
    }
  }

  // line 26 "../../../umpleFile.ump"
  public boolean hasNextJob(){
    return activeJob.getNextJob()!=null && activeJob.getNextJob()!=Job.DummyJob;
  }


  public String toString()
  {
    return super.toString() + "["+
            "id" + ":" + getId()+ "," +
            "name" + ":" + getName()+ "," +
            "isRunning" + ":" + getIsRunning()+ "]" + System.getProperties().getProperty("line.separator") +
            "  " + "activeJob" + "=" + (getActiveJob() != null ? !getActiveJob().equals(this)  ? getActiveJob().toString().replaceAll("  ","    ") : "this" : "null") + System.getProperties().getProperty("line.separator") +
            "  " + "floor = "+(getFloor()!=null?Integer.toHexString(System.identityHashCode(getFloor())):"null") + System.getProperties().getProperty("line.separator") +
            "  " + "schedule = "+(getSchedule()!=null?Integer.toHexString(System.identityHashCode(getSchedule())):"null");
  }
}
'''