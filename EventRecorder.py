import datetime
import time


class EventRecorder:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.events = []

    def add_event(self, event):
        # record how much time has passed between the last event and the current one
        timedelta = self.get_timedelta()
        self.now = datetime.datetime.now()

    def get_timedelta(self):
        return datetime.datetime.now() - self.now