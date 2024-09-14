#check wehether the given number is perfect square
import math
a=int(input('Enter the number:'))
temp= math.sqrt(a)
temp1 = int(temp)
if temp==temp1:
    print('the given number is perfect square')
else:
    print('the given number is not perfect square')
