"""
Copyright 2015 Kyriella

This file is part of NecroDancer Stat Tracker.

NecroDancer Stat Tracker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NecroDancer Stat Tracker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with NecroDancer Stat Tracker.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import time

import config

logs_path = config.config['general']['directory'] + 'logs/'
print("Using %s as the log directory" % logs_path)


def month_to_num(log):
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
              'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    split = log.split('_')
    split[3] = months.index(split[3].upper())

    return split


def find_latest(logs):
    return max(logs, key=month_to_num)  # Sort the logs using above key, return latest.


def open_latest():
    """Return opened latest logfile (the one being actively written to by the game)."""
    logs = os.listdir(logs_path)  # Store list of log files.
    # print logs
    latest = logs_path + find_latest(logs)  # Find and store the path to the latest log.
    print("Using %s as the latest log" % latest)

    return open(latest)


def readline(log):
    """Read a single line of the logfile, exit if there is no line to be read."""
    continue_ = False
    while not continue_:        # Try repeatedly to read a line, exit the loop if you can.
        last_read = log.tell()  # Store the last read line so it doesn't get read again.
        line = log.readline()   # Store the current line, or False if there is none to read.
        if not line:            # If there is no line to read, seek to the last read line.
            time.sleep(0.1)
            log.seek(last_read)
        else:                   # If there is a line to read, exit the loop.
            continue_ = True

    return line
