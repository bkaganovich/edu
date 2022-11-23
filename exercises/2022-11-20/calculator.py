#!/usr/bin/env python3

# File: calculator.py
# Date: 2022-11-20

# Two-number four-operation calculator.

# Prompt for two numbers.
# Display operations: + = 1, - = 2, * = 3, / = 4
# Prompt for operation.
# Print operation result.

nums = [] #init nums list

print("Calculator\n") #greet
print("Enter two numbers, then choose operation.\n") #start

for i in range(2): #two numbers
    nums.append(float(input(f"Enter number[{i}]: "))) #prompt append

#display operations
print("\nFor addition + enter 1")
print("For subtraction - enter 2")
print("For multiplication * enter 3")
print("For division / enter 4")

op = int(input("\nEnter operation: ")) #prompt for operation

def output(op, result): #operation display function
    print(f"\n{nums[0]} {op} {nums[1]} = {result}") #first _ second = result

match op:
    case 1: #addition +
        result = sum(nums)
        output("+", result)
    case 2: #subtraction -
        result = nums[0]-nums[1]
        output("-", result)
    case 3: #multiplication *
        result = nums[0]*nums[1]
        output("*", result)
    case 4: #division /
        result = nums[0]/nums[1]
        output("/", result)
    case other:
        print("Invalid operation")

print("\nClosing") #end
