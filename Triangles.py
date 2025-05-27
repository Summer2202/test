def triangle(t1, t2, t3):
    sides = [t1, t2, t3]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
        print("This is a triangle :）")
    else:
        print("This is not a triangle ：（")
triangle(5, 6, 5)  
triangle(2, 23, 15) 
