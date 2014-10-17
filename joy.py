#!/usr/bin/python
# coding: utf-8
# Copyright 2014 Luke Macken <lewk@csh.rit.edu>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
A tool for using joystick buttons to click on stuff.

Uses xdotool to move the mouse and click on specific locations, but
can be adapted to do anything you want.
"""

import sys
import pygame

from subprocess import call

X = 1
CIRCLE = 2
SQUARE = 0
TRIANGLE = 3
R1 = 5
L1 = 4
R2 = 7
L2 = 6
L3 = 10
R3 = 11
START = 9
SELECT = 8
HOME = 12
UP = (0, 1)
DOWN = (0, -1)
RIGHT = (1, 0)
LEFT = (-1, 0)
PIXELS = 10  # Number of pixels to jump in each direction

pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print('No joysticks found')
    pygame.quit()
    sys.exit(1)
elif joystick_count > 1:
    print('Available joysticks:')
    sticks = []
    for i in range(joystick_count):
        stick = pygame.joystick.Joystick(i)
        sticks.append(stick)
        print('%d: %s' % (i, stick.get_name()))
    i = int(raw_input('Which joystick? ').strip())
    stick = pygame.joystick.Joystick(i)
    stick.init()
elif joystick_count == 1:
    stick = pygame.joystick.Joystick(0)
    stick.init()

clock = pygame.time.Clock()

done = False
while not done:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('QUIT')
                done = True
            if event.type == pygame.JOYBUTTONDOWN:
                continue
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == X:
                    print(u'✖')
                    call(['xdotool', 'mousemove', '1266', '1082'])
                    call(['xdotool', 'click', '1'])
                elif event.button == CIRCLE:
                    print(u'●')
                    call(['xdotool', 'mousemove', '1416', '1082'])
                    call(['xdotool', 'click', '1'])
                elif event.button == TRIANGLE:
                    print(u'▲')
                elif event.button == SQUARE:
                    print(u'◼')
                    call(['xdotool', 'mousemove', '1528', '894'])
                    call(['xdotool', 'click', '1'])
                elif event.button == R2:
                    call(['xdotool', 'mousemove', '1625', '1031'])
                    call(['xdotool', 'click', '1'])
                elif event.button == R1:
                    call(['xdotool', 'mousemove', '1498', '1029'])
                    call(['xdotool', 'click', '1'])
                elif event.button == L2:
                    call(['xdotool', 'mousemove', '1607', '1079'])
                    call(['xdotool', 'click', '1'])
                elif event.button == START:
                    call(['xset', 'dpms', 'force', 'off'])
            elif event.type == pygame.JOYHATMOTION:
                if event.value == (0, 0):
                    pass
                x, y = map(str, map(lambda i: i * PIXELS, event.value))
                call(['xdotool', 'mousemove_relative', '--', x, y])
            #elif event.type == pygame.JOYAXISMOTION:
            #    print(event)

        clock.tick(600)
    except KeyboardInterrupt:
        done = True

pygame.quit()

# vim: ts=4 sw=4 expandtab ai
