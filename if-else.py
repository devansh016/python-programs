# https://www.hackerrank.com/challenges/py-if-else/problem

import math
a = int(input())

if a%2==1:
    print("Weird")
elif 2<=a and a<=5 :
    print("Not Weird")
elif 6<=a and a<=20 :
    print("Weird")
else:
    print("Not Weird")