#!/usr/bin/env python

import rospy
import rosbag
import csv

def motor_to_csv(rosbag_path, csv_path):
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['stamp', 'm1', 'm2'])

        with rosbag.Bag(rosbag_path, 'r') as bag:
            for topic, msg, timestamp in bag.read_messages(topics=['/ecparm']):
                row = [
                    msg.header.stamp,
                    msg.motor.speed1, msg.motor.speed2
                ]
                csv_writer.writerow(row)

def joystick_to_csv(rosbag_path, csv_path):
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['stamp', 'x', 'y'])

        with rosbag.Bag(rosbag_path, 'r') as bag:
            for topic, msg, timestamp in bag.read_messages(topics=['/ecparm']):
                row = [
                    msg.header.stamp,
                    msg.joystick.joystick_x, msg.joystick.joystick_y
                ]
                csv_writer.writerow(row)

def sensor_to_csv(rosbag_path, csv_path):
    with open(csv_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['stamp', 'f1', 'f2', 'f3', 'f4'])

        with rosbag.Bag(rosbag_path, 'r') as bag:
            for topic, msg, timestamp in bag.read_messages(topics=['/ecparm']):
                row = [
                    msg.header.stamp,
                    msg.sensor.sensor_1, msg.sensor.sensor_2, msg.sensor.sensor_3, msg.sensor.sensor_4
                ]
                csv_writer.writerow(row)
