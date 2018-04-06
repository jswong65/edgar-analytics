class Session(object):
    """
    This class is used to store related information of a session
    """
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

    def increment_count(self):
        """ 
        increment the count value by 1 
        """
        self.__count += 1

    def __duration_cal(self):
        """ 
        calculate the duration of a session 
        """
        return int((self.__last_request_time - self.__init_time).total_seconds()) + 1 

    
    def get_output(self):
        """
        return the desired output format for writing the session to a file
        """
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
        