# ROS simulation for Neobotix mobile robots

This simulation package provides a quick and easy way to try out the autonomous mobile robots from Neobotix. It comes with the most commonly used configuration but is open for any kind of modification.

![neo_simulation](http://www.neobotix-roboter.de/fileadmin/files/downloads/ROS-extern/neo_simulation_mpo_500.png)

Neobotix offers a wide range of mobile robots for different applications:
* [MP-400](http://www.neobotix-robots.com/mobile-robot-mp-400.html): Small and cost-saving robot with differential drive for both industrial transport applications and research.
* [MP-500](https://www.neobotix-robots.com/mobile-robot-mp-500.html): Compact, industrial grade robot for material flow and intralogistics.
Very good system for robotics research when equipped with a robot arm.
* [MPO-500](http://www.neobotix-robots.com/mecanum-robot-mpo-500.html): Omnidirectional robot with Mecanum wheels for all kinds of service robotics research
* [MPO-700](http://www.neobotix-robots.com/omnidirectional-robot-mpo-700.html): Omnidirectional robot with Omni-Drive-Modules, offering very high payload and smooth movements. Great for both research and demanding industrial applications.

# Contact information

For more information please visit our website at www.neobotix-robots.com. 
If you have any questions, just get in touch with us:
* General information: http://www.neobotix-robots.com/company-contact.html
* ROS related questions: ros@neobotix.de

# neo_simulation

## Instructions to Download the Package

1. First step is to create a catkin workspace

   Follow this link to create a workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. Next step is to clone the neo_simulation repository to the source folder of the created workspace(catkin_ws).

   `$ cd catkin_ws/src`
   
   `$ git clone https://github.com/neobotix/neo_simulation.git`
   
   once cloned go back to catkin_ws directory and run:
   
    `$ catkin_make`
   
    `$ source devel/setup.bash`

3. Now we need to add the path of our custom gazebo models into the bashrc
      
    i. In your command line terminal

        $ gedit ~/.bashrc

    ii. Add this to your bashrc

        $ export GAZEBO_MODEL_PATH=/(Path to your workspace)/src/neo_simulation/models:$GAZEBO_MODEL_PATH
    
4. Download additional Gazebo Models from http://data.nvision2.eecs.yorku.ca/3DGEMS/

 ## Additional Packages that are required for the simulation

  1. Teleoperation

    $ sudo apt-get install ros-kinetic-teleop-twist-keyboard

  2. Control package 

    $ sudo apt-get install ros-kinetic-ros-control

  3. Navigation

    $ sudo apt-get install ros-kinetic-navigation

  3.1 Local Planner

    $ sudo apt-get install ros-kinetic-eband-local-planner

  3.2 Localization

    $ sudo apt-get install ros-kinetic-openslam-gmapping
    $ sudo apt-get install ros-kinetic-amcl

  4. Scan Unifier (Just the folder cob_scan_unifier)

    $ git clone https://github.com/neobotix/neo_driver.git
    
## Launch a mobile Robot

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`

### Parameters

| Parameter | Description | Options |
| --- | --- | --- |
| robot_type | robot type used in simulation | mpo_500, mmo_500, mpo_700 |
| robot_world | name of the .world file located in folder "worlds"  | neo_track1, neo_track2 |
| rviz | indicates if rviz should be started with the simulation  | true, false |
| autonomous_navigation | indicates if move base and gmapping or amcl should be started with the simulation  | true, false |

## Moving obstacles

For neo_track2 world, there is a ready made python script for moving obstacles. 

After launching the simulation for the mobile robot, run the following line in the command line window.

    $ rosrun neo_simulation models_spawn.py

## Topics

1. **/cmd_vel**

    - Plugin name: Planar Move *(geometry_msgs/twist)*

   __NOTE__: With this the robot can move in all directions and also able rotate along the Z-direction.


2. **/sick_s300_laser/back/scan**  *(sensor_msgs/LaserScan)*

   * Frame name: sick_s300_laser_back_link
   
   * Plugin name: GPU Laser
   
   __NOTE__: Laser scan covers an angle of 270 degrees

3. **/sick_s300_laser/front/scan** *(sensor_msgs/LaserScan)*

   * Frame name: sick_s300_laser_front_link

   * Plugin name: GPU Laser

   __NOTE__: Laser scan covers an angle of 270 degrees
   
4. **map** *(nav_msgs/OccupancyGrid)*

   __NOTE__: This topic publishes the data of the map.

5. **amcl_pose** *(geometry_msgs/PoseWithCovarianceStamped)*

   __NOTE__: This topic gives the estimated pose of the robot on map.
   
6. **tf** *(tf2_msgs/TFMessage)*

   __NOTE__: This topic publishes transform from /odom to /map.
   
7. **particle cloud** *(geometry_msgs/PoseArray)*

   __NOTE__: This topic publishes a set of pose estimates.
   
