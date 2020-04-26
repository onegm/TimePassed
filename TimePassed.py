from datetime import datetime, time

class TimeCounter:
    def __init__(self):
        pass
    def start(self):
        global Starting_Time
        Starting_Time = datetime.now()
        pass
    def stop(self):
        Stopping_Time = datetime.now()
        global TimeElapsed
        TimeElapsed = Stopping_Time - Starting_Time
        pass
    def show(self):
        print(TimeElapsed)
        pass
    pass


