def choose_day_of_week(day):

    if day == 1:
        return "Monday"
    elif day == 2:
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid day"


try:
    user_input = int(input("Enter a number (1-7) to choose a day of the week: "))
    print(choose_day_of_week(user_input))

except ValueError:
    print("Please enter a number.")