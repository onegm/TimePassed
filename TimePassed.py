from datetime import datetime, timedelta, time

class TimeCounter:
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.time_elapsed = timedelta(seconds = 0)
        pass

    def start(self):
        self.start_time = datetime.now()
        return self.start_time

    def stop(self):
        self.stop_time = datetime.now()
        time_elapsed = self.time_elapsed
        self.time_elapsed = timedelta(seconds = 0)
        return time_elapsed + (self.stop_time - self.start_time)

    def pause(self):
        self.stop_time = datetime.now()
        self.time_elapsed = self.time_elapsed + self.stop_time - self.start_time
        return self.time_elapsed

    def show(self):
        return self.time_elapsed
