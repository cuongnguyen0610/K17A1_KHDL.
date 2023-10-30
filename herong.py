import math
a=int(input("nhập vào a:"))
b=int(input("nhập vào b:"))
c=int(input("nhập vào c:"))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("diện tích là:",S)
