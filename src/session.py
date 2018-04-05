class Session(object):
    def __init__(self, ip, init_time):
        self.__ip = ip
        self.__init_time = init_time
        self.__last_request_time = init_time
        self.__count = 1

    @property
    def ip(self):
        return self.__ip
    
    @property
    def init_time(self):
        return self.__init_time

    @property
    def last_request_time(self):
        return self.__last_request_time

    @last_request_time.setter
    def last_request_time(self, timestamp):
        self.__last_request_time = timestamp

    @property
    def count(self):
        return self.__count

    # increment the count value by 1
    def increment_count(self):
        self.__count += 1

    # calculate the duration of a session
    def __duration_cal(self):
        return int((self.__last_request_time - self.__init_time).total_seconds()) + 1 

    def get_output(self):
        return "{},{},{},{},{}\n".format(
                                self.__ip,
                                self.__init_time.strftime('%Y-%m-%d %H:%M:%S'),
                                self.__last_request_time.strftime('%Y-%m-%d %H:%M:%S'),
                                self.__duration_cal(),
                                self.__count
                            )

    def __repr__(self):
        return "ip: {}, count: {}, last_request_time: {}".format(self.__ip, 
                                                            str(self.__count), 
                                                            self.__last_request_time.strftime('%Y-%m-%d %H:%M:%S')) 
        