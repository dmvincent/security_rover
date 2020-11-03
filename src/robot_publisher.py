#!/usr/bin/env python

import rospy
import time
import tf 
from get_gazebo_model_pose import GazeboModel

def handle_turtle_pose(pose_msg, robot_name):
    br = tf.TransformBroadcaster()
    
    br.sendTransform((pose_msg.position.x,pose_msg.position.y,pose_msg.position.z),
                     (pose_msg.orientation.x,pose_msg.orientation.y,pose_msg.orientation.z,pose_msg.orientation.w),
                     rospy.Time.now(),
                     "base_link",
                     "odom")

def publisher_of_tf():
    
    rospy.init_node('publisher_of_tf_node', anonymous=True)
    robot_name_list = ["security_rover"]
    gazebo_model_object = GazeboModel(robot_name_list)
    
    
    for robot_name in robot_name_list:
        pose_now = gazebo_model_object.get_model_pose(robot_name)
    
    # Leave enough time to be sure the Gazebo Model logs have finished
    time.sleep(1)
    rospy.loginfo("Ready..Starting to Publish TF data now...")
    
    rate = rospy.Rate(200) # 200hz
    while not rospy.is_shutdown():
        for robot_name in robot_name_list:
            pose_now = gazebo_model_object.get_model_pose(robot_name)
            if not pose_now:
                print "The " + str(robot_name) + "'s Pose is not yet available...Please try again later"
            else:
                handle_turtle_pose(pose_now, robot_name)
        rate.sleep()
    

if __name__ == '__main__':
    try:
        publisher_of_tf()
    except rospy.ROSInterruptException:
        pass