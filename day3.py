#!/usr/bin/env python3
print ("build a simple age checker: ask the user age and tell them if they are eligible for certain services")
#users age
age = int(input("enter your age: "))
if age >= 20:
    print("your networth should be up to $100k")

elif age >= 18:
    print ("you should have at least $1k")

else:
    print( "get a skill")
