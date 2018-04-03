class Session(object):
    def __init__(self, ip, init_time):
        self._ip = ip
        self._init_time = init_time
        self._last_request_time = init_time
        self._count = 1

    @property
    def ip(self):
        return self._ip
    
    @property
    def last_request_time(self):
        return self._last_request_time

    @last_request_time.setter
    def last_request_time(self, timestamp):
        self._last_request_time = timestamp

    @property
    def count(self):
        return self._count

    def increment_count(self):
        self._count += 1

    def __str__(self):
        return self._ip + ", count: " + str(self._count)