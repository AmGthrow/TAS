"""This contains the stuff I use to record Keyboard and Mouse events.
My problem is that pynput has no way of memorizing the time between each event,
so EventRecorder is kind of a wrapper that lets me execute events with the 
correct time delay between them.
"""

import datetime
import time


class EventRecorder:
    def __init__(self):
        self.now = datetime.datetime.now()
        self.events = []  # array of tuples that looks like [(timedelta, Event)]

    def add_event(self, event):
        """Adds an Event to the EventRecorder, as well as the time between each event

        Args:
            event (Event): The event to be recorded
        """
        # record how much time has passed between the last event and the current one
        timedelta = self.get_timedelta()

        # Update what "now" is
        self.now = datetime.datetime.now()

        # add the event to the list of events in this EventRecorder
        self.events.append((timedelta, event))

    def get_timedelta(self):
        return datetime.datetime.now() - self.now

    def __iter__(self):
        """Generator which uses time.sleep() to pause
        between sending each Event

        Yields:
            Event: each event that's been recorded
        """
        for timedelta, event in self.events:
            time.sleep(timedelta.total_seconds())
            yield event
