# OS Scheduling Algorithim Comparision (CS446-PA2)
 Compare and contrast, and simulate first come first served, shortest job first, and priority scheduling process management algorithms.

General Instructions and Hints: 

Name files exactly as described in the documentation below.
When the assignment is done, zip or tarball the specified files into a folder with the name <netid>_CS446_PA2.zip or  <netid>_CS446_PA2.tar.gz (for example sarad_CS446_PA2.tar.gz).
All work should be done on a machine where you have sudoer permission. If you do not have linux on your machine, or sudo permissions on a linux machine, there is a video about ssh-ing into the school's engineering server under files -> Lecture Recordings, or you can use any of the methods outlined hereLinks to an external site., which include a remote option to access school resources. 
The assignment must be done in Python3- trust me, it's a lot easier to sort objects in Python3 than it is in C++, and I'd like you to focus on the algorithm, not how to implement sorting. 
You may import the glob, numpy, sys, pandas, and/or os libraries if you would like.
If you are using list copies where you don't want the original to change, but would like the copy to change, then you will need to make a deep copy  (Links to an external site.)using the copy library, so you can also import that.
You can return multiple data structures from a single function in python (unlike c). 
If you hate the way that the functions are structured, you may alter your code to make more sense to you. However, all input and output should happen in main, and you should maintain the general functionality of each function- that is, there should be a function to calculate each of the averages and a function to perform each algorithm.
 

-Part 1-

***To be done individually.***

Background

Process scheduling algorithms come in many different variations, and they have many different tradeoffs to consider like resource sharing and simplicity of execution. Understanding how First Come First Served, Shortest Job First, and Priority Scheduling work will give you a better understanding of the ways in which these algorithms differ. Waiting time measures the amount of time from when a process enters a queue to when the process is executed. Turn around time measures the amount of time from when a process enters a queue to when the process is terminated. The are both used in operating systems to determine CPU usage efficiency. 

Directions

There is a test batchfile for assignment 2 part 1 in Files -> ProgrammingAssignments. Each line of the batchfile contains 4 comma separated values. They are: PID, Arrival Time, Burst Time, and Priority. PID is the process id. Arrival time is the time since the process arrived in the ready queue. Burst time is the amount of time required to fully execute the process on the CPU. Priority should only be used by the priority scheduling algorithm, and it decides which process should run first if more than one process arrives at the same time. Let's look at a simplified example of the batchfile:

1, 0, 20, 2

3, 0, 50, 1

7, 9, 4, 3

2, 10, 12, 4


Your program should consist of at least 6 functions: Main, FirstComeFirstServedSort, ShortestJobFirstSort, PrioritySort, AverageTurnaround, and AverageWait. Please note that the way Python implements main (Links to an external site.) is different than the way that C or C++ implements it. Below, I provide the general description of each of the functions. You will notice that these descriptions are much less comprehensive than the first assignment. This is because I would like you to begin working on implementing algorithms from a general description (much like you would in an interview).

Name your program batchSchedulingComparison.py 

You can implement sorting in many ways in Python: you can take your data and create a tuple (or other object) and sort a list of those objects (Links to an external site.),  you can zip, sort and unzip lists (Links to an external site.), you can create parallel lists and sort (not recommended since mistakes with this method are common), etc. In each of the sort functions, it is up to you to decide what data structures and process you use to implement the sorting algorithm. If you want to create a list of dict objects containing each of the variables and sort by key or item, that's fine. Or you could create three separate lists (one for PID, one for arrival time, and one for burst time) and sort them using zip/unzip. There are many ways to sort in python, so pick whatever makes the most sense to you.

 

Note: you will only use the priority entry in the batchfile to implement PriorityScheduling.

Main()

From the terminal, the user should be able to enter the program name batchfileName and type of process sort they would like to do. So for example: python3 batchSchedulingComparison.py batchfile.txt FCFS could be entered on the commandline when you want to run the program. If the user does not enter your three arguments (program name batchfileName and sortType), then you should prompt the user repeatedly and take their input until they enter the correct number of arguments. There are many ways to accomplish this check. You will likely want to import sys and use sys.argv (Links to an external site.) to get all of the arguments given from the command line.

