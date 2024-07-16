"""
If it is a multiple of 3, display "Zip"

If it is a multiple of 5, display "Zap"

If it is a multiple of both 3 and 5, display "Zoom"

If it does not satisfy any of the above given conditions, display "Invalid"
"""

def zipzap(num):
    if (num % 3 == 0) and (num % 5 != 0):
        print('Zip')
    elif (num % 5 == 0) and (num % 3 != 0):
        print('Zap')
    elif ((num%3 == 0) and (num%5 == 0)):
        print('Zoom')
    else:
        print('Invalid')
        
zipzap(9)
zipzap(30)
zipzap(25)
zipzap(49)