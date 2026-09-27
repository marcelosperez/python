def choose_day_of_week(day):

    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"


try:
    user_input = int(input("Enter a number (1-7) to choose a day of the week: "))
    print(choose_day_of_week(user_input))

except ValueError:
    print("Please enter a number.")