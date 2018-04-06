import datetime

def convert_datetime(date, time):
    """ creates a datetime object from given date and time
        Args:
            date: a string of date in %Y-%m-%d
            time: a string of time in 
        Returns:
            A datetime obeject with the given date and time information
    """
    return datetime.datetime.strptime(date + " " + time, '%Y-%m-%d %H:%M:%S')
    
def time_diff(dt1, dt2):
    """ calculates difference of time between two datetime objects in seconds
        Args:
            dt1: a datime object
            dt2: another datime object for comparison
        Returns:
            The difference of time between dt1 and dt2 in seconds
    """
    return abs(int((dt2 - dt1).total_seconds()))
