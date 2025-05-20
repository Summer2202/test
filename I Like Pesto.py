iLikePesto = []
otherfoods = []
for _ in range(8):
    food = input("What's your favourite food? ").strip().lower()
    if food == 'pesto':
        iLikePesto.append(food)
    else:
        otherfoods.append(food)
print(f"Pesto is loved by {len(iLikePesto)} people!")
for _ in range(len(iLikePesto)):
    print("I like pesto")
print("\nOther Foods:")
for food in otherfoods:
    print(food)
