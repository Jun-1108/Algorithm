import sys
a,b,c=map(int,sys.stdin.readline().split())

if(a==b==c):
   result= a*1000+10000
elif a==b:
    result=a*100+1000
elif b==c:
    result=b*100+1000
elif a==c:
    result=a*100+1000
else:
    result=max(a,b,c)*100

print(result)       

