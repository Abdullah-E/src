#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class node:
    def __init__(self):
        rospy.init_node('goto_goal', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/odom', Odometry, self.callback)
        
        self.pose = Odometry()
        self.orientation_list = []
        self.msg = Twist()
        self.rate = rospy.Rate(10)
        
        def callback(self, msg):
            self.pose = msg
            print(self.pose)            