#!/usr/bin/env python3

# File: numlist.py
# Date: 2022-11-20

# Get input of numbers into a list until user enters -1 then print all numbers.

print("Welcome\n")

nums = [] #init nums list

go = True #init loop to on

while go == True: #start loop
    mispar = input("Enter integer to add to list, -1 to quit: ") #prompt
    mispar = int(mispar) #change to int

    if mispar == -1:
        go = False #toggle exit
    elif mispar != -1:
        nums.append(mispar) #add mispar to nums list

print(f"\n{nums}") #print list
print("\nClosing") #end
