import time
from collections import OrderedDict

from utils import convert_datetime, time_diff
from session import Session
start_time = time.time()
with open("sample.csv", "r") as r, open("sessionization.txt", "w") as w:
    
    r.readline()
    first_line = r.readline()
    fields = first_line.split(",")
    ip_map = OrderedDict()
    init_time = convert_datetime(fields[1], fields[2])
    session = Session(fields[0], init_time)
    ip_map[fields[0]] = session

    date_time = ""
    k = 2
    for line in r:
        fields = line.split(",")
        ip = fields[0]

        if date_time != fields[1] + " " + fields[2]:
            date_time = fields[1] + " " + fields[2]
            # convert a given date and time to a datetime object
            dt = convert_datetime(fields[1], fields[2])
            all_ip = list(ip_map.keys())
            for exist_ip in all_ip:
                if time_diff(ip_map[exist_ip].last_request_time, dt) > k:
                    w.write(ip_map[exist_ip].get_output())
                    ip_map.pop(exist_ip)


        # if ip not in ip_map create a new session, otherwise update the last_request_time
        if ip not in ip_map:
            session = Session(ip, dt)
            ip_map[ip] = session
        else:
            session = ip_map[ip]
            session.last_request_time = dt
            session.increment_count()

    rest_ips = list(ip_map.keys())
    for rest_ip in rest_ips:
        w.write(ip_map[rest_ip].get_output())
        ip_map.pop(rest_ip)
        
elapsed_time = time.time() - start_time
print("completed in seconds: {}s".format(round(elapsed_time), 2))