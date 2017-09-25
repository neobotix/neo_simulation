# neo_simulation
Package to simulate Neobotix robots 

- This package contains robot description of mpo_500, launch file to simulate the robot in Gazebo and Worlds for simulating the robot in Gazebo.


## Parameters to be set before the bringing up the robot in gazebo 

1. **robotname**
- set the name of the robot you wish to simulate in gazebo.

2. **robotworld**
- set the world in which the robot is to be simulated.

## Launch file

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`


## Published topics

1. **/cmd_vel**

    - Plugin name: Planar Move *(geometry_msgs/twist)*

  __NOTE__: With this the robot can move in all directions and also able rotate along the Z-direction.


2. **/sick_s300_laser/back/scan**  *(sensor_msgs/LaserScan)*

3. **/sick_s300_laser/front/scan** *(sensor_msgs/LaserScan)*

     - Plugin name: GPU Laser

   __NOTE__: Laser scan cover an angle of 270 degrees


http://www.neobotix-robots.com
