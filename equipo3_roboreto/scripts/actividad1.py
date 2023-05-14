#!/usr/bin/env python

#TERMINAL1 CORRER EL GAZEBO (roslaunch puzzlebot_world puzzlebot_simple_world.launch)
#TERMINAL2 EL PROGRAMA (rosrun puzzlebot actividad1.py)

import rospy
import numpy as np 
from geometry_msgs.msg import Twist 

msg=Twist()

#declaramos el tiempo
vel= 0.5
dis= 2
tiempoto = dis/vel

if __name__ == '__main__':
    pub = rospy.Publisher("cmd_pwmL", Twist, queue_size=10)
    rospy.init_node('controller')
    rate= rospy.Rate(10)
    
    msg.linear.x=0.5

    while not rospy.is_shutdown():
        pub.publish(msg)    
        rate.sleep()
    
