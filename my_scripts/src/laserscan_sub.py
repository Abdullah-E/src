#!/usr/bin/env python2

import rospy
from sensor_msgs.msg import LaserScan

class laserDataNode:
    def __init__(self):
        rospy.init_node('laser_subscriber', anonymous=True)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
        self.laser_data = LaserScan()    
        self.rate = rospy.Rate(10)
    
    def callback(self, msg):
        self.laser_data = msg
    def print_data(self):
        print(self.laser_data)
        self.rate.sleep()
    
if __name__ == "__main__":
    try:
        n = laserDataNode()
        while not rospy.is_shutdown():
            n.print_data()
    except rospy.ROSInterruptException:
        pass
        
    