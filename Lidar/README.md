1.将miiboo_imu.zip解压后拷贝到你的ROS工作空间路径下（比如catkin_ws/src/）。

2.使用catkin_make命令对上面的miiboo_imu驱动包进行编译。

3.用USB线将IMU模块与运行ROS的Ubuntu主机进行连接，在Ubuntu下查看IMU模块被识别出的串口设备号（比如/dev/ttyUSB0），并对该串口设备号赋予Linux系统可读写权限。最后将该串口设备后填入上面驱动包miiboo_imu/launch/imu.launch启动文件中的com_port变量之中，保存该launch启动文件并退出。

查看串口设备，一般是/dev/ttyUSB0

```bash
ls /dev/tty*
```

给串口临时读写权限

```bash
chmod 777 /dev/ttyUSB0
```

给串口永久读写权限，系统重启后生效

```bash
ls -l /dev/ttyUSB0
//search group
whoami
//search username
sudo usermod -aG <group> <username>
//for example
sudo usermod -aG dialout ztr
```

4.使用roslaunch命令启动miiboo_imu驱动包，IMU模块数据就会自动发送到对应的ROS话题（/imu），其他需要使用IMU数据的程序只需订阅话题/imu就可以了。

```bash
roslaunch miiboo_imu imu.launch
```