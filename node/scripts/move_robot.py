#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy


def callback(data):
  try:
    cv_image = bridge.imgmsg_to_cv2(data, "mono8")
  except CvBridgeError as e:
    print(e)
  img=numpy.asarray(cv_image)

  move.linear.x = 0.5
  move.angular.z = 0.5
  pub.publish(move)
  print("Test")


rospy.init_node('move_robot')
rospy.Subscriber("/robot/camera/image_raw", Image, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
bridge = CvBridge()
rospy.spin()