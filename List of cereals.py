cerealsList = []
while True:
    food=input("Enter Cereal: ").strip().lower()
    if food in ['sultana', 'bran', 'weetbix']:
        break
    else:
        cerealsList.append(food)
print(cerealsList)
