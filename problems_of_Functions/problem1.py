#basic function syntax
#write a function to calculate and return the square of a number


def square (number):
    return number ** 2

result = square(4)
print(square(4))    


#Function with Multiple parameters
#create a function that takes two numbers as parameters and return their sum

def add (numOne, numTwo):
    return numOne+numTwo

print(add(5, 5))


#Polymorphism in functions
#write a function multiply that multiplies two numbers, but can also accept and multiply strings


def multiply(p1, p2):
    return p1 * p2

print(multiply(8,5))
print(multiply('a', 5))
print(multiply(5, 'a'))


#function returning multiple values
#create a function that returns both the area and circumference of a circle given its radius.

import math 

def circle_status (radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference 

a, c = circle_status(3)
print("Area: ", a, "Circumference: ", c)