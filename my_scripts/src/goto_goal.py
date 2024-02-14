#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist, Point, Quaternion, Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import pow, atan2, sqrt

class node:
    def __init__(self):
        rospy.init_node('goto_goal', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/odom', Odometry, self.callback)
        
        self.angles = {}
        self.angle_names = ['roll', 'pitch', 'yaw']
        
        self.odom = Odometry()
        self.position = Point()
        self.orient = Quaternion()
        self.orientation_list = []
        self.msg = Twist()
        self.rate = rospy.Rate(10)
        
    def callback(self, msg):
        self.odom = msg
        self.position = self.odom.pose.pose.position
        self.orient = self.odom.pose.pose.orientation
        euler_angs = euler_from_quaternion([self.orient.x, self.orient.y, self.orient.z, self.orient.w])
        for i, n in enumerate(self.angle_names):
            self.angles[n] = euler_angs[i]
    def euclidean_distance(self, pose):
        return sqrt(pow((pose.x - self.position.x), 2) + pow((pose.y - self.position.y), 2))
    def move2goal(self):
        goal_pose = Pose()
        goal_pose.position.x = float(input("Set your x goal: "))
        goal_pose.position.y = float(input("Set your y goal: "))

        vel_msg = Twist()
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        # fix heading:
        # curr_yaw = self.angles['yaw'] 
        
        
        goal_yaw = atan2(goal_pose.position.y-self.position.y, goal_pose.position.x- self.position.x)
        angle_err = goal_yaw-self.angles['yaw']
        while angle_err >= 0.005:
            vel_msg.angular.z = angle_err*0.2
            goal_yaw = atan2(goal_pose.position.y-self.position.y, goal_pose.position.x- self.position.x)
            angle_err = goal_yaw-self.angles['yaw']
            self.pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.angular.z = 0
        print("reached angle")
        
        dist_err = self.euclidean_distance(goal_pose.position)
        while dist_err >= 0.1:
            vel_msg.linear.x = 0.5*dist_err
            self.pub.publish(vel_msg)
            dist_err = self.euclidean_distance(goal_pose.position)
            self.rate.sleep()
        vel_msg.linear.x = 0
        self.pub.publish(vel_msg)
        print("reached goal")
        
        rospy.spin()
        
    def print_pose(self):
        # print("x: ", self.pose.pose.pose.position.x)
        # print(self.pose)
        # print(self.pose.pose.pose.position)
        print("postion:", self.position)
        print("orientation:", self.orient)
        print("angles:", self.angles)
        self.rate.sleep()
            
if __name__ == "__main__":
    try:
        x = node()
       
        x.move2goal()
    except rospy.ROSInterruptException:
        pass
        