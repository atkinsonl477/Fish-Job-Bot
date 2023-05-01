#!/usr/bin/env python3
from collections import namedtuple

with open('schedule.txt') as f:
    lines = f.readlines()
    
numINeed = 0
schedule = []
for i in range(len(lines)):
    
    
    schedule.append(lines[i+numINeed][:-1])
        
        
    if lines[i+numINeed] == '2230 - L/O\n':
            
        numINeed += 2
            


mondaySchedule = []
index = 0
while schedule[index][0:len('Tuesday')] != 'Tuesday':
    
    mondaySchedule.append(schedule[index])
    index += 1
mondayDate = [mondaySchedule]
#its choosday innit

tuesdaySchedule = []
while schedule[index][0:len('Wednesday')] != 'Wednesday':
    
    tuesdaySchedule.append(schedule[index])
    index += 1


#it is wednesday my dudes

wednesdaySchedule = []
while schedule[index][0:len('Thursday')] != 'Thursday':
    
    wednesdaySchedule.append(schedule[index])
    index += 1


#thursday pass

thursdaySchedule = []
while schedule[index][0:len('Friday')] != 'Friday':
    
    thursdaySchedule.append(schedule[index])
    index += 1


#friday pass

fridaySchedule = []
remainingItems = True
while remainingItems:
    try:
        
        fridaySchedule.append(schedule[index])
        index += 1
    except:
        remainingItems = False



#interpreting the schedule and knowing the important stuff

def dateToInts(string):
    print(string, 'aaaaaa')
    if string[0] == ' ':
        month = int(string[1])
    else:
        month = int(string[0:2])
    if string[-3] == '/':
        day = int(string[3:5])
    else:
        day = int(string[3])
    return day, month
        
def thirtyMinutesBefore(hour, minute):
    minute -= 30
    if minute < 0:
        minute += 60
        hour -= 1
    return [hour, minute, 0]

monthOfDay = []
dayOfDay = []
i = 0


for schedule in [mondaySchedule, tuesdaySchedule, wednesdaySchedule, thursdaySchedule, fridaySchedule]:
    for i, s in enumerate(schedule[0]):
        if s == '/':
            dashIndex = i
        
    d, m = dateToInts(schedule[0][dashIndex-2:dashIndex + 3])
    monthOfDay.append(m)
    dayOfDay.append(d)


FC = namedtuple('FC', ['activity', 'hour', 'minute', 'uniform', 'day', 'month'])
firstCallList = []
for x, sched in enumerate([mondaySchedule, tuesdaySchedule, wednesdaySchedule, thursdaySchedule, fridaySchedule]):
    for i, part in enumerate(sched):
        sched[i] = part[0:-1]
        if part[7:9] == 'FC':
            arr = thirtyMinutesBefore(int(part[0:2]), int(part[2:4]))
            if part[-2] != ')':
                part = part[0:-1] + ' (OPTG/WOPTG/Class b, idk im too lazy to find out)'
            
            
            try:
                if sched[i + 2][7:(7 + len('formation'))] == 'Formation' or sched[i + 3][7:(7 + len('formation'))] == 'Formation' or sched[i + 2][7:(7 + len('Morning Formation'))] == 'Morning Formation':
                    print('there is a formation here \n')
                    firstCallList.append(FC('Formation', arr[0], arr[1], part[10:-1], dayOfDay[x], monthOfDay[x]))
                    
                else:
                    if sched[i + 1][7:9] == 'AC':
                        
                        firstCallList.append(FC(sched[i + 2][7:len(sched[i + 2]) - 1], arr[0], arr[1], part[10:-1], dayOfDay[x], monthOfDay[x]))
                    else:
                        firstCallList.append(FC(sched[i + 1][7:len(sched[i + 1]) - 1], arr[0], arr[1], part[10:-1], dayOfDay[x], monthOfDay[x]))
            except:
               
                if sched[i + 1][7:9] == 'AC':
                    
                    firstCallList.append(FC(sched[i + 2][7:len(sched[i + 2]) - 1], arr[0], arr[1], part[10:-1], dayOfDay[x], monthOfDay[x]))
                else:
                    firstCallList.append(FC(sched[i + 1][7:len(sched[i + 1]) - 1], arr[0], arr[1], part[10:-1], dayOfDay[x], monthOfDay[x]))
        print(part)
    
    


firstCallList.append(FC('Something', 14, 16, 'Bravos', 11, 10))
