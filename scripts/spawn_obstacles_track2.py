#!/usr/bin/env python

import rospy, tf
from gazebo_msgs.srv import SpawnModel
import time
from geometry_msgs.msg import *
from gazebo_msgs.msg import ModelState, ModelStates
import os
from os.path import expanduser


home = expanduser("~")
path = home + '/.gazebo/models/construction_barrel/model.sdf'

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
			if model.name[i] == self.model_name and round(model.pose[i].position.y) <= round(self.y_model_pose)+5.0 and self.flag == 0:
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = 1.3
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.y) != round(self.y_model_pose):
				self.flag = 1
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = -1.3
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif  round(model.pose[i].position.y) == round(self.y_model_pose):
				self.flag = 0

	def moving_tile_y_short_path(self):
		obstacle = ModelState()
		model = rospy.wait_for_message('gazebo/model_states', ModelStates)
		model_original_pose_y = model.pose[0].position.y
		for i in range(len(model.name)):
			if model.name[i] == self.model_name and round((model.pose[i].position.y),1) <= round(self.y_model_pose,1)+1.0 and self.flag1 == 0:
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = 0.8
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif model.name[i] == self.model_name and round(model.pose[i].position.y,1) != round(self.y_model_pose,1):
				self.flag1 = 1
				obstacle.model_name = self.model_name
				obstacle.pose = model.pose[i]
				obstacle.twist = Twist()
				obstacle.twist.linear.y = -0.8
				obstacle.twist.angular.z = 0
				self.pub_model.publish(obstacle)
			elif  round(model.pose[i].position.y,1) == round(self.y_model_pose,1):
				self.flag1 = 0

def main():
	rospy.init_node('moving_obstacle')
	rospy.loginfo("Here")
	Spawning1 = rospy.ServiceProxy("gazebo/spawn_sdf_model", SpawnModel)
	rospy.wait_for_service("gazebo/spawn_sdf_model")
	moving = Moving("construction_barrel", Spawning1, -17.13, 9.78)
	moving1 = Moving("construction_barrel_1", Spawning1, -16.33, -12.3)
	moving2 = Moving("construction_barrel_2", Spawning1, 0.1, -3.5)
	moving3 = Moving("construction_barrel_3", Spawning1, -27.1, -4.8)
	moving.spawning()
	moving1.spawning()
	moving2.spawning()
	moving3.spawning()
	while not rospy.is_shutdown():
		moving.moving_tile_y_long_path()
		moving1.moving_tile_y_long_path()
		moving2.moving_tile_y_short_path()
		moving3.moving_tile_y_short_path()


if __name__ == '__main__':
	main()

