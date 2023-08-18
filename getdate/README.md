## 1.文件说明

get_imu_raw.py：将rosbag中/imu转化为本地csv文件  
get_ecparm_raw.py：将rosbag中/ecparm转化为本地csv文件，/ecparm是自定义的topic类型  
形如：  
header:   
  seq: 20  
  stamp:   
    secs: 1692343215  
    nsecs: 184760808  
  frame_id: "ecparm_link"  
motor:   
  speed1: 32.0  
  speed2: 23.0  
joystick:   
  joystick_x: 0.04363323003053665  
  joystick_y: 0.045378562062978745  
sensor:   
  sensor_1: 1.0180248022079468  
  sensor_2: -2.652737617492676  
  sensor_3: -9.299264907836914  
  sensor_4: -9.29923152923584  

get_mp4_raw.py：将rosbag中/usb_cam/image_raw转化为本地mp4文件，帧率为30FPS  
get_data_raw.py：整合imu和ecparm，但不包括mp4转化  