#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################################################################################################################
## Start Date: 19-Feb-2019
## Last Modified: 19-Feb-2019
## Version: 1.0
## 
## REA Robot Training Program
##
## Commnad Examples:
## python rea-robot.py --help
## python 
##
## Version Tracking
## Ver 1.0.0
## 18-Feb-2019      Start 1st skelaton.
## 19-Feb-2019      Develop ReaRobot class using Singleton design pattern.
## 20-Feb-2019      Develop basic functions and checking functions.
## 21-Feb-2019      Complete all movement function and edge checking condition.
#####################################################################################################################################################################

### Imports packages
import sys, getopt, os

############################################################################################################
## Global Variables
############################################################################################################


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
        for d, facing in self.dict_dir.items():
            if (facing == f):
                dir = int(d)
                break
        return dir

    def place(self, x=0, y=0, f="NORTH"):
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
            print ("Robot at edge! Ignore move.")

    def left(self):
        self.turn_left()
    
    def right(self):
        self.turn_right()


############################################################################################################
## Function Defination
############################################################################################################
def hello_rea_robot():
    return "Hello Rea Toy Robot!!!"

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"chi:",["ifile=","command"])
    except getopt.GetoptError:
        print ('rea_robot.py -i <command file>')
        sys.exit(2)
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
            sys.exit()

        elif opt in ("-c", "--command"):
            print ("Rea Toy Robot in Command Line Mode ...\n")
            sys.exit()
    
    ## Initiate ReaToyRobot.
    rr = ReaRobot()
    rr.report_yourself()

############################################################################################################
## Main program started.
############################################################################################################
## Clear console screen for operations
os.system('cls')

if __name__ == "__main__":
   main(sys.argv[1:])

