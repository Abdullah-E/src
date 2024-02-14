#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Twist

class node:
    def __init__(self) -> None:
        rospy.init_node('circle_publisher', anonymous=True)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.msg = Twist()
    
    def publish(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            msg = Twist()
            msg.linear.x = 0.5
            msg.angular.z = 0.5
            self.pub.publish(msg)
            rate.sleep()
if __name__ == "__main__":
    
    n = node()
    n.publish()
    