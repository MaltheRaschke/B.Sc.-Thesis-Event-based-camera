#! /usr/bin/python
# Copyright (c) 2015, Rethink Robotics, Inc.

# Using this CvBridge Tutorial for converting
# ROS images to OpenCV2 images
# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

# Using this OpenCV2 tutorial for saving Images:
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
# Numpy for arrays
import numpy as np

# Instantiate CvBridge
bridge = CvBridge()


def image_callback(msg):
    global counter
    print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        # Change the color map of the image
        cv2_img[np.all(cv2_img == (255,255,255), axis=-1)] = (255,0,0)
        cv2_img[np.all(cv2_img == (0,0,0), axis=-1)] = (0,0,255)
        cv2_img[np.all(cv2_img == (128,128,128), axis=-1)] = (0,0,0)
        # Downscale image from 640x480 to 200x150
        scale_percent = 31.25 # percent of original size
        width = int(cv2_img.shape[1] * scale_percent / 100)
        height = int(cv2_img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(cv2_img, dim, interpolation = cv2.INTER_NEAREST)
    except CvBridgeError:
        print(e)
    else:
        counter += 1
        # Save your OpenCV2 image as a jpeg
        cv2.imwrite(f'/path/to/target/folder/accumulated_image_{counter}.png', cv2_img) # or instead of cv2_img uncompressed image, use "resized" for scaling_percent


def main():
    rospy.init_node('image_listener')
    # Define your image topic
    image_topic = "/accumulator/image"
    # Set up your subscriber and define its callback
    rospy.Subscriber(image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__ == '__main__':
    counter = 0
    main()
    