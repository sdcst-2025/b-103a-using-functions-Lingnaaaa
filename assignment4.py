def isPythagoreanTriple(a,b,c):
    sides= sorted ([a,b,c]) # smallest to largest
    x,y,z=sides
    print(f"The hypotenuse is {z}")
    if x**2 + y**2 != z**2:
        return False
    return True

if isPythagoreanTriple(5,3,4):
    print(f"They are pytyagorean triple number")
else:
    print("They are not pytyagorean triple number ")