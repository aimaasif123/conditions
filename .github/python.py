def check_even_odd(num):
    if num % 2 == 0:
        print (f" {num} is Even.")
    else:
        print (f" {num} is Odd.")
# Function to check if a number is positive, negative, or zero
def check_numbers(num):
    if num > 0:
        print ( f" {num} is positive.")
    elif num < 0:
        print ( f" {num} is Negative.") 
    else:
        print ( " The number is zero.")   
# Function to check divisibility
def check_numbers(num):
    divisible_by_2 = (num % 2 == 0)
    divisible_by_3 = (num % 3 == 0)
    if divisible_by_2 and divisible_by_3:
        print (f" {num} is divisible by both 2 and 3.")
    elif divisible_by_2:
        print (f" {num} is divisible by 2 but not by 3.")
    elif divisible_by_3:
        print (f" {num} is divisible by 3 but not by 2.")
    else:
        print (f" {num} is not divisible by either 2 or 3.")
# Function to check voting eligibility
def check_numbers(age):
    if age >= 18:
        nationality = input (" Do you have a nationality of Pakistan? ( yes/no):")
        if nationality.lower() == "yes":
            print (" you are eligible to vote.")
        else:
            print (" Please obtain a valid ID to vote.")
    else:
        print (" you are not eligible to vote. ")
# Function to determine age category
def check_age_category(age):
    if 0 <= age <= 12:
        print (" The person is a Child.")
    elif 13 <= age <= 19:
        print (" The person is a Teenager.")
    elif 20 <= age <= 59:
        print ( " The person is an adult.")
    else:
        print (" The person is a Senior Citizen.")
# Function to determine days in a month
def days_in_month(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print ("31 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print ("30 days")
    elif month == 2:
        print ("28 days")
    else:
        print ("Invalid month")
# function to check if a year ia a leap year
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print (f" {year} is a leap year.")
    else:
        print (f" {year} is not a leap year.") 