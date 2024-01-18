import sys
import time

class TimeController:

    init_time = 0
    end_time = 0

    def __init__(self) -> None:
        self.start()


    def getRunTime(self):
        self.end()
        return self.end_time - self.init_time

    def start(self):
        self.init_time = time.time()

    def end(self):
        self.end_time = time.time()