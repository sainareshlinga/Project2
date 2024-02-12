def add_time(start, duration, start_day=None):
    # Splitting the start time into hours, minutes, and AM/PM
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Splitting the duration time into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Converting start time to 24-hour format
    if period == "PM":
        start_hour += 12

    # Adding duration to start time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    # Handling carry over from minutes to hours
    if end_minute >= 60:
        end_hour += 1
        end_minute -= 60

    # Calculating number of days later
    days_later = end_hour // 24
    end_hour %= 24

    # Converting end time back to 12-hour format
    if end_hour >= 12:
        period = "PM" if end_hour >= 12 else "AM"
        end_hour %= 12
        if end_hour == 0:
            end_hour = 12
    else:
        period = "AM"

    # Determining day of the week if provided
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = days_of_week.index(start_day)
        end_day_index = (start_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        end_time = f"{end_hour}:{end_minute:02d} {period}, {end_day}"
    else:
        end_time = f"{end_hour}:{end_minute:02d} {period}"

    # Formatting output based on number of days later
    if days_later == 0:
        return end_time
    elif days_later == 1:
        return f"{end_time} (next day)"
    else:
        return f"{end_time} ({days_later} days later)"
