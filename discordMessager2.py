
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

mNotifHour = 4
mNotifMinute = 50
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


url = testUrl


def sendMessage(message):
    r = requests.post(url, data={"content": message})


def mornCheck(date, Jobs, index):
    print(date, 'Sending morning reminders for Fish Jobs for ', weekDays[i])
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


weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

morningPrint = [False, False, False, False, False]
evenPrint = [False, False, False, False, False]

notSaturday = True

while True:
    
    
    # 0 - Monday, 6 - Sunday
    todaysDate = datetime.today()
    todaysDate = datetime(todaysDate.year, todaysDate.month, todaysDate.day, todaysDate.hour, todaysDate.minute, 0)
    
    dayOfWeek = todaysDate.weekday()
    
    
    
    
    

    
    



    for i in range(5):
        #morning check
        if not morningPrint[i] and dayOfWeek == i:
            morningPrint[i] = timedMessage(i, 'Morning')
        if i != 4 and not evenPrint[i] and dayOfWeek == i:
            evenPrint[i] = timedMessage(i, 'Evening')
            
    # If its saturday reset the printed boolean
    
    if dayOfWeek == 5 and notSaturday:
        morningPrint = [False, False, False, False, False]
        evenPrint = [False, False, False, False, False]
        weekIndex = (weekIndex + 1) % 3
        notSaturday = False
    
    
    
    # Sunday Evening Check
    if dayOfWeek == 6:
        notSaturday = True
        if not evenPrint[4]:
            evenPrint[4] = timedMessage(-1, 'Evening')

    sleep(1)
