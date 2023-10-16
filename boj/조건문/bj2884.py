import sys
a,b=map(int,sys.stdin.readline().split())
if b<45:
    if(a==0):
        a=23
        b+=60
    else:
        a-=1
        b+=60
print(a,b-45)