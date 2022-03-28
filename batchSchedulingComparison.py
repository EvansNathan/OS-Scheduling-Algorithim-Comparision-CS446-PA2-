# Author: Nathan Evans
# Date: 28 Mar 2022
# Purpose: Compares different OS scheduling algorithm

import sys


class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = int(arrival_time)
        self.burst_time = int(burst_time)
        self.priority = priority
        self.original_burst_time = int(burst_time)
        self.time_completed = 0
        self.turnaround_time = 0
        self.wait_time = 0
        self.already_ran = False


def sort_by_arrival(process):
    return process.arrival_time


def sort_by_burst(process):
    return process.burst_time


def sort_by_priority(process):
    return process.priority


def first_come_first_served_sort(process_list):
    print("First Come First Served Sort")

    sorted_process_list = sorted(process_list, key=sort_by_arrival)
    time = 0
    for process in sorted_process_list:
        if time < process.arrival_time:
            time = process.arrival_time

        time = time + process.burst_time
        process.time_completed = time

    return sorted_process_list


def shortest_job_first_sort(process_list, sjf_run_order):
    print("Shortest Job First Sort")

    process_ran = 0
    time = 0
    i = 0
    sorted_process_list = sorted(process_list, key=sort_by_arrival)
    last_process_ticked = Process(0, 0, 0, 0)

    while process_ran < len(sorted_process_list):
        next_process = -1
        for process in sorted_process_list:
            if process.arrival_time <= time and not process.already_ran:
                if next_process == -1:
                    next_process = i
                elif sorted_process_list[next_process].burst_time > process.burst_time:
                    next_process = i
            i = i + 1

        i = 0
        time = time + 1
        sorted_process_list[next_process].burst_time = sorted_process_list[next_process].burst_time - 1
        if sorted_process_list[next_process] != last_process_ticked:
            sjf_run_order.append(sorted_process_list[next_process])
            last_process_ticked = sorted_process_list[next_process]
        if sorted_process_list[next_process].burst_time == 0:
            sorted_process_list[next_process].time_completed = time
            sorted_process_list[next_process].already_ran = True
            process_ran = process_ran + 1

    return sorted_process_list


def priority_sort(process_list):
    print("Priority Sort")
    priority_process_list = []

    sorted_process_list = sorted(process_list, key=sort_by_arrival)
    time = 0
    processes_ran = 0
    i = 0

    while processes_ran < len(sorted_process_list):
        next_process = -1
        for process in sorted_process_list:
            if process.arrival_time <= time and not process.already_ran:
                if next_process == -1:
                    next_process = i
                elif sorted_process_list[next_process].priority > process.priority:
                    next_process = i

            i = i + 1

        sorted_process_list[next_process].already_ran = True
        time = time + sorted_process_list[next_process].burst_time
        sorted_process_list[next_process].time_completed = time
        priority_process_list.append(sorted_process_list[next_process])
        processes_ran = processes_ran + 1
        i = 0

    return priority_process_list


def average_turnaround(sorted_process_list):
    total_turnaround_time = 0
    for process in sorted_process_list:
        process.turnaround_time = process.time_completed - process.arrival_time
        total_turnaround_time = process.turnaround_time + total_turnaround_time

    average_turnaround_time = float(total_turnaround_time) / len(sorted_process_list)
    return average_turnaround_time


def average_wait(sorted_process_list):
    total_wait_time = 0
    for process in sorted_process_list:
        process.wait_time = process.turnaround_time - process.original_burst_time
        total_wait_time = total_wait_time + process.wait_time

    average_wait_time = float(total_wait_time) / len(sorted_process_list)
    return average_wait_time


def main():
    n = len(sys.argv)

    if n != 3:
        print ("Incorrect format, please provide 3 arguments")
        quit()

    sort_type = sys.argv[2]
    average_turnaround_time = 0
    average_wait_time = 0
    process_list = []
    sjf_run_order = []

    try:
        with open(sys.argv[1]) as in_file:
            for line in in_file:
                process_values = line.split(", ")
                process_list.append(Process(process_values[0], process_values[1], process_values[2], process_values[3]))
    except Exception:
        print("File Not Found. Try Again")
        quit()

    if sort_type == "FCFS":
        sorted_process_list = first_come_first_served_sort(process_list)
        average_turnaround_time = average_turnaround(sorted_process_list)
        average_wait_time = average_wait(sorted_process_list)
    elif sort_type == "ShortestFirst":
        sorted_process_list = shortest_job_first_sort(process_list, sjf_run_order)
        average_turnaround_time = average_turnaround(sorted_process_list)
        average_wait_time = average_wait(sorted_process_list)
    elif sort_type == "Priority":
        sorted_process_list = priority_sort(process_list)
        average_turnaround_time = average_turnaround(sorted_process_list)
        average_wait_time = average_wait(sorted_process_list)
    else:
        print ("Please select a valid sort type 'FCFS' 'ShortestFirst' 'Priority'")
        quit()

    if sort_type == "ShortestFirst":
        print("PID ORDER OF EXECUTION")
        for process in sjf_run_order:
            print(process.process_id)
    print("Average Turnaround Time: " + str(average_turnaround_time))
    print("Average Wait Time: " + str(average_wait_time))


if __name__ == "__main__":
    main()
