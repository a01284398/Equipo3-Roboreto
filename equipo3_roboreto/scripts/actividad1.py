#!/usr/bin/env python

#TERMINAL1 CORRER EL GAZEBO (roslaunch puzzlebot_world puzzlebot_simple_world.launch)
#TERMINAL2 EL PROGRAMA (rosrun puzzlebot actividad1.py)

import rospy
import numpy as np 
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Float32

#declaramos el tiempo
vel= 0.5
wl=1
wr=1

if __name__ == '__main__':
    msg = Twist()
    cmd_vel= rospy.Publisher ("cmd_vel", Twist, queue_size=10) 
    rospy.init_node('controller')
    rate= rospy.Rate(10)

    
    while not rospy.is_shutdown():
	    wl=1.0
	    wr=1.0
        msg.linear.x=1.0
	    msg.angular.x=1.0
	    cmd_vel.publish(msg)   
        rate.sleep()
