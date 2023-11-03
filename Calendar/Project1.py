
# File: Project1.py
# Student: Simon Yarmowich 
# UT EID: sy22637
# Course Name: CS303E
# 
# Date Created:Oct 9 2023
# Description of Program: The program takes the month as an integer [1-12] and then prints out the 2024 calendar. 


def monthName( n ):
   # Given the number of a month, return its name.
   # Example, if n == JAN, return "January"
   if(JAN<= n<=DEC):
        if(n ==JAN):
           return "January"
        if(n ==FEB):
           return "Febuary"
        if(n ==MAR):
           return "March"
        if(n ==APR):
           return "April"
        if(n ==MAY):
           return "May"
        if(n ==JUN):
           return "June"
        if(n ==JUL):
           return "July"
        if(n ==AUG):
           return "August"
        if(n ==SEP):
           return "September"
        if(n ==OCT):
           return "October"
        if(n ==NOV):
           return "November"
        if(n ==DEC):
           return "December"
        

def firstDayOfMonth( n ):
    if(n ==JAN):
        return monday
    if(n ==FEB):
        return thursday
    if(n ==MAR):
       return friday
    if(n ==APR):
       return monday
    if(n ==MAY):
       return wednesday
    if(n ==JUN):
       return monday
    if(n ==JUL):
         return monday
    if(n ==AUG):
        return thursday
    if(n ==SEP):
        return sunday
    if(n ==OCT):
        return tuesday
    if(n ==NOV):
        return friday
    if(n ==DEC):
        return sunday 

def daysInMonth2024( n ):
    if(n ==JAN):
        return 31
    if(n ==FEB):
        return 29
    if(n ==MAR):
       return 31
    if(n ==APR):
       return 30
    if(n ==MAY):
       return 31
    if(n ==JUN):
       return 30
    if(n ==JUL):
         return 31
    if(n ==AUG):
        return 31
    if(n ==SEP):
        return 30
    if(n ==OCT):
        return 31
    if(n ==NOV):
        return 29
    if(n ==DEC):
        return 31

def printCalendar(name, first, num):
    count =0
    space = (20-len(name)-4)//2
    for x in range(space):
        print(" ", end = '')
    print(name+ " 2024")
    print("Su Mo Tu We Th Fr Sa")
    gap = first *3-1
    for x in range(gap+2):
        count= first
        print(" ", end='')
    for x in range(1,num+1):
        if x <10:
           print(x, end = '  ')
        else:
           print(x, end=' ')
        count+=1
        if count==7:
            print("")
            count=0
    
sunday=0
monday =1
tuesday =2
wednesday =3
thursday =4
friday=5
saturday =6
JAN =1
FEB=2
MAR=3
APR = 4
MAY= 5
JUN=6
JUL=7
AUG=8
SEP=9
OCT=10
NOV=11
DEC =12
check = True
while check:
    month = int(input("Enter the number of a month [1..12]: "))
    if(JAN<=month<=DEC):
        check = False
    else:
        print("Month must be between 1 and 12. Try again!")
month_name = monthName(month)
day = firstDayOfMonth(month)
numOfDays = daysInMonth2024(month)
print("")
printCalendar(month_name, day, numOfDays)
print("\n")








