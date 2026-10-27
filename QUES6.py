
# Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of b moves to c, and the value of c moves to a, without using a fourth variable or multiple assignment operation.



a = 1
b = 2
c = 3

a = a + b + c  
b = a - (b + c) 
c = a - (b + c) 
a = a - (b + c)

print("a =", a, "b =", b, "c =", c)
