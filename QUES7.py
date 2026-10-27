
n=int(input("enter number : "))
d1=n//100
d2=(n//10)%10
d3=n%10

x=d1+d2+d3
if n%x==0 :
    print("N is Harshad number")
else:
    print("N is not a Harshad number")