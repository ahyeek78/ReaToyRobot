# Rea Toy Robot

## Command To Run Rea Toy Robot
-------------------------------
- To execute the **rea_robot** by using command file.
```
python rea_robot.py -i <command.txt>
```
For example:
```
python rea_robot.py -i cmd_test_1.txt
python rea_robot.py -i cmd_test_2.txt
python rea_robot.py -i cmd_test_3.txt
```

- To execute the **rea_robot** by using command line.
```
python rea_robot.py [-c | --command]
```

For example:
```
python rea_robot.py -c
```

Execution example:
```
Rea Toy Robot in Command Line Mode ...

Hello, I am Rea Toy Robot !!! ...
Dimension setting - Witdth:5, Height:5
My current position at (0,0) facing NORTH.
Rea-Robot >> move
Rea-Robot >> move
Rea-Robot >> right
Rea-Robot >> move
Rea-Robot >> move
Rea-Robot >> report
2,2,EAST
Rea-Robot >> move
Rea-Robot >> report
3,2,EAST
Rea-Robot >> move
Rea-Robot >> left
Rea-Robot >> report
4,2,NORTH
Rea-Robot >> move
Rea-Robot >> report
4,3,NORTH
Rea-Robot >> move
Rea-Robot >> move
Robot at edge! Ignore move.
Rea-Robot >> move
Robot at edge! Ignore move.
Rea-Robot >> report
4,4,NORTH
Rea-Robot >> rught
*** Unknown syntax: rught
Rea-Robot >> right
Rea-Robot >> move
Robot at edge! Ignore move.
Rea-Robot >> move
Robot at edge! Ignore move.
Rea-Robot >> report
4,4,EAST
Rea-Robot >> exit
```

## Perform Sanity Test
Some test cases have been developed to test functions implemented in **rea_robot.py**  
Test cases can refer to **test-rea-robot.py**.

For example:
```
python test-rea-robot.py
```
