#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################################################################################################################
## Start Date: 19-Feb-2019
## Last Modified: 23-Feb-2019
## Version: 1.5
## 
## REA Robot Training Program
##
## Commnad Examples:
## python rea_robot.py -i <command file> | -c : Command line interface | -h : Help
##
## Version Tracking
## Ver 1.5.3
## 18-Feb-2019      Start 1st skelaton.
## 19-Feb-2019      Develop ReaRobot class using Singleton design pattern.
## 20-Feb-2019      Develop basic functions and checking functions.
## 21-Feb-2019      Complete all movement function and edge checking condition.
## 22-Feb-2019      Implement command line interactive mode for Rea Robot.
## 22-Feb-2019      Implement error checking for place position with respect to dimension.
## 23-Feb-2019      Implement file input command.
## 23-Feb-2019      Final testing and refactoring.
#####################################################################################################################################################################

### Imports packages
import sys, getopt, os
from rea_robot_terminal import *

############################################################################################################
## Class Defination
############################################################################################################
class ReaRobot:
    """Class level variables"""
    __instance = None

    ## Define table top dimensions (in unit) 
    dim_x = 5
    dim_y = 5
    edge_x = dim_x - 1
    edge_y = dim_y - 1

    ## Current Situation of Rea Toy Robot.
    curr_x = 0
    curr_y = 0

    ## 0:NORTH, 1:EAST, 2:SOUTH, 3:WEST
    ## Default to face NORTH.
    curr_dir = 0

    ## Define direction directionary.
    dict_dir = {'0':'NORTH', '1':'EAST', '2':'SOUTH', '3':'WEST'}

    ## Define available command list for checking.
    lst_cmd = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']

    ## Command line file Processing mode
    b_cmd_mode = False
   
    @staticmethod 
    def get_instance():
        """ Static access method. """
        if ReaRobot.__instance == None:
            ReaRobot()
        return ReaRobot.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if ReaRobot.__instance != None:
            raise Exception("ReaRobot has already created !")
        else:
            ReaRobot.__instance = self

    def chk_command(self, str_cmd):
        """Check if valid command given"""
        return (str_cmd in self.lst_cmd)

    def report_name(self):
        """The robot report its name ..."""
        return "Rea Toy Robot !!!"

    def get_curr_dir(self):
        """Get current robot facing direction."""
        return self.dict_dir[str(self.curr_dir)]

    def get_curr_position(self):
        """The robot report its current position and facing direction ..."""
        str_curr_pos = "My current position at ({},{}) facing {}.".format(self.curr_x, self.curr_y, self.get_curr_dir())
        return str_curr_pos

    def report_yourself(self):
        """The robot report its info details ..."""
        print ("Hello, I am {} ...".format(self.report_name()))
        print ("Dimension setting - Witdth:{}, Height:{}".format(self.dim_x, self.dim_y))
        print (self.get_curr_position())

    def get_report(self):
        """Return simple latest status report."""
        return "{},{},{}".format(self.curr_x, self.curr_y, self.get_curr_dir())

    def report(self):
        print(self. get_report())

    def get_dir(self, f):
        """Get facing direction number by given facing string."""        
        ff = f.upper()
        for d, facing in self.dict_dir.items():
            if (facing == ff):
                dir = int(d)
                break
        return dir

    def place(self, x=0, y=0, f="NORTH"):
        """
        Setting a new position and direction for robot. 
        Robot will take new position and direction only when all parameters are correct.
        """
        allow_update = False
        if(x >= 0 and x < self.dim_x):            
            allow_update = True
        else:
            print("Position setting X = {} is invalid! X value must within range [{}, {}].".format(x, 0, self.edge_x))
            return

        if(y >= 0 and y < self.dim_y):            
            allow_update = True
        else:
            print("Position setting Y = {} is invalid! Y value must within range [{}, {}].".format(y, 0, self.edge_y))
            return

        ff = f.upper()
        if (ff in self.dict_dir.values()):            
            allow_update = True
        else:
            print("{} is not a valid facing direction! Please input values: {}".format(f, self.dict_dir.values()))
            return
        
        if(allow_update):
            self.curr_x = x
            self.curr_y = y
            self.curr_dir = self.get_dir(f)

    def do_move(self):
        ## Direction facing NORTH
        if (self.curr_dir == 0):
            self.curr_y = self.curr_y + 1        
        ## Direction facing EAST
        elif (self.curr_dir == 1):
            self.curr_x = self.curr_x + 1        
        ## Direction facing SOUTH
        elif (self.curr_dir == 2):
            self.curr_y = self.curr_y - 1        
        ## Direction facing WEST
        elif (self.curr_dir == 3):
            self.curr_x = self.curr_x - 1

    def allow_move(self):
        if (
            ## current X < Edge_X and Robot facing EAST
            (self.curr_x < self.edge_x and self.curr_dir == 1) or
            ## current X > 0 and Robot facing WEST
            (self.curr_x > 0 and self.curr_dir == 3) or
            ## current Y < Edge_Y and Robot facing NORTH
            (self.curr_y < self.edge_y and self.curr_dir == 0) or
            ## current Y > 0 and Robot facing SOUTH
            (self.curr_y > 0 and self.curr_dir == 2)
        ):
            can_move = True
        else:
            can_move = False

        return can_move

    def turn_left(self):
        if(self.curr_dir > 0):
            self.curr_dir = self.curr_dir - 1
        else:
            self.curr_dir = 3

    def turn_right(self):
        if(self.curr_dir < 3):
            self.curr_dir = self.curr_dir + 1
        else:
            self.curr_dir = 0

    def move(self):
        if self.allow_move():
            self.do_move()
        else:
            ## Surpress error message when file processing mode.
            if(not self.b_cmd_mode):
                print ("Robot at edge! Ignore move.")

    def left(self):
        self.turn_left()
    
    def right(self):
        self.turn_right()

    def process_command_file(self, cmd_filename):
        """Process content in a command file by given a filename."""
        self.b_cmd_mode = True
        beginning_flag = True        
        with open(cmd_filename, "r") as file_handler:
            for cmd_line in file_handler:
                cmd = cmd_line.strip()
                cmd = cmd.lower()

                # Ignore input line start with '#' as comment.
                if(not cmd.startswith("#")):
                    if(beginning_flag and ("place" not in cmd)):
                        ## Skip other commands until 1st place found.
                        continue
                    else:
                        beginning_flag = False
                        self.process_command(cmd)
        
    def process_command(self, cmd_line):
        """Process command line obtain from file."""        
        ## Process PLACE command
        if ("place" in cmd_line):            
            e = cmd_line.split()
            p = e[1].split(",")
            self.place(int(p[0]), int(p[1]), p[2])
        elif ("move" in cmd_line):
            self.move()
        elif ("left" in cmd_line):
            self.left()
        elif ("right" in cmd_line):
            self.right()
        elif ("report" in cmd_line):
            self.report()
        else:
            print("Command : {} not recognize! Ignoring ...".format(cmd_line))


