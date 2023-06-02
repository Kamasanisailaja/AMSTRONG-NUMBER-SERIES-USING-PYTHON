n1=int(input("enter the starting limit;"))
n2=int(input("enter the ending limit:"))
for i in range(n1,n2+1):
    sum=0
    m=i
    while m>0:
        l=m%10
        sum=sum+l**3
        m=m//10
        if i==sum:
           print(i)
    
    
        
    
