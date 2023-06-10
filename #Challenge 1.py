#Challenge 1
import math


# Write a function that takes the base and height of a triangle and return its area

def tri_area():
    x= int(input("base: "))
    y= int(input("height: "))
    area = (x*y)/2
    print (area)

tri_area()

# Create a function that takes an integer and returns the factorial of that integer. 

def find_factorial():
    n = int(input("Find the factorial of this number: "))
    fact = math.factorial(n)
    print(fact)

find_factorial()

def longest_time():
    h = int(input("Hours(s): "))
    m = int(input("Minute(s): "))
    s = int(input("Seconds(s): "))

    h_to_s = h*3600 #converting them both to seconds
    m_to_s = m*60

    if (h_to_s > m_to_s) and (h_to_s) > s:
        print (h)
    elif (m_to_s > h_to_s) and (m_to_s) > s:
        print (m)
    else:
        print (s)

longest_time()



