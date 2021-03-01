"""This contains the stuff I use to record Keyboard and Mouse events.
My problem is that pynput has no way of memorizing the time between each event,
so EventRecorder is kind of a wrapper that lets me execute events with the 
correct time delay between them.
"""

import datetime
import time


class EventRecorder:
    def __init__(self):
        self.t_last_event = datetime.datetime.now()
        # array of tuples that looks like [(timedelta, Event)]
        self.events = []

    def add_event(self, event):
        """Adds an Event to the EventRecorder, as well as the time between each event

        Args:
            event (Event): The event to be recorded
        """

        if self.events:
            # record how much time has passed between the last event and the current one
            timedelta = self.get_timedelta()
        else:
            # if this is the first event, say "no time has passed"
            timedelta = datetime.timedelta(0)

        # Update what "now" is
        self.t_last_event = datetime.datetime.now()

        # add the event to the list of events in this EventRecorder
        self.events.append((timedelta, event))

    def get_timedelta(self):
        return datetime.datetime.now() - self.t_last_event

    def clear_events(self):
        """Erase all recorded events and start from scratch
        """
        self.events = []

    def __iter__(self):
        """Generator which uses time.sleep() to pause
        between sending each Event

        Yields:
            Event: each event that's been recorded
        """
        for timedelta, event in self.events:
            time.sleep(timedelta.total_seconds())
            yield event
