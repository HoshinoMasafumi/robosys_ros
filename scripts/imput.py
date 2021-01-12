#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64

rospy.init_node('imput_number')
pub = rospy.Publisher('number', Float64, queue_size=1)

print("Enter the number you want to determine if it is a prime number.")

while not rospy.is_shutdown():
    num = input("imput:")
    num = float(num)
    pub.publish(num)
