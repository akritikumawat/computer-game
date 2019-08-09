from random import *
count=0
l=1
h=100
while True:
    x=randint(l,h)
    print("my guess",x)
    count=count+1
    s=int(input("please give me a hint:"))
    if s==1:
        l=x
    elif s==2:
        h=x
    elif s==3:
        break;
print("congratulations computer you found it in",count,"attempts")
        #if number i have choosed is smaller thn guess thn i will enter 2
        #if number is greater thn enter 1
