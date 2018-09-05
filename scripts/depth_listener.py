#!/usr/bin/env python


import rospy
import cv2
import time

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

object_pixel_x = 300
object_pixel_y = 300

global rgb_topic
global depth_topic

bridge = CvBridge()

def rgb(data):

    try:
        # Convert your ROS Image message to OpenCV2
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        
	time.sleep(1)
	cv2.imwrite('catkin_ws/src/beginner_tutorials/camera_image.jpeg', cv_image)
	#cv2.imshow("hey", cv_image)
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
    	print("RGB image saved")
	
	rgb_topic.unregister()

def depth(data):

    try:
        # Convert your ROS Image message to OpenCV2
        cv_image = bridge.imgmsg_to_cv2(data, "16UC1")
        
	time.sleep(1)
	cv2.imwrite('catkin_ws/src/beginner_tutorials/depth_image.png', cv_image)
	
    except CvBridgeError, e:
        print(e)
    else:
        # Save your OpenCV2 image as a jpeg 
    	print("Depth image saved")
	#(rows,cols,channels) = cv_image.shape
	#print rows
	#print cols
	print "Depth reading (",object_pixel_x, ", ", object_pixel_y,"): ",cv_image[object_pixel_x,object_pixel_y]
	depth_topic.unregister()	



if __name__ == '__main__':
   
    rospy.init_node('depth_listener', anonymous=True)

    rgb_topic = rospy.Subscriber('/camera/rgb/image_raw', Image, rgb)

    ############ Do object recognition stuff here ###############################
    time.sleep(3) # to simulate code duration 

    depth_topic = rospy.Subscriber('/camera/depth/image_raw', Image, depth)

    # spin() simply keeps python from exiting until this node is stopped
    time.sleep(3)
    






