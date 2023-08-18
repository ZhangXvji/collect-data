#!/usr/bin/env python

import rospy
import rosbag
import csv

def imu_to_csv(rosbag_path, csv_path):
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['stamp', 'x', 'y', 'z', 'w', 'x1', 'y1', 'z1', 'x2', 'y2', 'z2'])

        with rosbag.Bag(rosbag_path, 'r') as bag:
            for topic, msg, timestamp in bag.read_messages(topics=['/imu']):
                row = [
                    msg.header.stamp,
                    msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w,
                    msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z,
                    msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z
                ]
                csv_writer.writerow(row)

