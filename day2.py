#!/usr/bin/env python3

print ("create a program that takes input for their name and age,then print a greeting with their name and calculates the year they were born")

#input users name and age
name= input("enter your name: ")
age= input("enter your age: ")

#convert age to integer
age= int(age)

#caculate year of birth
current_year=2025 
year_of_birth= current_year - age

#print a greeting with their name and year_of_birth
print(f"hi {name} hope you see christ is working, you were born in the year {year_of_birth}")
