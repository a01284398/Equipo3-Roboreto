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
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)

    rospy.init_node('controller')
    msg.linear.x = 0.5#
    rate=rospy.Rate(10)
    rate.sleep
    #tiempo=rospy.get_time()#

    while not rospy.is_shutdown():
        #print (tiempo)
        t=rospy.get_time() #-tiempo
        print('tiempo tiempo real:',t)
        if t < tiempoto:
            msg.linear.x=0.5
            
        elif t > tiempoto:
            msg.linear.x=0
            print ("acabo")
        print('tiempo final:',tiempoto)
        pub.publish(msg) #
        rate.sleep()#

     
#    pub = rospy.Publisher("c", String, queue_size=10)
#    rospy.init_node("controller")
#    rate=rospy.Rate(10)
#
#    while not rospy.is_shutdown():
#        hello_str = "hello world %s" % rospy.get_time()
#        pub.publish(hello_str)
#        rate.sleep()