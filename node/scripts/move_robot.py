#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy
import time

def callback(data):
  try:
    cv_image = bridge.imgmsg_to_cv2(data, "mono8")
  except CvBridgeError as e:
    print(e)
  img=numpy.asarray(cv_image)

  threshold = 150
  # cv2.destroyAllWindows()
  # cv2.imshow('img', img)
  # cv2.waitKey(0)
  sum = 0
  count = 0
  previous_angular = 0
  for i in range(len(img[750,:])):
    if img[750,i] < threshold:
      sum += i
      count += 1

  if count == 0:
    move.linear.x = 0
    move.angular.z = previous_angular
  else:
    move.linear.x = 0.3
    previous_angular = -0.01 * (sum / count - 400)
    move.angular.z = previous_angular
    pub.publish(move)


rospy.init_node('move_robot')
rospy.Subscriber("/robot/camera/image_raw", Image, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move = Twist()
move.linear.x = 0.3
bridge = CvBridge()
rospy.spin()