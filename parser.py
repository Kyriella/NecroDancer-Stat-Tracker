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


def is_int(num):
    """Return True if string is an int, False if it is not."""
    try:
        int(num)
        return True
    except ValueError:
        return False


def convert_nums(item):
    """If string is a number, return it as an int. Otherwise, return it as a string."""
    if is_int(item):
        return int(item)
    else:
        return item


def parse_line(current, run):
    """Parse the current line, do something with it (if necessary)."""
    split = [convert_nums(item) for item in current.split()]

    # Decide what to do with the rest of the information by what the first word is.
    if split[0] == 'DETERMINISTIC':
        if split[4] == 1 and split[6] == 1:  # If starting on 1-1, start a new run.
            run.new(split[4], split[6])
        else:  # Otherwise, update the current zone/floor.
            run.update_floor(split[4], split[6])
    elif split[0] == "MOVE":  # Keeps track of the beat count for each floor.
        run.update_beat_num(split[2])
    elif split[0] == "No":  # Toggles low% (always 1 -> 0).
        run.toggle_low_percent()
    elif split[0] == "Player":  # Retrieve what killed player, update run to killed.
        run.killed(split)
