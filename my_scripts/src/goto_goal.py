#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist, Point, Quaternion, Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

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
    
    def move2goal(self):
        goal_pose = Pose()
        goal_pose.x = 
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
        while not rospy.is_shutdown():
            x.print_pose()
    except rospy.ROSInterruptException:
        pass
        