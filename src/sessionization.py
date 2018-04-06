import time
import sys
from collections import OrderedDict

from utils import convert_datetime, time_diff
from session import Session

def process_log(log_path, inactive_period_path, output_path):
    """ Process the given log data and write the desired results to a file
        Args:
            log_path: a string indicates the file path of log data
            inactive_period_path: a string indicates the file path of inactive period
            output_path: a string indicates the file path of log data
    """
    try:
        # read the inactive_period
        with open(inactive_period_path, "r") as f:
            inactive_period = int(f.readline())

        # main logic for processing the log data
        with open(log_path, "r") as r, open(output_path, "w") as w:    
            # A OrderedDict used to store session info - key: ip, value: session
            ip_map = OrderedDict()
            date_time = ""
            
            r.readline() # reads the title
            first_line = r.readline() # first record
            fields = first_line.split(",")
            init_time = convert_datetime(fields[1], fields[2]) # timestamp of the first record 
            session = Session(fields[0], init_time)
            ip_map[fields[0]] = session

            for line in r:
                fields = line.split(",")
                if len(fields) != 15: 
                    continue

                ip = fields[0]
                # if a new date time is identified
                if date_time != fields[1] + " " + fields[2]:
                    date_time = fields[1] + " " + fields[2]
                    # convert a given date and time to a datetime object
                    dt = convert_datetime(fields[1], fields[2])
                    all_ip = list(ip_map.keys())

                    # only starts to check inactive session when the difference between current time
                    # and the init_time of first record is greater than inactive_period
                    if time_diff(init_time, dt) > inactive_period:           
                        for exist_ip in all_ip:
                            # when identifies the record which init_time is less than and equalt to
                            # current time, there is no need to continue
                            if time_diff(ip_map[exist_ip].init_time, dt) <= inactive_period:
                                break

                            # finds the sessions that were over, write to sessionization.txt and remove from ip map
                            if time_diff(ip_map[exist_ip].last_request_time, dt) > inactive_period:
                                w.write(ip_map[exist_ip].get_output())
                                ip_map.pop(exist_ip)

                # if ip is not in ip_map, creates a new session. Otherwise, updates the last_request_time
                if ip not in ip_map:
                    session = Session(ip, dt)
                    ip_map[ip] = session
                else:
                    session = ip_map[ip]
                    session.last_request_time = dt
                    session.increment_count()

            # when reaches the end of file, handle the rest of sessions.
            rest_ips = list(ip_map.keys())
            for rest_ip in rest_ips:
                w.write(ip_map[rest_ip].get_output())
                ip_map.pop(rest_ip)

    except FileNotFoundError as fe:
        print(str(fe))

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) < 4:
        raise Exception("Not enough arguments")    

    log_path, inactive_period_path, output_path = argvs[1:]

    start_time = time.time()  
    process_log(log_path, inactive_period_path, output_path)      
    elapsed_time = time.time() - start_time
    print("completed in {}s".format(round(elapsed_time), 2))