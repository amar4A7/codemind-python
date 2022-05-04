n=int(input())
s=n**2
flag=0
while n:
    if(n%10!=s%10):
        print('Not an Automorphic Number')
        flag=1
        break
    n=n//10
    s=s//10
if(flag==0):
    print('Automorphic Number')