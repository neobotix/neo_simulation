# neo_simulation
Package to simulate Neobotix robots 

**Instructions to Download the Package**

1. First step is to create a catkin workspace

   Follow this link to create a workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. Next step is to clone the neo_simulation repository to the source folder of the created workspace(catkin_ws).

   `$ cd catkin_ws/src`
   
   `$ git clone https://github.com/neobotix/neo_simulation.git`
   
   once cloned go back to catkin_ws directory and run:
   
    `$ catkin_make`
   
    `$ source devel/setup.bash`

## Parameters to be set before the bringing up the robot in gazebo 

1. **robotname**
- set the name of the robot you wish to simulate in gazebo.

  [Example]: If you opt to simulate the robot mpo_500, in the *simulation.launch* file:

  Change the default name of the argument *robotname* to mpo_500.

  ```arg name="robotname" default="mpo_500"```

2. **robotworld**
- set the world in which the robot is to be simulated.

  [Example]: If you opt to simulate the robot in different world, in the *simulation.launch* file:

  Change the default name in the argument *robotworld* to construction_barrel.world. 

  ```arg name="robotworld" default="empty.world"```

## Launch file

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`


## Published topics

1. **/cmd_vel**

    - Plugin name: Planar Move *(geometry_msgs/twist)*

   __NOTE__: With this the robot can move in all directions and also able rotate along the Z-direction.


2. **/sick_s300_laser/back/scan**  *(sensor_msgs/LaserScan)*

   **Frame name**: sick_s300_laser_back_link

3. **/sick_s300_laser/front/scan** *(sensor_msgs/LaserScan)*

   **Frame name**: sick_s300_laser_front_link

     - Plugin name: GPU Laser

   __NOTE__: Laser scan cover an angle of 270 degrees


http://www.neobotix-robots.com
