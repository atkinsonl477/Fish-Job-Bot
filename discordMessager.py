#!/usr/bin/env python3
from scheduleReader import firstCallList, monthOfDay, dayOfDay
from excelReader import mondayJob, tuesdayJob, wednesdayJob, thursdayJob, fridayJob, Jobs
from time import sleep
from datetime import datetime, time
import requests
from collections import namedtuple


#helpful user variables that can be changed as needed
discPings = {'Person1': '<@DISCORD_ID_HERE>',
             'Person2': '<@DISCORD_ID_HERE>',
             'Person3': '<@DISCORD_ID_HERE>',
             'Person4': '<@DISCORD_ID_HERE>',
             'Botello': '<@DISCORD_ID_HERE>',
             'Bryson': '<@DISCORD_ID_HERE>',
             'Henderson': '<@DISCORD_ID_HERE>',
             'Higgins': '<@DISCORD_ID_HERE>',
             'Hryhorchuk': '<@DISCORD_ID_HERE>',
             'Morin': '<@DISCORD_ID_HERE>',
             'Nishiyama': '<@DISCORD_ID_HERE>',
             'Ridge': '<@DISCORD_ID_HERE>',
             'Robinson': '<@DISCORD_ID_HERE>',
             'Seargeant': '<@DISCORD_ID_HERE>',
             'Sechrist': '<@DISCORD_ID_HERE>',
             'Mattei': '<@DISCORD_ID_HERE>',
             'Ibarra': '<@DISCORD_ID_HERE>',
             'Hao': '<@DISCORD_ID_HERE>',
             'Renard': '<@DISCORD_ID_HERE>'
    }

#collection of job variables
job = namedtuple('job', ['title', 'jobIndex'])

mornWhistle = job('Morning Whistle Jock', 0)
lysol = job('Lysol Fish', 2)
sweep = job('Sweeper Fish', 1)
sod = job('Sergeant of day fish', 3)
afterWhistle = job('Afternoon Activities Whistle Jock', 4)
formoWhistle = job('Foramtion Whistle Jock', -1)

mNotifHour = 5
mNotifMinute = 0
eNotifHour = 20
eNotifMinute = 26

#jobs we have for the day
mondayJobs = [mornWhistle, sweep,  lysol,  sod, afterWhistle, formoWhistle]
tuesdayJobs = [mornWhistle, sweep,  lysol,  sod, formoWhistle]
wednesdayJobs = [mornWhistle, sweep,  lysol,  sod]
thursdayJobs = [mornWhistle, sweep,  lysol,  sod, formoWhistle]
fridayJobs = [mornWhistle, sweep,  lysol,  sod, afterWhistle]

weeklyJobs = [mondayJobs, tuesdayJobs, wednesdayJobs, thursdayJobs, fridayJobs]

#url to use for different channels
testUrl = '' # INPUT DISCORD WEBHOOK HERE
mainUrl = '' # INPUT DISCORD WEBHOOK HERE
newUrl = '' # INPUT DISCORD WEBHOOK HERE


url = newUrl


def firstcall(activity, whistle_jock, uniform):
    message = discPings[whistle_jock] + ' 30 minutes until first call for ' + activity + ', whistle jock is ' + whistle_jock + ', uniform is ' + uniform
    r = requests.post(url, data={"content": message})
def sendMessage(message):
    r = requests.post(url, data={"content": message})


def mornCheck(date, Jobs, index):
    print(date, 'Sending morning reminders for Fish Jobs')
    message = 'Wakey wakey! It\'s time for PT! Here is the morning announcement for fish Jobs. Make sure you have the items necessary when it is your time to shine. \n'
    sendMessage(message)
    message = ''
    for thing in weeklyJobs[index]:
        print(f'{thing.title} for today is: {Jobs[thing.jobIndex][weekIndex]}')
        message += (thing.title + ' for today is: ' + Jobs[thing.jobIndex][weekIndex] + ' ' + discPings[Jobs[thing.jobIndex][weekIndex]] + '\n')
    sendMessage(message)
    morningPrint[index] = True

