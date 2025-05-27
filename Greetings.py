def morning(name):
    print(f"Good morning {name}! How's your day?")

def afternoon(name):
    print(f"Good afternoon {name}! How's your day?")

def evening(name):
    print(f"Good evening {name}! How's your day?")
def greeting():
    name = input("Enter your name: ")
    time = int(input("Enter a time(number from 0 to 23): "))
    
    if 0 <= time <= 12:
        morning(name)
    elif 13 <= time <= 17:
        afternoon(name)
    elif 18 <= time <= 23:
        evening(name)
greeting()
