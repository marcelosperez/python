def choose_day_of_week(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day, "Invalid day")

user_input = int(input("Enter a number (1-7) to choose a day of the week: "))
print(choose_day_of_week(user_input))