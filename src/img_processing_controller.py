#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np 

class BallTracker(object):

    def __init__(self):
        self.image_sub = rospy.Subscriber("/security_rover/camera1/image_raw", Image, self.camera_callback)
        self.bridge_object=CvBridge()
        self.hsv_pub = rospy.Publisher("hsv_img", Image, queue_size=10)
        
    def camera_callback(self,data):
   
        rate = rospy.Rate(10)
        try:
            # We select bgr8 because its the OpenCV encoding by default
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            print(e)

        height, width, channels = cv_image.shape
        descentre = 160
        rows_to_watch = 60
        crop_img = cv_image[(height)/2+descentre:(height)/2+(descentre+rows_to_watch)][1:width]
        hsv = cv2.cvtColor(cv_image,cv2.COLOR_BGR2HSV)

        hsv_img = self.bridge_object.cv2_to_imgmsg(hsv, encoding="bgr8")
        upper_yellow=np.array([70,48,255])
        lower_yellow=np.array([50,28,245])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask_img = self.bridge_object.cv2_to_imgmsg(mask, encoding="mono8")
        #a = cv2.moments(mask, False)
        #try:
         #   cx,cy=a['m10']/a['m00'], a['m01']/a['m00']
        #except ZeroDivisionError:
         #   cy, cx=height/2, width/2
        self.hsv_pub.publish(hsv_img)
        rate.sleep()

def main():

    ball_tracker_object=BallTracker()
    rospy.init_node('Ball_tracking_node', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting Down")

if __name__=='__main__':
    main()