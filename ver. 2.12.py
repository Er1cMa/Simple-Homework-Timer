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

stop_flag = 0
if not os.path.exists("history.csv"):
    with open('history.csv', 'w', newline='') as history_file:
        csv.writer(history_file).writerow(["Date", "Task Name", "Start Time", "End Time", "Length"])
ctypes.windll.kernel32.SetConsoleTitleW("Simple Homework Timer")

print("Hello, there! Today is " + time.strftime("%Y-%m-%d", time.localtime())
      + ".\nWhat would you like to do now?")
while True:
    choice = input("1. Start timing a new task.\n2. See today\'s timing history.\n")
    if choice == "1":
        while True:
            task_name = input("Please input the name of the task and press \"Enter\".\n")
            time_start_ref = time.time()
            time_start_save = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            time_count = 0
            os.system("cls")
            print(task_name)
            ctypes.windll.kernel32.SetConsoleTitleW("Simple Homework Timer")
            while True:
                time.sleep(0.1)
                time_count += 0.1
                time_display_value = int(10 * time_count) / 10
                if time_display_value / 3600 < 10:
                    time_h = "0" + str(int(time_display_value / 3600))
                else:
                    time_h = str(int(time_display_value / 3600))
                if time_display_value % 3600 / 60 < 10:
                    time_m = "0" + str(int(time_display_value % 3600 / 60))
                else:
                    time_m = str(int(time_display_value % 3600 / 60))
                if time_display_value % 60 < 10:
                    time_s = "0" + str(int(time_display_value) % 60)
                else:
                    time_s = str(int(time_display_value) % 60)
                time_z = str(int(10 * (time_display_value - int(time_display_value))))

                time_list = [time_h, ':',
                             time_m, ':',
                             time_s, '.',
                             time_z]
                cache = ''
                time_display = cache.join(time_list)
                # os.system("cls")
                print("\r", time_display, end="", sep="")
                if keyboard.is_pressed(41):  # `
                    os.system("cls")
                    print("\rPausing...\nTime:%s \nPress \"F8\" to stop, or \"`\" to restart." % time_display)
                    ctypes.windll.kernel32.SetConsoleTitleW("[Pausing: %s] Simple Homework Timer" % time_display)
                    # print("......Pausing for 0.5 second to avoid multi recognizing.......", end="", sep="")
                    time.sleep(0.5)
                    while True:
                        time.sleep(0.1)
                        if keyboard.is_pressed(66):  # F8
                            stop_flag = 1
                            # print("......Pausing for 0.5 second to avoid multi recognizing.......", end="", sep="")
                            time.sleep(0.5)
                            break
                        if keyboard.is_pressed(41):  # `
                            os.system("cls")
                            ctypes.windll.kernel32.SetConsoleTitleW("Simple Homework Timer")
                            # print("......Pausing for 0.5 second to avoid multi recognizing.......", end="", sep="")
                            time.sleep(0.5)
                            break
                if stop_flag:
                    stop_flag = 0
                    ctypes.windll.kernel32.SetConsoleTitleW("Simple Homework Timer")
                    break
            length_sec = int(time_count)
            time_stop_save = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            with open('history.csv', 'a', newline='') as history_file:
                csv.writer(history_file).writerow(
                    [time.strftime("%Y-%m-%d", time.localtime()),
                     task_name, time_start_save, time_stop_save, length_sec])
            print("\nNotice: Task Saved! Start:%s Stop:%s Length:%s" % (time_start_save, time_stop_save, length_sec))
            print("Auto restart in 10 seconds...")
            time.sleep(10)
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
