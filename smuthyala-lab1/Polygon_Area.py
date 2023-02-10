'''
This program helps in finding area of a polgon.
Name : Sanjay Reddy Muthyala
'''
import math as m
try:
    n = int(input("Enter the number of sides:"))
    l = float(input("Enter the length:"))
    area = float((l * l * n) / (4 * m.tan(m.pi / n)))
    print("Area of the polygon:", format(area, '.4f'))
except:
    print("Invalid entry for a polygon")

