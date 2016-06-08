__author__ = 'chisaton'

#First set of Python Exercises from book

#Exercise 13
#get length and width of rectangle and
#display the area

 length = input("Enter the length of a rectangle: ")
 length = int(length)

 width = int(input("Enter the width of the rectangle: "))
 print("The area is ", length * width, " square units")

#Exercise 15
#Get a character. Write congrats if a vowel otherwise you lose

 character = input("Enter a character: ")
 if character in ["a","e","i","o","u"]:  #['a','e','i','o','u']でもオッケー
     print("Congratulations - you picked a voewl!")
 else:
     print("You lose, better luck next time.")

#Exercise 18
#print the even integers from 2 to 30

 n = 2
 while n<=30:
     print(n)
     n += 2

#Exercise 20
#get duration of time in hours and minutes
#print the duration only in minutes

 hours = int(input("Enter the hours: "))
 minutes = int(input("Enter the minutes: "))
 total = hours * 60 + minutes
 print(total)

#Exercise 22
#get some integer and print the sum of positive number and negative number

 stop = True
 sum1 = 0
 sum2 = 0
 while(stop):
     integer = int(input("Enter an integer: "))
     if integer>0:
         sum1 += integer
     elif integer<0:
         sum2 += integer
     else:
         stop = False

 print(sum1)
 print(sum2)

#Exercise 25
#write the function that print sum and multiple of two parameter

 def sum(n1,n2):
     print(n1+n2)
     print(n1*n2)

 sum(3,5)

#Exercise 28+29
#get miles and gallons
#print miles per gallons

 def milesPerGallon(miles, gallon):
     return miles/gallon

 miles = int(input("Enter the miles driven: "))
 gallon = int(input("Enter the gallons of gas used: "))

 print(milesPerGallon(miles, gallon))

#Exercise 31
#get three room's dementions
#print the total cost of carpeting

def getFeet():
    feetL = float(input("Enter length of a room in feet: "))
    feetW = float(input("Enter width of a room in feet: "))

    return feetL, feetW

def feetIntoYard(feet):
    yard = feet * 0.33333
    return yard

def computeArea(yardL, yardW):
    area = yardL * yardW
    return area

def computeCost(area):
    cost = area * 8.95
    return cost

def main():
    sum = 0
    i = 0

    while i < 3:
        feetL, feetW = getFeet()
        yardL = feetIntoYard(feetL)
        yardW = feetIntoYard(feetW)
        area = computeArea(yardL, yardW)
        cost = computeCost(area)
        sum += cost
        i += 1

    print("The total cost is " , sum)

main()
