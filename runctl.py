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


class Run:
    num = 0
    low_percent = 1
    beats_in_zone = {}      # Format [Zone, Floor], Zone total is [Zone, num_of_floors + 1].
    time_in_zone = {}       # Format [Zone, Floor], Zone total is [Zone, num_of_floors + 1].
    bosses = []             # Dead Ringer, NecroDancer 1/2, and Golden Lute are included.
    current_zone = 0
    current_floor = 0
    zone_killed = 0
    floor_killed = 0
    killed_by = 0
    end_status = 'Reset'    # Updated to "Death" or "Win"

    def new(self, new_zone, new_floor):
        """Save run info, then clear the run info by initializing to default values."""

        # Output run info to file

        print("Starting new run")

        self.update_floor(new_zone, new_floor)

        self.num = 0
        self.low_percent = 1
        self.beats_in_zone = {}
        self.time_in_zone = {}
        self.bosses = {}
        self.zone_killed = 0
        self.floor_killed = 0
        self.killed_by = 0
        self.end_status = 0

    def update_floor(self, new_zone, new_floor):
        """Update Zone and Floor num and store num of beats in that zone/floor."""
        if new_floor == 5 and new_zone != 4:
            new_zone += 1
            new_floor = 1

        if new_zone != self.current_zone:  # If new_zone is not the same as current, update
            # current_zone and current_floor, and total up the
            # num of beats in the zone.

            self.total_beats()  # Total up the num of beats in the zone.

            self.current_zone = new_zone
            print("Zone updated to Zone %s" % self.current_zone)

            self.current_floor = new_floor
            print("Floor updated to Floor %s" % self.current_floor)
        else:  # If new_zone is same as current, only update
            # current floor.
            self.current_floor = new_floor
            print("Floor updated to Floor %s" % self.current_floor)

    def total_beats(self):
        """If not in the lobby, total up the number of beats on each floor of current_zone."""
        if self.current_zone > 0:
            floor_total = 0
            for num in range(1, self.current_floor + 1):
                try:
                    floor_total += self.beats_in_zone[self.current_zone, num]
                except KeyError:
                    continue
            # Save this information as [Zone, Num of floors + 1]
            self.beats_in_zone[self.current_zone, self.current_floor + 1] = floor_total
            print("Total beats in Zone %s = %s" % (self.current_zone, floor_total))

    def update_beat_num(self, current_beat):
        """Set the beats on current floor to the current number of beats on the floor."""
        self.beats_in_zone[self.current_zone, self.current_floor] = current_beat

    def toggle_low_percent(self):
        self.low_percent = 0

    def killed(self, split):
        """Get name of enemy that killed player, store that name, set end_status to 'Killed'"""
        enemy = []
        split = split[3:]  # Cut string down to start of the enemy name
        for item in split:  # Append words to empty list until full name of enemy is appended
            if item != "dmg:":
                enemy.append(item.capitalize())
            else:
                break

        self.killed_by = '_'.join(enemy)
        print("Player killed by %s" % self.killed_by)

        self.end_status = 'Killed'
