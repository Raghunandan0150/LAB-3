# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 19:39:29 2026

@author: Lenovo
"""

A=int(input("enter angle1 : "))
B=int(input("enter angle2 : "))
C=int(input("enter angle3 : "))
if A+B+C!=180 :
    print("Invalid Triangle")

elif A>90 :
    print("Obtuse angled triangle")
elif A==90 :
    print("Right angled triangle")
else:
    print("Acute angled triangle")