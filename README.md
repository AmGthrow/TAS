# TAS
Macro program that makes it easy to record and replay keystrokes for speed-running games or automating menial tasks.


## Installation
1. Make sure you've got [Python](https://www.python.org/downloads/) installed.
2. Get a local copy of the repository using either `git clone https://github.com/AmGthrow/TAS.git` or just regular downloading. The only files you actually are `EventRecorder.py`, `Events.py`, and `tasbot.py`.
3. run `pip install -r requirements.txt` to get all dependencies (nothing but `pynput`, actually)

## Usage
1. Open up a terminal and run `python tasbot.py` to start the script.
2. If you want to save a new recording, 
    <ol type="A">
        <li>press `Ctrl + Shift + F1`</li>
        <li>perform all the actions you want to be recorded</li>
        <li>If you want to replay the recording you currently have saved, press `Ctrl + Shift + F2`</li>
    </ol>

3. If you want to replay the recording you currently have saved, press `Ctrl + Shift + F2`
    <ol type="A">
    <li>Press `Ctrl + Shift + F2` to start the playback</li>
    <li>Either wait for the replay to finish or press `Ctrl + Shift + F2` to end it early</li>
    </ol>

**NOTE** It's always a bit risky to automate your mouse and keyboard. To instantly close the script, press `Ctrl + Shift + Esc`

## Overview
The script creates a `TASbot` instance from `tasbot.py` which is mainly responsible for listening to keystrokes and playing them back. To store the actual actions that the user is executing, an `EventRecorder` keeps a list of all the events with two bits of information:
1. What the action is (a key press, a mouse click, etc.)
2. The time taken since the last event

When the `EventRecorder` plays the events back, it just executes the events in FIFO order and uses a `time.sleep()` to wait the appropriate amount of time between each event.
