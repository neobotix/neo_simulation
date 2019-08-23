#!/usr/bin/env python

import rospy, tf
from gazebo_msgs.srv import SpawnModel
import time
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelState, ModelStates
import os
from os.path import expanduser


home = expanduser("~")
path = home + '/.gazebo/models/construction_cone/model.sdf'
speed = 1.3
class Moving():
	def __init__(self, model_name, Spawning1, y_pose, x_pose):
		self.pub_model = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
		self.model_name = model_name
		self.rate = rospy.Rate(10)
		self.x_model_pose = x_pose
		self.y_model_pose =	y_pose
		self.Spawning1 = Spawning1 
		self.flag = 0
		self.flag1 = 0
		self.flag2 = 0
		self.flag3 = 0
		self.flag4 = 0
		self.flag5 = 0


	def spawning(self,):
		with open(path) as f:
			product_xml = f.read()
		item_name   =   "product_{0}_0".format(0)
		print("Spawning model:%s", self.model_name)
		item_pose   =   Pose(Point(x=self.x_model_pose, y=self.y_model_pose,    z=0.0),   Quaternion(0.,0.,0.0,0))
		self.Spawning1(self.model_name, product_xml, "", item_pose, "world")

	def moving_tile_y_long_path(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_y = model.pose[0].position.y
		for i in range(len(model.name)):
			if model.name[i] == self.model_name and round(model.pose[i].position.y) < round(self.y_model_pose)+5.50 and self.flag == 0:
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = speed
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.y) == 3.0:
				self.flag1 = 1
				self.flag = 1

	def moving_tile_x_long_path(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_x = model.pose[0].position.x
		for i in range(len(model.name)):
			if model.name[i] == self.model_name and self.flag1==1 and self.flag == 1 and round(model.pose[i].position.x) > round(self.x_model_pose)-6.:
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.x = -speed
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.x) <= -3.0:
				self.flag1 = 0
				self.flag2 = 1
	
	def moving_tile_y_long_path1(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_y = model.pose[0].position.y
		for i in range(len(model.name)):
			if model.name[i] == self.model_name and self.flag1==0 and self.flag2 == 1 and round(model.pose[i].position.y) > round(self.y_model_pose):			
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = -speed
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.y) <= -3.0:
				self.flag3 = 1
				self.flag2 = 0

	def moving_tile_x_long_path1(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_x = model.pose[0].position.x

		for i in range(len(model.name)):
			if model.name[i] == self.model_name and self.flag==1 and self.flag1 == 0 and self.flag2==0 and self.flag3 == 1 and round(model.pose[i].position.x) < round(self.x_model_pose)+3	:

				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.x = speed
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
				
			elif model.name[i] == self.model_name and round(model.pose[i].position.x) >= 4.0:
				print("1")
				self.flag4 = 1
				self.flag3 = 0		

	def moving_tile_y_long_path2(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_y = model.pose[0].position.y
		for i in range(len(model.name)):
			if model.name[i] == self.model_name and self.flag==1 and self.flag1 == 0 and self.flag2==0 and self.flag3 == 0 and self.flag4==1 and round(model.pose[i].position.y) < round(self.y_model_pose)+5.50:
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = speed
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.y) == 3.0:
				self.flag5 = 1
				self.flag4 = 0


def main():
	rospy.init_node('moving_obstacle')
	Spawning1 = rospy.ServiceProxy("gazebo/spawn_sdf_model", SpawnModel)
	rospy.wait_for_service("gazebo/spawn_sdf_model")
	moving = Moving("construction_barrel", Spawning1, -3.0, 2.0)
	moving.spawning()
	while not rospy.is_shutdown():
		moving.moving_tile_y_long_path()
		moving.moving_tile_x_long_path()
		moving.moving_tile_y_long_path1()
		moving.moving_tile_x_long_path1()
		moving.moving_tile_y_long_path2()
		# moving.moving_tile_y_long_path3()


if __name__ == '__main__':
	main()