def evenCheck(date, Jobs, index):
    print(date, 'Sending evening reminders for Fish Jobs tomorrow')
    message = 'Nightly reminder that you\'re loved :) \nAlso, fish jobs for tomorrow:'
    sendMessage(message)
    message = ''
    print(Jobs)
    for thing in weeklyJobs[index]:
        print(f'{thing.title} for tomorrow is: {Jobs[thing.jobIndex][weekIndex]}')
        message += (thing.title + ' for tomorrow is: ' + Jobs[thing.jobIndex][weekIndex] + ' ' + discPings[Jobs[thing.jobIndex][weekIndex]] + '\n')
    sendMessage(message)
    evenPrint[index] = True

#TimedMessage removes the need for multiple copy pastes considering I may need to implement more than just evening and morning messages. Returns true or false
def timedMessage(index, timeOfMessage):
    if timeOfMessage == 'Morning':
        Hour = mNotifHour
        Minute = mNotifMinute
        if todaysDate.hour == Hour and todaysDate.minute == Minute:
               mornCheck(todaysDate.day, Jobs[index], index)
               return True
    elif timeOfMessage == 'Evening':
        Hour = eNotifHour
        Minute = eNotifMinute
        if todaysDate.hour == Hour and todaysDate.minute == Minute:
               evenCheck(todaysDate.day, Jobs[index + 1], index + 1)
               return True
    
    #BRASS THING TO GET RID OF LATER
    '''
    elif timeOfMessage == 'Brass':
        Hour = brassHour
        Minute = brassMinute
        if todaysDate.hour == Hour and todaysDate.minute == Minute:
            print('brass message sent')
            sendMessage('Day ' + str(todaysDate.day + 1) + ' is basically over, AAAAAAAAAAAAAAAAAAAAA')   
            return True
    return False
    '''


#fish job specific
def rotationPick():
    rotation = input('Enter which week we are in (a/b/c): ').lower()
        
    if rotation == 'a':
        return 0
    elif rotation == 'b':
        return 1
    elif rotation == 'c':
        return 2
    else:
        print('invalid answer, try again')
        return rotationPick()
weekIndex = rotationPick()





#TESTING ZONE, PUT ALL CODE THAT YOU WOULD NORMALLY PUT IN THE WHILE LOOP RIGHT HERE


'''
try:
    
    firstcall('formation', 'me', 'something sexy')
except:
    print('You have no internet connection')
'''


for obj in firstCallList:
    print(obj.activity)





