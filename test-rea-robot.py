#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################################################################################################################
## Start Date: 19-Feb-2019
## Last Modified: 19-Feb-2019
## Version: 1.0
## 
## TDD - REA Robot Training Program 
## 20-Feb   Initial testing skelaton developed.
## 21-Feb   Add test_rea_robot_object and test_rea_robot_command.
##
#####################################################################################################################################################################

import unittest
from rea_robot import *

class ReaRobotTests(unittest.TestCase):
    rr = ReaRobot()

    def test_rea_robot(self):
        self.assertEqual(hello_rea_robot(), 'Hello Rea Toy Robot!!!')

    def test_rea_robot_object(self):        
        self.assertEqual(self.rr.report_name(), 'Rea Toy Robot !!!')
        self.assertEqual(self.rr.get_curr_position(), 'My current position at (0,0) facing NORTH.')

    def test_rea_robot_command(self):        
        self.assertTrue(self.rr.chk_command("PLACE"))
        self.assertTrue(self.rr.chk_command("MOVE"))
        self.assertTrue(self.rr.chk_command("LEFT"))
        self.assertTrue(self.rr.chk_command("RIGHT"))
        self.assertFalse(self.rr.chk_command("BACK"))
        self.assertFalse(self.rr.chk_command("TURN"))

if __name__ == '__main__':
    unittest.main()