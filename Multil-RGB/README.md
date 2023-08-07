## 1.下载  
wiki使用：http://wiki.ros.org/usb_cam  
github：https://github.com/ros-drivers/usb_cam

## 2.使用
注意：我对code有更改，直接从github上拉取的代码无法直接运行  
### 2.1 查看相机接口
每台机器接口都不一样，需要查看自己的相机接口  
```
ls /dev/video*
```
### 2.2 运行
运行单个相机，在config文件中更改启动的相机
```
roslaunch usb_cam usb_cam-test.launch
```
运行4个相机，在config文件中更改启动的相机
```
roslaunch usb_cam usb_cam-test_total.launch
```
