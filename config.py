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

import configparser

config = configparser.ConfigParser()


def necrodancer_dir():
    """Allows the user to choose their Steam or NecroDancer directory.
    ONLY WORKS ON UNIX-BASED SYSTEMS AT THE MOMENT"""
    while True: # Loop until a valid path is specified
        path = input('Please enter the path to either your \'Steam\' or your \'Crypt of the NecroDancer\' directory:\n')
        split_path = path.split('/')    # Split path to detect if directory is Steam or NecroDancer
        split_path = [x for x in split_path if x.strip()]   # Remove entries of only whitespace
        if split_path[-1] == 'Steam':
            path = '/' + '/'.join(split_path) + '/steamapps/common/Crypt of the NecroDancer/'
            break
        elif split_path[-1] == 'Crypt of the NecroDancer':
            path = '/' + '/'.join(split_path) + '/'
            break
        else:
            print('Not a valid path')
    print('Saving %s as the Crypt of the Necrodancer directory' % path)
    config['general'] = {'directory': path}


def create():
    """Create config file with no options set"""
    print('Creating config file')
    necrodancer_dir()

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def open_():
    """Try to open the config file, close it and read it if it exists; create it otherwise"""
    try:                                # Try to open the file, except if it doesn't exist
        try_ = open('config.ini')
        print('Config file exists!')
        try_.close()
        config.read('config.ini')
    except FileNotFoundError:           # If file doesn't exist, create it, then open it
        print('Config file not found!')
        create()
        open_()
