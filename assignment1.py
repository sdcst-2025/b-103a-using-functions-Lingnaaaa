def isNegative(a,b,c):
    if a > 0:
        return False
    if b > 0:
        return False
    if c > 0:
        return False
    return True
    
if isNegative(-2.5,-3,-4):
    print('These number are negative number!')
else:
    print("Something is wrong")