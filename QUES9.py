
#. Enter the coefficients of two straight lines a1x + b1y = c1 and a2x + b2y = c2 and display their point of intersection. Handle all the cases for invalid input as well as the cases where the two lines are parallel or coincident, and display the solution till exactly 2 decimal places.



a1=int(input("a1"))
b1=int(input("b1"))
c1=int(input("c1"))
a2=int(input("a2"))
b2=int(input("b2"))
c2=int(input("c2"))
x=input("x axis")
y=input("y axis")

#a1*x + b1*y = c1
#a2*x + b2*y = c2

determinant = a1 * b2 - a2 * b1

if determinant == 0:
        if (a1 * c2 == a2 * c1) and (b1 * c2 == b2 * c1):
            print("The two lines are coincident (infinite solutions).")
        else:
            print("The two lines are parallel (no solution).")
else:
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    a=format(x,'.2f')
    b=format(y,'.2f')
    print(x,y)
