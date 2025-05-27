def getEven(numbers):
    evennumbers = []
    for num in numbers:
        if num % 2 == 0:
            evennumbers.append(num)
    return evennumbers
mynumbers = [12, 23, 54, 43, 57, 84, 73, 89, 91, 100]
evenlist = getEven(mynumbers)

print("Input list:", mynumbers)
print("Even numbers:", evenlist)
