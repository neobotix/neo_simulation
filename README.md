# ROS simulation for Neobotix mobile robots

This simulation package provides a quick and easy way to try out the autonomous mobile robots from Neobotix. It comes with the most commonly used configuration but is open for any kind of modification.

![neo_simulation](http://www.neobotix-roboter.de/fileadmin/files/downloads/ROS-extern/neo_simulation_mpo_500.png)

Neobotix offers a wide range of mobile robots for different applications:
* [MP-400](http://www.neobotix-robots.com/mobile-robot-mp-400.html): Small and cost-saving robot with differential drive for both industrial transport applications and basic research.
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

## Parameters to be set before the bringing up the robot in gazebo

1. In the **.bashrc** file

      1.1 **ROBOT and MAP_NAME**
  
   -  open bashrc file by commanding in the terminal ```sudo gedit ~/.bashrc``` and add the following lines:

       export ROBOT = mpo_500

       export MAP_NAME = env2map

2. In the **simulation.launch** file

      2.1 **robotname**
  
   -  set the name of the robot you wish to simulate in gazebo. Available robot models are mpo_500 and mmo_500.

      [Example]: If you opt to simulate the robot mpo_500:

      Change the *value* of the argument *robotname* to **mpo_500**.

      ```arg name="robotname" value="mpo_500"```

     2.2 **robotworld**
  
   - set the world in which the robot is to be simulated.

      [Example]: If you opt to simulate the robot in different world:

      Change the *value* of the argument *robotworld* to **construction_barrel.world**.

      ```arg name="robotworld" value="empty.world"```
      
    2.3  **rviz**

    - To visualize the robot in *rviz* set the value of the argument *rviz* to **true** else **false**.
    
      ```arg name="rviz" value="true"```
   
     2.4  **scanunifier**

    - Scan Unifier Node can unify any number of given input laser scans.
    
    - To launch the scan unifier node set the value of the arguement *scanunifier* to **true** else **false**.
    
      ```arg name="scanunifier" value="true"```
      
      __NOTE__: To use scan unifier node a package called *cob_scan_unifier* must be downloaded from the metapackage neo_driver (https://github.com/neobotix/neo_driver)
 
     2.5  **gmapping**

    - To launch the slam_gmapping node to create a map set the argument *gmappping* to **true** else **false**.
    - Before changing the *arg gmapping* set the argument of *amcl* and *navigation* to false.
    
      ```arg name="gmapping" value="false"```
      
     2.6  **amcl**
    
    - To launch the amcl node for localization of the robot set the argument *amcl* to **true** else **false**.
     
      ```arg name="amcl" value="false"```
      
     2.7  **navigation**

     - To launch the move_base node for navigating the robot to reach the desired location set the argument *navigation* to     **true** else **false**.
     
        ```arg name="navigation" value="true"```
     
     2.8  **localplanner**

    - With this parameter suitable local planner for the robot can be selected. Available local planners are Teb, DWA, EBand, Trajectory.
    
    - To set the local planner as Teb
    
       ```arg name="localplanner" value="teb"```
    
## Launch file

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`


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
   
