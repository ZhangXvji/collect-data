#!/usr/bin/env python

import get_ecparm_raw
import get_imu_raw
import rospy

if __name__ == '__main__':
    rospy.init_node('get_data_raw', anonymous=True)
    
    rosbag_path = '/home/ztr/ttt/bag/output_2023-08-15-14-16-18.bag'  # Replace with the actual path
    imu_csv_path = './p1/p1_imu_raw.csv'  # Replace with the desired output CSV file path
    motor_csv_path = './p1/p1_motor_raw.csv'  # Replace with the desired output CSV file path
    joystick_csv_path = './p1/p1_joystick_raw.csv'  # Replace with the desired output CSV file path
    sensor_csv_path = './p1/p1_sensor_raw.csv'  # Replace with the desired output CSV file path

    get_imu_raw.imu_to_csv(rosbag_path, imu_csv_path)
    print('imu conversion complete.\n')
    get_ecparm_raw.motor_to_csv(rosbag_path, motor_csv_path)
    print('motor conversion complete.\n')
    get_ecparm_raw.joystick_to_csv(rosbag_path, joystick_csv_path)
    print('joystick conversion complete.\n')
    get_ecparm_raw.sensor_to_csv(rosbag_path, sensor_csv_path)
    print('sensor conversion complete.\n')

    print('good luck conversion complete.\n')