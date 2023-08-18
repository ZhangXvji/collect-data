#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from rosbag import Bag

# 输入的ROS bag文件和输出的视频文件名
input_bag_file = '/home/ztr/ttt/bag/lidar2camera0.bag'
output_video_file = './p1/p1_video_raw.mp4'

# 初始化ROS节点
rospy.init_node('rosbag_to_video', anonymous=True)

# 设置cv_bridge
cv_bridge = CvBridge()

# 设置视频编码参数
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 或者使用其他支持的编码器
frame_rate = 30
frame_size = (640, 480)  # 根据实际情况设置

# 创建VideoWriter对象
video_writer = cv2.VideoWriter(output_video_file, fourcc, frame_rate, frame_size)

# 读取ROS bag中的图像数据并写入视频文件
with Bag(input_bag_file, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/usb_cam/image_raw']):
        cv_image = cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        video_writer.write(cv_image)

# 释放资源
video_writer.release()

print("Conversion complete!")
