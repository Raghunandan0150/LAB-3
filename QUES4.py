n=int(input("enter number : "))
d1=n//1000
d2=(n//100)%10
d3=(n//10)%10
d4=n%10
s1=d1+d2
s2=d3+d4

if s1 == s2:
    print("sums are equal")
else:
    print("sums are not equal")
    