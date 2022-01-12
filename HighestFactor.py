# This function print the Highest Factor between two numbers.

def highestFactor(numX,numY):
    if numX > numY:
        x = numY
    else:
        x = numX
    while x > 1:
        if numX % x == 0 and numY % x == 0:
            break
        x -= 1
    print (x)


highestFactor(36,54)