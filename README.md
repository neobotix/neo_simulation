# neo_simulation
Package to simulate Neobotix robots 

This package contains robot description of mpo_500, launch file to simulate the robot in Gazebo and Worlds for simulating the robot in Gazebo.


[Before the bringing up the robot in gazebo, parameters to be set are:]

## Parametrs
**robotname**
set the name of the robot you wish to simulate in gazebo.

**robotworld**
set the world in which the robot is to be simulated.

## Launch file

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`


## Published topics

**/cmd_vel**
Plugin name: Planar Move *(geometry_msgs/twist)

__NOTE__With this the robot can move in all directions and also able rotate along the Z-direction.


**/sick_s300_laser/back/scan**  *(sensor_msgs/LaserScan)*
**/sick_s300_laser/front/scan** *(sensor_msgs/LaserScan)*
plugin name: GPU Laser

__NOTE__Laser scan cover an angle of 270 degrees


[In order to merge the Front and Back Laser Scans]

Node: scan_unifier_node
---------------------

This node unifies the front and back laser scans

## Parameters
**input_scans** *(List of std::string)*
 The names of the scan topics to subscribe to as list of strings.
 
**loop_rate** *(double, default: 100.0 [hz])*
 The loop rate of the ros node.

## Published Topics
**scan_unified** *(sensor_msgs::LaserScan)* 
 Publishes the unified scans.

## Subscribed Topics
**input_scan_name** *(sensor_msgs::LaserScan)*
 The current scan message from the laser scanner with topic name specified via the parameter **input_scan_topics**

`rosrun cob_scan_unifier **************`
http://www.neobotix-robots.com