############################################################################################################
## Function Defination
############################################################################################################
def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"chi:",["ifile=","command"])

    except getopt.GetoptError:
        print ('rea_robot.py -i <command file> | -c : Command line interface | -h : Help')
        sys.exit(2)

    ## Initiate ReaToyRobot.
    rr = ReaRobot()

    for opt, arg in opts:
        if opt == '-h':
            print ('Help - Rea Toy Robot ver 1.0.0')            
            print ('Usage: rea_robot.py -i <command file>')
            print ('To enter command line mode: rea_robot.py -c')
            sys.exit()

        elif opt in ("-i", "--ifile"):
            inputfile = arg
            
            ## Output information 
            print ('Input command file : {}\n\n'.format(inputfile))

            ## Get robot to process command file.
            rr.process_command_file(inputfile)
            
            ## Get robot to report itself after processing command file.
            rr.report_yourself()

            sys.exit()

        elif opt in ("-c", "--command"):
            print ("Rea Toy Robot in Command Line Mode ...\n")

            shell = rea_robot_terminal()
            shell.register_rea_robot(rr)
            shell.prompt = "Rea-Robot >> "
            shell.cmdloop()

            sys.exit()
    
############################################################################################################
## Main program started.
############################################################################################################
## Clear console screen for operations
os.system('cls')

if __name__ == "__main__":
   main(sys.argv[1:])

