def isHappy(a):
    try:
        b=float(a)
    except:
        return False
    if b < 0:
        return False
    if b % 1 != 0:
        return False
    
    return True

if isHappy("4"):
    print("Yeah!")
else:
    print("Opps")