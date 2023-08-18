#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
from ecparm.msg import ECParm
from ecparm.msg import Motor
from ecparm.msg import Joystick
from ecparm.msg import Sensor

def publish_ecparm(speed1, speed2, joystick_x, joystick_y, sensor_1, sensor_2, sensor_3, sensor_4):
    rospy.init_node('ecparm_publisher', anonymous=True)
    pub = rospy.Publisher('/ecparm', ECParm, queue_size=10)
    ecparm_msg = ECParm()
        
    ecparm_msg.header = Header()
    ecparm_msg.header.stamp = rospy.Time.now()
    ecparm_msg.header.frame_id = "ecparm_link"
        
    ecparm_msg.motor = Motor()
    ecparm_msg.motor.speed1 = speed1
    ecparm_msg.motor.speed2 = speed2
        
    ecparm_msg.joystick = Joystick()
    ecparm_msg.joystick.joystick_x = joystick_x
    ecparm_msg.joystick.joystick_y = joystick_y
        
    ecparm_msg.sensor = Sensor()
    ecparm_msg.sensor.sensor_1 = sensor_1
    ecparm_msg.sensor.sensor_2 = sensor_2
    ecparm_msg.sensor.sensor_3 = sensor_3
    ecparm_msg.sensor.sensor_4 = sensor_4
        
    pub.publish(ecparm_msg)


