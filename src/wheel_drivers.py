#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

class CMD_Class():
    command = Twist()
    def __init__(self):
        self.subscriber = rospy.Subscriber("/cmd_vel", Twist, self.callback)

    def callback(self, message):
        self.command = message

    def start(self):
        return self.command

def main():
    # Define to topic names to publish to
    front_left_wheel_topic = "/security_rover/joint3_velocity_controller/command"
    front_right_wheel_topic = "/security_rover/joint4_velocity_controller/command"

    # Declare the publishers
    rover_publisher_FL = rospy.Publisher(front_left_wheel_topic, Float64, queue_size=10)
    rover_publisher_FR = rospy.Publisher(front_right_wheel_topic, Float64, queue_size=10)

    cmd_class = CMD_Class()
    rospy.init_node('wheel_drivers', anonymous=True)

    while not rospy.is_shutdown():
        rates = cmd_class.start()
        xLinRate = rates.linear.x
        zAngRate = rates.angular.z

        while abs(zAngRate) > 0.05:
            rates = cmd_class.start()
            zAngRate = rates.angular.z
            if zAngRate < 0:
                rover_publisher_FL.publish(1.5)
                rover_publisher_FR.publish(-1.5)
            else:
                rover_publisher_FL.publish(-1.5)
                rover_publisher_FR.publish(1.5)

        print("done turning")
        rover_publisher_FL.publish(0)
        rover_publisher_FR.publish(0)

        while abs(xLinRate) > 0.05:
            rates = cmd_class.start()
            xLinRate = rates.linear.x
            rover_publisher_FL.publish(3)
            rover_publisher_FR.publish(3)

        print("done moving")
        rover_publisher_FL.publish(0)
        rover_publisher_FR.publish(0)

if __name__=='__main__':
    
    main()