Once the user supplies the correct number of arguments (which you can get by taking the length of the sys.argv list, see link above),  use argv to get the batch file name, and then read all of the data from it, if you can. If you can't (because the user entered a non-existing file name), you should tell the user that the file doesn't exist and exit the program. If you're able to read from the file name provided by the user (again there are many ways to do this, but I like using readlines()) (Links to an external site.), then you should get the algorithm name from the argv list. Expected algorithm names supplied by the user are FCFS and ShortestFirst and Priority (with that exact spelling and capitalization). If the user does not provide one of these arguments, you should tell the user that their process scheduling options are FCFS, ShortestFirst, or Priority, and exit the program. If the user enters an acceptable algorithm name, perform a logical check to see which function you should call (FirstComeFirstServedSort or ShortestJobFirstSort or PrioritySort). For each algorithm, the output to the terminal should be the processes in the order that they should execute, the average process waiting time, and the average process turn around time, each on their own line. All input and output should be gathered and executed IN MAIN.  In other words, your reading and printing should happen here. Examples of output for each algorithm are below, but please make sure that you print from main. The easiest way to do that is to have each of the algorithm functions return a list of the times that each process is completed at. Then you can pass that and the relevant data to averageTurnaround and averageWait, whose returns can be used to print the turnaround and wait times.

 

Please print to 2 decimal places. 

 

AverageTurnaround(processCompletionTimes, processArrivalTimes)

Parameters: accepts the time that the process would be completed at by the algorithm, accepts the time that each process arrives (I suggest using two lists)

Returns: (1)the average turn around, (2)a list of each process turn around times (note: Python will let you return multiple values at once. For ease of implementation, you should do that (Links to an external site.) in this function)

Turnaround time is calculated by subtracting each processCompletionTime from its arrivalTime. For example, using FCFS (see below) process 3 takes 50 seconds to execute and arrived at time 0, so process 3 has a turnaround time of 70 because it has to wait 20 seconds for process 1 to fully execute. To calculate the average, sum each process' turnaround time, and divide by the number of processes. So if we only executed process 1 and 3, we would add 20 and 70 and divide by 2- the turnaround time of those two processes averaged (ignoring the rest of the list for simplicity) is 45.

 

AverageWait(processTurnaroundTimes, processBurstTime)

Parameters: accepts the list of process turnaround times that is returned by AverageTurnaround, accepts the burst time of each process(I suggest using two lists)

Returns: (1)AverageWait

Wait time is calculated by subtracting each processBurstTime from its processTurnaroundTime. For example, using FCFS (see below) we previously calculated that process 3 has a turnaround time of 70, and process 1 has a turnaround time of 20. To calculate the waitTime for process 3, we subtract the burst time from the turnaround (70-50) and get 20; doing the same for process 1, we get 0. To calculate the average, sum each process' wait time, and divide by the number of processes. So if we only executed process 1 and 3, we would add 20 and 0and divide by 2- the wait time of those two processes averaged (ignoring the rest of the list for simplicity) is 10.

FirstComeFirstServedSort(batchFileData)

Parameters: accepts all of the batchFileData from the batchfile opened in main

Returns: (1) a list (or other data structure) of the time each process is completed at, and (2) a list (or other data structure) containing the PID of the processes in the order the algorithm sorted them by.

If the command line argument for the algorithm is FCFS, then this function will be called. The data from the batchfile should be passed in and sorted by arrival time (again, there are many ways to do this). The basic algorithm can be summarized as:

Sort processes by arrival time.
Execute in the order that they arrived.
If two processes arrive at the same time, execute the process with the smaller PID.
In the data structure of your choice, store the time that each process would be completed at. So, for example, process 1 would finish executing at time 20, process 3 would finish executing at time 70, and process 7 would finish executing at time 74.  Return your data structure with the completed times in it. 

Using the batchfile above as an example, the input would look like

python3 batchSchedulingComparison.py batchfile.txt FCFS

And the output  (FROM MAIN BASED ON YOUR RETURNED VALUES) to the screen would be:

PID ORDER OF EXECUTION

1

3

7

2

Average Process Turnaround Time: 57.75

Average Process Wait Time: 36.25

 

ShortestJobFirst(batchFileData)

Parameters: accepts all of the batchFileData from the batchfile opened in main

Returns: (1) a list (or other data structure) of the time each process is completed at, and (2) a list (or other data structure) containing the PID of the processes in the order the algorithm sorted them by.

