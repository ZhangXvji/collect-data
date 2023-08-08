## 1.有限设置

设置你的IPV4  

Address: 192.168.1.102

Netmask: 255.255.255.0

Getway: 192.168.1.1

## 2.启动robosense 16

参照github配置激光雷达驱动  
https://github.com/RoboSense-LiDAR/rslidar_sdk

## 3.将/rslidar_points转为/velodyne_points
参照github  
https://github.com/HViktorTsoi/rs_to_velodyne  
注意：我对代码修改，输出为points_raw，而非velodyne_points
## 4.使用
roslaunch rslidar_sdk start.launch  
rosrun rs_to_velodyne rs_to_velodyne XYZIRT XYZIRT