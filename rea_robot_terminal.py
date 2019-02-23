#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################################################################################################################
## Start Date: 22-Feb-2019
## Last Modified: 23-Feb-2019
## Version: 1.1
## 
## REA Robot Terminal Class
## 22-Feb-2019  Completed terminal shell implementation.
## 23-Feb-2019  Add in command case invariant.
##
#####################################################################################################################################################################
import cmd
from rea_robot import *

class rea_robot_terminal(cmd.Cmd):

    def register_rea_robot(self, robot):
        self.rr = robot

    def preloop(self):
        self.rr.report_yourself()
    
    def precmd(self, line):
        line = line.lower()
        return line

    def do_report(self, e):
        """
        Report Rea Robot position: (X,Y) and Facing (NORTH, EAST, SOUTH, WEST)
        Form: X,Y,FACING
        """
        self.rr.report()

    def do_left(self, e):
        """
        Turn Rea Robot Facing to 90 deg counter clock-wise without changing the position.
        """
        self.rr.left()

    def do_right(self, e):
        """
        Turn Rea Robot Facing to 90 deg clock-wise wthout changing the position.
        """
        self.rr.right()

    def do_move(self, e):
        """
        Move Rea Robot 1 unit forward from current position in the direction that it's facing.
        """
        self.rr.move()

    def do_place(self, e):
        """
        Place Rea Robot in the specific position and facing direction.
        In general form: place X,Y,F
        For example: place 1,1,NORTH

        Place without any parameter, reset the robot position to 0,0,NORTH.
        """
        if (e==""):
            self.rr.place()
        else:    
            p = e.split(",")
            self.rr.place(int(p[0]), int(p[1]), p[2])

    def do_exit(self, e):
        """
        Exit Rea Robot Terminal ...
        """
        return True