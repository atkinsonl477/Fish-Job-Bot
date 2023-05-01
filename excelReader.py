
from openpyxl import load_workbook


workbook = load_workbook(filename="FISH SHEET.xlsx")

sheet = workbook['pyRead']



#It is necessary we have a function that converts the character value to the letter in excel/ i.e. [ = AA. Also, there is totally 26 letters in the alphabet!!!
def excelCharConv(num):
    if num >= 26:
        
        
        secondChar = chr((num % 26) + 65)
        return str(excelCharConv(num // 26 - 1) + '' + secondChar)
        
    else:
        return str(chr(65 + num))

numOfM = 6
numOfT = 5
numOfW = 4
numOfR = 5
numOfF = 5



#Monday Pass

mondayJob = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
numChar = 65


for x in range(numOfM):
    numChar += 1
    letter = excelCharConv(numChar - 65)
    number = 2
    for y in range(3):
        number += 1
         
        
        mondayJob[x][y] = sheet[letter + str(number)].value



#Tuesday Pass

tuesdayJob = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
numChar = 65 + numOfM


for x in range(5):
    numChar += 1
    letter = excelCharConv(numChar - 65)
    number = 2
    for y in range(3):
        number += 1
        
        
        tuesdayJob[x][y] = sheet[letter + str(number)].value
    
    
    
#Wednesday Pass

wednesdayJob = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
numChar = 65 + numOfM + numOfT


for x in range(numOfW):
    
        
    numChar += 1
    letter = excelCharConv(numChar - 65)
    number = 2
    for y in range(3):
        number += 1
            
        
        wednesdayJob[x][y] = sheet[letter + str(number)].value
    



#Thursday Pass

thursdayJob = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
numChar = 65 + numOfM + numOfT + numOfW

for x in range(5):
    numChar += 1
    letter = excelCharConv(numChar - 65)
    number = 2
    for y in range(3):
        number += 1
        
        
        thursdayJob[x][y] = sheet[letter + str(number)].value
    
    
    
#Friday Pass

fridayJob = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
numChar = 65 + numOfM + numOfT + numOfW + numOfR


for x in range(5):
    numChar += 1
    letter = excelCharConv(numChar - 65)
    number = 2
    for y in range(3):
        number += 1
       
        
        fridayJob[x][y] = sheet[letter + str(number)].value




Jobs = [mondayJob, tuesdayJob, wednesdayJob, thursdayJob, fridayJob]

    
    
    