morningPrint = [False, False, False, False, False]
evenPrint = [False, False, False, False, False]
fcPassed = False
firstCallPassed = 0
while True:
    
    
    
    
    todaysDate = datetime.today()
    todaysDate = datetime(todaysDate.year, todaysDate.month, todaysDate.day, todaysDate.hour, todaysDate.minute, 0)
    
    
    
    '''
    #Ends program if time has already passed, disable when testing
    if todaysDate.month > monthOfDay[4] or (todaysDate.month == monthOfDay[4] and todaysDate.day > dayOfDay[4]):
        print('this week has already passed, ending program')
        break
    '''
    
    
    
   
    
    
    '''
    
    
    #first call notification
    if firstCallPassed < len(firstCallList):
        nextFirstCall = datetime(todaysDate.year, firstCallList[firstCallPassed].month, firstCallList[firstCallPassed].day, firstCallList[firstCallPassed].hour, firstCallList[firstCallPassed].minute, 0)
        nextFirstCallTime = time(firstCallList[firstCallPassed].hour, firstCallList[firstCallPassed].minute, 0)
        
        
        
        if nextFirstCall < todaysDate:
            print(f'{firstCallList[firstCallPassed].activity} on {nextFirstCall.month}/{nextFirstCall.day} has already passed')
            firstCallPassed += 1
        else:
            #we can assure that the next first call has not passed in this else statement, in the event that the program has to restart
            if nextFirstCall == todaysDate:
                print(f'{nextFirstCall} first call is 30 minutes away! Sending discord ping')
                
                hour = firstCallList[firstCallPassed].hour
                print(hour)
                #determines what activity first call is for
                
                messOfArrays = [mondayJob, tuesdayJob, wednesdayJob, thursdayJob, fridayJob]
                
                if todaysDate.month == monthOfDay[0] and todaysDate.day == dayOfDay[0]:
                    messIndex = 0
                elif todaysDate.month == monthOfDay[1] and todaysDate.day == dayOfDay[1]:
                    messIndex = 1
                elif todaysDate.month == monthOfDay[2] and todaysDate.day == dayOfDay[2]:
                    messIndex = 2
                elif todaysDate.month == monthOfDay[3] and todaysDate.day == dayOfDay[3]:
                    messIndex = 3
                elif todaysDate.month == monthOfDay[4] and todaysDate.day == dayOfDay[4]:
                    messIndex = 4
                else:
                    print('You did something wrong')
                messIndex = 4
                print(messIndex)
                if hour < 12:
                    #assume its morning training time
                    whistleJock = messOfArrays[messIndex][mornWhistle.jobIndex][weekIndex]
                    print(whistleJock, 'is whistle jock for this activity')
                elif messIndex == 1 or messIndex == 3:
                    whistleJock = messOfArrays[messIndex][formoWhistle.jobIndex][weekIndex]
                    print(whistleJock, 'is whistle jock for this activity')
                elif messIndex == 4:
                    whistleJock = messOfArrays[messIndex][afterWhistle.jobIndex][weekIndex]
                    print(whistleJock, 'is whistle jock for this activity')
                elif messIndex == 0:
                    if firstCallList[firstCallPassed].hour == 16:
                        whistleJock = messOfArrays[messIndex][afterWhistle.jobIndex][weekIndex]
                        print(whistleJock, 'is whistle jock for this activity')
                    else:
                        whistleJock = messOfArrays[messIndex][formoWhistle.jobIndex][weekIndex]
                        print(whistleJock, 'is whistle jock for this activity')
                #code I need to add here
                
                
                
                
                firstCallPassed += 1
            else:
                pass
        
    elif not fcPassed:
        print('All activities that involve first call have passed for this week')
        fcPassed = True
    
    '''
                
                
                
    
    
    
    
    for i in range(5):
        if todaysDate.month == monthOfDay[i] and todaysDate.day == dayOfDay[i]:
            if not morningPrint[i]:
                morningPrint[i] = timedMessage(i, 'Morning')
            if not evenPrint[i]:
                evenPrint[i] = timedMessage(i, 'Evening')
            
    
    sleep(1)
    
    # monday (depricated)
    '''
    if todaysDate.month == monthOfDay[0] and todaysDate.day == dayOfDay[0]:
        if not morningPrint[0]:
            morningPrint[0] = timedMessage(0, 'Morning')
        if not eveningPrint[0]:
            eveningPrint[0] = timedMessage(0, 'Evening')
            
            
        if todaysDate.hour == mNotifHour and todaysDate.minute == mNotifMinute and not morningPrint[0]:
           mornCheck(todaysDate.day, mondayJobs, 0)
        if todaysDate.hour == eNotifHour and todaysDate.minute == eNotifMinute and not evenPrint[0]:
           evenCheck(todaysDate.day, tuesdayJobs, 0)
           
    
    
    #tuesday
    elif todaysDate.month == monthOfDay[1] and todaysDate.day == dayOfDay[1]:
        if todaysDate.hour == mNotifHour and todaysDate.minute == mNotifMinute and not morningPrint[1]:
            mornCheck(todaysDate.day, tuesdayJobs, 1)
        if todaysDate.hour == eNotifHour and todaysDate.minute == eNotifMinute and not evenPrint[1]:
            evenCheck(todaysDate.day, wednesdayJobs, 1)
    
    
    #wednesday
    elif todaysDate.month == monthOfDay[2] and todaysDate.day == dayOfDay[2]:
        if todaysDate.hour == mNotifHour and todaysDate.minute == mNotifMinute and not morningPrint[2]:
            mornCheck(todaysDate.day, wednesdayJobs, 2)
        if todaysDate.hour == eNotifHour and todaysDate.minute == eNotifMinute and not evenPrint[2]:
            evenCheck(todaysDate.day, thursdayJobs, 2)
    
    #thursday
    elif todaysDate.month == monthOfDay[3] and todaysDate.day == dayOfDay[3]:
        if todaysDate.hour == mNotifHour and todaysDate.minute == mNotifMinute and not morningPrint[3]:
            mornCheck(todaysDate.day, thursdayJobs, 3)
        if todaysDate.hour == eNotifHour and todaysDate.minute == eNotifMinute and not evenPrint[3]:
            evenCheck(todaysDate.day, fridayJobs, 3)
    
    #friday
    elif todaysDate.month == monthOfDay[4] and todaysDate.day == dayOfDay[4]:
        if todaysDate.hour == mNotifHour and todaysDate.minute == mNotifMinute and not morningPrint[4]:
            mornCheck(todaysDate.day, fridayJobs, 4)
        '''
            
            
