#!/usr/bin/env python
import serial
import time
import rospy
import get_ecparm

# 设置串口参数
serial_port = '/dev/ttyACM0'  # 根据实际情况修改串口设备路径
baud_rate = 115200

# 打开串口
ser = serial.Serial(serial_port, baud_rate)
# 循环接收数据
while True:
  a = ser.read(1)
  if a[0] == 0xaa:
      data = ser.read(18)  # 假设要读取的数据长度为18字节
    # 进行数据处理
      if len(data) == 18 and data[0] == 0xff and data[17] == 0xaa:
        byte1 = data[0]  # 第1个字节
        byte2 = data[1]  # 第2个字节
        byte3 = data[2]  # 第3个字节
        byte4 = data[3]  # 第4个字节
        byte5 = data[4]  # 第5个字节
        byte6 = data[5]  # 第6个字节
        byte7 = data[6]  # 第7个字节
        byte8 = data[7]  # 第8个字节
        byte9 = data[8]  # 第9个字节
        byte10 = data[9]  # 第10个字节
        byte11 = data[10]  # 第11个字节
        byte12 = data[11]  # 第12个字节
        byte13 = data[12]  # 第13个字节
        byte14 = data[13]  # 第14个字节
        byte15 = data[14]  # 第15个字节
        byte16 = data[15]  # 第16个字节
        byte17 = data[16]  # 第17个字节
        byte18 = data[17]  # 第18个字节
        speed1 = (byte2<<8)|byte3
        speed2 = (byte4<<8)|byte5
        joystick_x = (byte6<<8)|byte7
        joystick_y = (byte8<<8)|byte9
        sensor_1 = (byte10<<8)|byte11
        sensor_2 = (byte12<<8)|byte13
        sensor_3 = (byte14<<8)|byte15
        sensor_4 = (byte16<<8)|byte17
        if(2100>joystick_x>1900):
           joystick_x = 2000
        if(2100>joystick_y>1900):
           joystick_y = 2000
        if speed1 > 10000:
           speed1 = -(65535-speed1)
        elif speed2 > 10000:
             speed2 = -(65535-speed2)
        get_ecparm.publish_ecparm(-speed1,speed2,joystick_x,joystick_y,sensor_1,sensor_2,sensor_3,sensor_4)
        print('speed1=',-speed1,'speed2=',speed2,'joystick_x=',joystick_x,'joy_stick_y=',joystick_y,'sensor1=',sensor_1,'sensor2=',sensor_2,'sensor3=',sensor_3,'sensor4=',sensor_4)
  else:
    continue
# 关闭串口连接
ser.close()
