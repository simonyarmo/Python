# File: Benford.py
# Student: Simon Yarmowich
# UT EID: sy22637
# Course Name: CS303E
# 
# Date: 11/03/2023
# Description of Program: The program runs through an inputed file with years seperated with "&". It finds the last instance of "&" and stores the number that follows it in a set. It then sees what the first digit is of that number and increments a count of what number it is in a dictionary. The program then writes the total count and percentage of numbers that started with a specific digit.


import os.path

def benford(f1):

    if not os.path.isfile(f1):
        print("File does not exist")
        return
    file = open(f1,"r")
    s1 = set()
    dic = {"1":0, "2":0, "3":0,"4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    count =0
    for line in file:
        if "#" in line:
            continue
        else:
            count+=1
            index= line.rfind("&")
            number = line[index+1:]
            number.replace("\n","")
            s1.add(int(number))
            dic[str(line[index+1])] = dic[str(line[index+1])] +1
    file.close()
    print("Output written to benford.txt")
    size = len(s1)
    total = 0

    for key in dic:
        total = total + dic[key]
    file = open("benford.txt", "w")
    file.write("Total number of counties: "+ str(count)+"\n")
    file.write("Unique population counts: "+ str(size)+ "\n")
    file.write("First digit frequency distributions:\n")
    file.write("Digit    Count    Percentage\n")

    for key in range(1,10):
        newCount =str(dic[str(key)])
        percentage = float(dic[str(key)])*100/count
        percentage = format(percentage, '.2f')
        file.write(str(key)+"        "+newCount+"      "+str(percentage)+"\n")

    
    pass

f1 = str(input("Source filename: ").strip())
benford(f1)
