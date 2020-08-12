import datetime
import calendar

def calc_day(day : str, next = False):

    """
    Returns a datetime for the next or coming day that is coming.

    Params:

        day : str
            The day you want to search for. Must be in
            [
                "monday"
                "tuesday"
                "wednesday"
                "thursday"
                "friday"
                "saturday"
                "sunday"
            ]

        next : bool
            If true, returns the next wednesday (skips the first one)
            Defaults to False if not passed in

    Returns:
        A datetime.date of the day

    """
    

    delta = 8 if next else 1
    date = datetime.date.today() + datetime.timedelta(days = delta)

    for _, i in enumerate(range(7)):
        date += datetime.timedelta(days = 0 if i == 0 else 1)
        
        if calendar.day_name[date.weekday()].lower() == day.lower():
            return date

if __name__ == "__main__":
    
    print(calc_day('thursday', True))