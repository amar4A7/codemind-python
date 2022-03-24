n=int(input())
sum=0
p=1
while n:
    r=n%10
    sum=sum+r
    p=p*r
    n=n//10
if (p==sum):
    print("Spy Number")
else:
    print("Not Spy Number")