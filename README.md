# PythonRobotics
[![Build Status](https://travis-ci.org/hasesuns/PythonRobotics.svg?branch=master)](https://travis-ci.org/hasesuns/PythonRobotics)

Python codes of Robotics for homework

# Requirements
- Python 3.x

# Install

1. Clone or download this repository "PythonRobotics".

2. Run the following code 

````
    $ pip install dist_for_homework/olkalmanflt-1.0-py3-none-any.whl
````
   or
````
    $ pip install dist_for_homework/olkalmanflt-1.0.tar.gz
````

# How to use

Run the following code
````
    $ olkalmanflt
````
Result of 1-older liner Kalman filter simulation is shown. 

````
-----------------------------------------------------------------
measured_pos    : [0.0, 1.2, 2.3, 4.1, 3.0, 6.1]
motionref_vel   :   [1.0, 1.0, 2.0, -1.0, 3.0, 3.0]
initial_mu      : 0.0
initial_sig     : 10000.0
measurement_sig : 4.0
motion_sig      : 2.0
-----------------------------------------------------------------
             | position |  sigma  |
update [ 0 ] :  0.000      3.998
predict[ 0 ] :  1.000      5.998
update [ 1 ] :  1.120      2.400
predict[ 1 ] :  2.120      4.400
update [ 2 ] :  2.214      2.095
predict[ 2 ] :  4.214      4.095
update [ 3 ] :  4.156      2.024
predict[ 3 ] :  3.156      4.024
update [ 4 ] :  3.078      2.006
predict[ 4 ] :  6.078      4.006
update [ 5 ] :  6.089      2.001
predict[ 5 ] :  9.089      4.001
````

The results when measurement_sig is 10 and motion_sig = 1 are shown below

````
    $ olkalmanflt 10 1
````

````
-----------------------------------------------------------------
measured_pos    : [0.0, 1.2, 2.3, 4.1, 3.0, 6.1]
motionref_vel   :   [1.0, 1.0, 2.0, -1.0, 3.0, 3.0]
initial_mu      : 0.0
initial_sig     : 10000.0
measurement_sig : 10.0
motion_sig      : 1.0
-----------------------------------------------------------------
             | position |  sigma  |
update [ 0 ] :  0.000      9.990
predict[ 0 ] :  1.000      10.990
update [ 1 ] :  1.105      5.236
predict[ 1 ] :  2.105      6.236
update [ 2 ] :  2.180      3.841
predict[ 2 ] :  4.180      4.841
update [ 3 ] :  4.154      3.262
predict[ 3 ] :  3.154      4.262
update [ 4 ] :  3.108      2.988
predict[ 4 ] :  6.108      3.988
update [ 5 ] :  6.106      2.851
predict[ 5 ] :  9.106      3.851
````

If you chose 0 as measurement_sig or motion_sig,
the value changes to small positive value(1e-7),
in order to avoid division by 0.



# Author
Akiyuki Hasegawa ([@has_eeic](https://twitter.com/has_eeic))

# Lisence
MIT
