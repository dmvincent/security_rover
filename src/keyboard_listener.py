#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

def callback(message):

    #x=0
    #z=0
    x=message.linear.x
    z=message.angular.z
    gimbal_publisher_pan.publish(0.0)

    # Output to wheel motors depending on input from keyboard
    if x == 0.5:
        rover_publisher_FL.publish(3)
        rover_publisher_FR.publish(3)

        print("move forward")
    elif x == -0.5:
        rover_publisher_FL.publish(-3)
        rover_publisher_FR.publish(-3)

        print("move backward")
    elif z == 1:
        rover_publisher_FL.publish(-1.5)
        rover_publisher_FR.publish(1.5)

        print("turn left")
    elif z == -1:
        rover_publisher_FL.publish(1.5)
        rover_publisher_FR.publish(-1.5)
        print("turn right")
 
def listener():

    # Initialize the Node
    rospy.init_node('keyboard_listener', anonymous=True)

    # Declare the subscriber
    keyboard_subscriber = rospy.Subscriber("/security_rover/cmd_vel", Twist, callback)
    
    rate=rospy.Rate(10.0)
    rate.sleep()

if __name__=='__main__':

    # Define to topic names to publish to
    front_left_wheel_topic = "/security_rover/joint3_velocity_controller/command"
    front_right_wheel_topic = "/security_rover/joint4_velocity_controller/command"
    pan_motor_topic = "/security_rover/joint1_position_controller/command"

    # Declare the publishers
    rover_publisher_FL = rospy.Publisher(front_left_wheel_topic, Float64, queue_size=10)
    rover_publisher_FR = rospy.Publisher(front_right_wheel_topic, Float64, queue_size=10)
    gimbal_publisher_pan = rospy.Publisher(pan_motor_topic, Float64, queue_size=10)
    

    # Call the listener function and spin
    listener() 
    rospy.spin()