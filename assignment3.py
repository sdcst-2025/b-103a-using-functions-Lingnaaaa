def isPerfectSquare(float):
    x=float ** 0.5
    if x % 1 != 0:
        return False
    return True

if isPerfectSquare(4):
    print('This is a perfectsquare number')
else:
    print('opps')