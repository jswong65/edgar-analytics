import datetime

def convert_datetime(date, time):
    # A function to create a datetime object from given date and time
    return datetime.datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')
    
def time_diff(dt1, dt2):
    return abs(int((dt2 - dt1).total_seconds()))