If the command line argument states that the user wants to process batch jobs using ShortestFirst, then this function will be called. The data from the batchfile should be passed in and sorted by arrival time (again, there are many ways to do this).  For this version of shortest job first, as processes arrive, they are added to the queue. If the burst time of the newest process in the queue is less than the remaining time to execute the current process, the current process should be added back to the queue and the new process should be executed. So in the batchfile above, process 1 and 3 arrive at the same time, but process 1 has a burst time of 20 seconds, so we run process 1. At time = 9, process 7 enters the queue. Process 1 has 11 seconds of execution remaining. Process 7 has a burst time of 4. Therefore, we will pause process 1, save its new burst time (which is the remaining time), and execute process 7. At time 10, process 2 enters the queue. The current process, PID 7, has 3 seconds remaining until full execution, while process 2 needs 12 seconds to fully execute. Therefore, we continue to execute PID 7 until it completes, and check the queue for the process with the shortest remaining burst time- in this case, we would run PID 1 until it is fully executed, then PID 2, then PID 3. This would complete the batch file's process scheduling algorithm. In summary, the basic algorithm. The basic algorithm can be summarized as:

At each time
Check what processes have arrived in the queue.
Compare the arrived process' burst time to the time that remains for the current process to fully execute.
If the newest process has a shorter burst time than the remaining time on the current process, update the burst time for the current process to be the remaining time. Then execute the new process with the shorter burst time.
Otherwise, continue executing the current process and decrement its remaining time.
If two processes arrive at the same time and have the same burst time, execute the process with the smaller PID first
The simplest way to check "at each time" is to sort all of the processes by arrival time, but there are a multitude of ways to simulate ShortestJobFirst. There are many different ways to update your process queue from the batch file. You can swap items in the batchFileData list. You can construct a dictionary object that tracks each process and the remaining burst time. You can simply update the burst time of a process each time you would have to pause the process.

Finally, print the PID values of the processes in the order that they will be executed by the algorithm, the average process waiting time, and average process turn around time. Using the example batchfile, the input would look like this

python3 batchSchedulingComparison.py batchfile.txt ShortestJobFirst

And the output  (FROM MAIN BASED ON YOUR RETURNED VALUES) would be:

PID ORDER OF EXECUTION:

1

7

1

2

3

Average Process Turnaround Time: 35.00

Average Process Wait Time: 13.5

 

PrioritySort(batchFileData)

Parameters: accepts all of the batchFileData from the batchfile opened in main

Returns: (1)a list (or other data structure) of the time each process is completed at, and (2) a list (or other data structure) containing the PID of the processes in the order the algorithm sorted them by.

If the command line argument states that the user wants to process batch jobs using Priority, then this function will be called. The data from the batchfile should be passed in and sorted by arrival (again, there are many ways to do this). The basic algorithm can be summarized as:

At each time
Check what processes are available for execution.
Compare the arrival times, and execute the process with the smallest arrival time.
If two or more processes have the same arrival time, consult each process' priority.
Of the processes that have the same arrival time, run the process with the lower priority value (lower priority value means higher priority, so priority 1 is always executed before priority 3).
If the processes have the same arrival time AND same priority value, execute from smallest to largest PID
This algorithm differs from ShortestJobFirst, because each process must fully execute before considering what processes are available in the queue.  Finally, print the PID values of the processes in the order that they will be executed by the algorithm, the average process waiting time, and average process turn around time. If you are performing an internet search, priority can be preemptive or non-preemptive. You should be creating a non-preemptive priority algorithm. Using the example batchfile, the input would look like this 

python3 batchSchedulingComparison.py batchfile.txt Priority

And the output (FROM MAIN BASED ON YOUR RETURNED VALUES)  would be:

 

PID ORDER OF EXECUTION:

3

1

7

2

 

Average Process Turnaround Time: 65.25

Average Process Wait Time: 43.75

 

Part 1 Requirements and Hints : 

Part 1 should be done in python3 (trust me, even with a learning curve, this is going to be way simpler in Python- I would prefer you have an understanding of the algorithms over an understanding of c syntax).
Note that the test batch file for grading will be different than the supplied batch file. Make sure you test a few different scenarios to ensure your algorithms are working right.
You do not need to actually create processes to implement these algorithms. You are simply deciding the order that processes would execute in, then outputting that, the average turnaround time, and the average wait time.
All file input and output should be performed in main. Nothing should be printed from the process sorting functions, or the averageWait or averageTurnaround functions.
The only thing in your zip or tar.gz should be your copy of batchSchedulingComparison.py
 

As part of your file header comment (Links to an external site.), compare and contrast the three algorithms. Be sure to explain where each would be appropriate to use, and any possible tradeoffs in implementation or process execution

 
