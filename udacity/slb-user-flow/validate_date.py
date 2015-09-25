months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]

def validate_month(month):
    if month:
        month = month.lower()
    if month in months:
        return True
    else:
        return None

def validate_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return True
        else:
            return None
    else:
        return None

def validate_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= 2015:
            return True
        else:
            return None
    else:
        return None