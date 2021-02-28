import datetime
import time

class EventRecorder:
    def __init__(self):
        self.now = time.time()
        self.events = []
