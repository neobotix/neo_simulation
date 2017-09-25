# neo_simulation
Package to simulate Neobotix robots 

- This package contains robot description of Neobotix robots, launch file to simulate the robot in Gazebo and Worlds for simulating the robot in Gazebo.


## Parameters to be set before the bringing up the robot in gazebo 

1. **robotname**
- set the name of the robot you wish to simulate in gazebo.
[__Example__]: If you opt to simulate the robot mpo_500, in the **simulation.launch** file:
Change the default name to mpo_500 in the argument **robotname
<arg name="robotname" default="mpo_500"/>

2. **robotworld**
- set the world in which the robot is to be simulated.
[__Example__]: If you opt to simulate the robot in different world, in the **simulation.launch** file:
Change the default name to ****.world in the argument **robotworld
<arg name="robotworld" default="empty.world"/>

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
