# ROS simulation for Neobotix mobile robots

This simulation package provides a quick and easy way to try out the autonomous mobile robots from Neobotix. It comes with the most commonly used configuration but is open for any kind of modification.

![neo_simulation](http://www.neobotix-roboter.de/fileadmin/files/downloads/ROS-extern/neo_simulation_mpo_500.png)

Neobotix offers a wide range of mobile robots for different applications:
* **MP-400**: Small and cost-saving robot with differential drive for both industrial transport applications and basic research.
* **MPO-500**: Omnidirectional robot with Mecanum wheels for all kinds of service robotics research
* **MPO-700**: Omnidirectional robot with Omni-Drive-Modules, offering very high payload and smooth movements. Great for both research and demanding industrial applications.

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

In the **simulation.launch** file

1. **robotname**
   - set the name of the robot you wish to simulate in gazebo.

      [Example]: If you opt to simulate the robot mpo_500:

      Change the *value* of the argument *robotname* to **mpo_500**.

      ```arg name="robotname" value="mpo_500"```

2. **robotworld**
   - set the world in which the robot is to be simulated.

      [Example]: If you opt to simulate the robot in different world:

      Change the *value* of the argument *robotworld* to **construction_barrel.world**. 

      ```arg name="robotworld" value="empty.world"```
      
3.  **rviz**

    - To visualize the robot in *rviz* set the value of the argument *rviz* to **true** else **false**.
    
      ```arg name="rviz" value="true"```
   
4.  **scanunifier**

    - Scan Unifier Node can unify any number of given input laser scans.
    
    - To launch the scan unifier node set the value of the arguement *scanunifier* to **true** else **false**.
    
      ```arg name="scanunifier" value="true"```
    

## Launch file

To simulate the robot in gazebo run:

`roslaunch neo_simulation simulation.launch`


## Published topics

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
   
4. **cob_scan_unifier/cob_scan_unifier/scan_unified** *(sensor_msgs/LaserScan)*

   * Node name: scan_unifier_node

