"""
---first thought (Sep.1 2022)---
    Simple Homework Timer
    need name of homework before timing
    press space to restart/pause timing
    could choose timer mode or stopwatch mode
    press tab to stop timing, save record ( in its folder), and cycle
    when open a new one and wait for name,
    input END to end today's homework,
    and see today's result.
------
    feature waiting to add:
        1. timer mode

"""

import time
import csv
from prettytable import PrettyTable
# from prettytable import from_csv
import os
import keyboard
import ctypes
# from termcolor import colored

pause_flag = 0
time_start_save = 0
time_stop_save = 0
length_sec = 0
if not os.path.exists("history.csv"):
    with open('history.csv', 'w', newline='') as history_file:
        csv.writer(history_file).writerow(["Date", "Task Name", "Start Time", "End Time", "Length"])
ctypes.windll.kernel32.SetConsoleTitleW("Simple Homework Timer")


def pause():
    global pause_flag
    pause_flag = pause_flag ^ 1


def timer(name):
    global time_start_save, time_stop_save, length_sec
    time_start = time.perf_counter()
    time_start_ref = time.time()
    time_start_save = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(name)
    while True:
        time.sleep(0.05)
#        os.system("cls")
        time_now = time.perf_counter()
        print("\r", int(10 * (time_now - time_start)) / 10, end="", sep="")
        if keyboard.is_pressed("space"):
            pause()
        global pause_flag
        if pause_flag:
            pause_flag = 0
            break
    length_sec = int(time.perf_counter() - time_start)
    time_stop_save = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_start_ref + length_sec))
    global history_file
    with open('history.csv', 'a', newline='') as history_file:
        csv.writer(history_file).writerow(
            [time.strftime("%Y-%m-%d", time.localtime()), name, time_start_save, time_stop_save, length_sec])


print("Hello, there! Today is " + time.strftime("%Y-%m-%d", time.localtime())
      + ".\nWhat would you like to do now?")
while True:
    choice = input("1. Start timing a new task.\n2. See today\'s timing history.\n")
    if choice == "1":
        while True:
            task_name = input("Please input the name of the task and press Enter.\n")
            timer(task_name)
            print("\nNotice: Task Saved! Start:%s Stop:%s Length:%s" % (time_start_save, time_stop_save, length_sec))
            cyc = input("If you want to continue doing another task, please press Enter. If not, you can close it.")
            if cyc != '':
                break
    else:
        if choice == "2":
            table = PrettyTable(["Date", "Task Name", "Start Time", "End Time", "Length"])
            with open("history.csv", "r") as fp:
                for row in csv.reader(fp):
                    if time.strftime("%Y-%m-%d", time.localtime()) in row:
                        table.add_row(row)
            print(table, "\n")
        else:
            break
