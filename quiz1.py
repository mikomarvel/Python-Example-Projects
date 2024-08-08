#python example project_1
#AGE_CALCULATOR

from datetime import datetime #keeps the date updated!

year = input("enter your year of birth.(Eg.1990)")
month = input("enter your month of birth.(E.g 8 june)")
day = input("enter your date of birth.")

print("Y",year, "M", month, "D", day)

x = 2024 - int(year) #this is a method called casting.
print("you are", x, "years old.")
