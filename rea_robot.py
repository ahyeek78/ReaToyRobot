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
    dim_x = 5
    dim_y = 5   

    ## Current Situation of Rea Toy Robot.
    curr_x = 0
    curr_y = 0

    ## 0:NORTH, 1:EAST, 2:SOUTH, 3:WEST
    ## Default to face NORTH.
    curr_dir = 0

    ## Define direction directionary.
    dict_dir = {'0':'NORTH', '1':'EAST', '2':'SOUTH', '3':'WEST'}

    ## Define available command list.
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

############################################################################################################
## Function Defination
############################################################################################################
def hello_rea_robot():
    return "Hello Rea Toy Robot!!!"

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print ('rea_robot.py -i <command file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Help - Rea Toy Robot ver 1.0.0')            
            print ('Usage: rea_robot.py -i <command file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    ## Output information 
    print ('Input command file : {}\n\n'.format(inputfile))

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

