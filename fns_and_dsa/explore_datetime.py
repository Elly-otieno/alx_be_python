'''
Objective: Familiarize yourself with Python’s datetime module by writing a script that performs specified operations with dates and times.

Task Instructions:
Your task is to create a Python script named explore_datetime.py. This script will demonstrate your ability to use the datetime module for handling dates and times in Python.

Part 1: Display the Current Date and Time

Research how to use the datetime module to obtain the current date and time.
Create a function with a name display_current_datetime and
save the current date inside a current_date variable
Format and print the current date and time in a readable format, such as “YYYY-MM-DD HH:MM:SS”.
Part 2: Calculate a Future Date

Prompt the user to enter a number of days (as an integer).
Create a function with a name calculate_future_date and
saves the future date inside a future_date variable
Calculate what the date will be after adding the specified number of days to the current date.
Print the future date in a format like “YYYY-MM-DD”.
'''

from datetime import date, datetime, timedelta

def display_current_datetime():
    # current_date = datetime.now()
    # use strftime - to format the date
    current_date = datetime.now()
    return current_date
#strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date():
    
    current_date = display_current_datetime()
    print(f'Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}')

    days = int(input('Enter number of days to add to the current date: '))
    future_date = current_date + timedelta(days=days)

    
    print(f'Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}')



if __name__ == "__main__":
    calculate_future_date()