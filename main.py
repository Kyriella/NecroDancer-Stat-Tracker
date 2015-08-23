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


import config
config.open_()  # Open config file so logctl doesn't error
import logctl
import parser
import runctl


run = runctl.Run()
log = logctl.open_latest()
while True:
    current_line = logctl.readline(log)
    parser.parse_line(current_line, run)
