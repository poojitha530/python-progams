def disaries(s):
    l=len(s)
    n=int(s)
    s1=0
    m=n
    while(n!=0):
        r=n%10
        s1=s1+(r**l)
        n=n//10
        l=l-1
        if(m==s):
            print("desaries num:")
        else:
            print("not desaries num:")
n=int(input("enter n:"))
disaries(n)
