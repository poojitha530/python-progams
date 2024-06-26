#factorial
n=int(input("enter n:"))
if (n==1):
      f=1
else:
    f=1
    for p in range(1,n+1,1):
        f=f*p
print("factorial is:",f)    
      
#prime number
n=int(input("enter n:"))
c=0
for p in range(1,n+1):
   if(n%p==0):
       c=c+1
if (c==2):
    print("prime number")
else:
    print("not prime number")
#read the string and no of vowels and no of consonents
'''s=input("enter a string:")
s=s.lower()
vc=cc=0
v="a,e,i,o,u"
for p in s:
    if p in v:
        vc=vc+1
    else:
        cc=cc+1
print("vowel count=",vc)
print("consonets count=",cc)'''

        
