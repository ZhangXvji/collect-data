import serial
import time

# 设置串口参数
serial_port = '/dev/ttyACM4'  # 根据实际情况修改串口设备路径
baud_rate = 115200

# 打开串口
ser = serial.Serial(serial_port, baud_rate)

# 循环接收数据
while True:
    # 读取串口数据
    data = ser.read(7)  # 假设要读取的数据长度为4字节

    # 进行数据处理
    if len(data) == 7 and data[0] == 0xff and data[6] == 0xaa:
        byte1 = data[0]  # 第1个字节
        byte2 = data[1]  # 第2个字节
        byte3 = data[2]  # 第3个字节
        byte4 = data[3]  # 第4个字节
        byte5 = data[4]  # 第5个字节
        byte6 = data[5]  # 第6个字节
        byte7 = data[6]  # 第7个字节

        # 合并中间两位数据的高8位和第8位
        #combined_data = (byte2 & 0x7F) << 8 | (byte3 & 0x80)
        #speed1 = int(combined_data)
        # 打印接收到的数据
        print("Received data:",hex(byte1),hex(byte2),hex(byte3),hex(byte4),hex(byte5),hex(byte6),hex(byte7))
        time.sleep(1)
        #print("Combined data:",speed1/19)
    else:
        print("Error: Failed to receive complete data")
        time.sleep(1)
# 关闭串口连接
ser.close()
