#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################################################################################################################
## Start Date: 19-Feb-2019
## Last Modified: 23-Feb-2019
## Version: 1.5
## 
## TDD - REA Robot Training Program 
## 20-Feb-2019      Initial testing skelaton developed.
## 21-Feb-2019      Add test_rea_robot_object and test_rea_robot_command.
## 22-Feb-2019      Add in 4 corner edge movement ignore test case.
## 23-Feb-2019      Add in command file line test cases.
#####################################################################################################################################################################

import unittest
from rea_robot import *

class ReaRobotTests(unittest.TestCase):
    rr = ReaRobot()  

    def test_rea_robot_object(self):        
        self.assertEqual(self.rr.report_name(), 'Rea Toy Robot !!!')
        
    def test_rea_robot_command(self):        
        self.assertTrue(self.rr.chk_command("PLACE"))
        self.assertTrue(self.rr.chk_command("MOVE"))
        self.assertTrue(self.rr.chk_command("LEFT"))
        self.assertTrue(self.rr.chk_command("RIGHT"))
        self.assertFalse(self.rr.chk_command("BACK"))
        self.assertFalse(self.rr.chk_command("TURN"))

    def test_rea_robot_example(self):
        ## Default place to (0,0,NORTH)
        self.rr.place()
        self.assertEqual(self.rr.get_report(), "0,0,NORTH")

        self.rr.place(0,0,"NORTH")
        self.rr.move()
        self.assertEqual(self.rr.get_report(), "0,1,NORTH")

        self.rr.place(0,0,"NORTH")
        self.rr.left()
        self.assertEqual(self.rr.get_report(), "0,0,WEST")

        self.rr.place(1,2,"EAST")
        self.rr.move()
        self.rr.move()
        self.rr.left()
        self.rr.move()
        self.assertEqual(self.rr.get_report(), "3,3,NORTH")

    def test_rea_robot_edge_lower_left_corner(self):
        self.rr.place()
        self.rr.left()
        self.rr.move()
        self.rr.move()
        self.rr.move()
        ## Robot remain lower left corner. Moving will drop.        
        self.assertEqual(self.rr.get_report(), "0,0,WEST")

    def test_rea_robot_edge_lower_right_corner(self):
        self.rr.place(4, 0, "WEST")
        self.rr.right()
        self.rr.right()
        self.rr.move()
        self.rr.move()
        self.rr.move()
        ## Robot remain lower right corner. Moving will drop.        
        self.assertEqual(self.rr.get_report(), "4,0,EAST")

    def test_rea_robot_edge_upper_right(self):
        self.rr.place(4,4,"NORTH")
        self.rr.move()
        self.rr.move()
        self.rr.right()
        self.rr.move()
        self.rr.move()
        self.rr.right()
        ## Robot remain upper right corner. 
        self.assertEqual(self.rr.get_report(), "4,4,SOUTH")

    def test_rea_robot_edge_upper_left(self):
        self.rr.place(0,4,"NORTH")
        self.rr.move()
        self.rr.move()
        self.rr.left()
        self.rr.move()
        self.rr.move()
        self.rr.left()
        ## Robot remain upper left corner. 
        self.assertEqual(self.rr.get_report(), "0,4,SOUTH")

    def test_rea_robot_process_command_file_1(self):
        self.rr.process_command_file("cmd_test_1.txt")
        self.assertEqual(self.rr.get_report(), "2,2,NORTH")

    def test_rea_robot_process_command_file_2(self):
        self.rr.process_command_file("cmd_test_2.txt")
        self.assertEqual(self.rr.get_report(), "0,0,WEST")

    def test_rea_robot_process_command_file_3(self):
        self.rr.process_command_file("cmd_test_3.txt")
        self.assertEqual(self.rr.get_report(), "4,4,EAST")


if __name__ == '__main__':
    unittest.main()