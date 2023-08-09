# for D455 get RGB Video Capture
# press Q to quit
import pyrealsense2 as rs
import numpy as np
from pathlib import Path
import cv2, re, glob

def increment_path(path, exist_ok=False, sep='', mkdir=False):
    path = Path(path)
    n=''
    if path.exists() and not exist_ok:
        suffix = path.suffix
        path = path.with_suffix('')
        dirs = glob.glob(f"{path}{sep}*")  # similar paths
        matches = [re.search(rf"%s{sep}(\d+)" % path.stem, d) for d in dirs]
        i = [int(m.groups()[0]) for m in matches if m]  # indices
        n = max(i) + 1 if i else 2  # increment number
        path = Path(f"{path}{sep}{n}{suffix}")  # update path
    dir = path if path.suffix == '' else path.parent  # directory
    if not dir.exists() and mkdir:
        dir.mkdir(parents=True, exist_ok=True)  # make directory
    return path, str(n)

def save_RGBvideo_D455(save_size=(640, 480), save_fps=30, save_mp4=False, dcam_size=(640,480), dcam_fps=30):
    #====create save_path =======#
    video_dirname, order_name = 'save_RGBD_video', 'video'
    exist_ok = False
    save_dir, order_num = increment_path(Path(video_dirname) / order_name, exist_ok=exist_ok)
    save_dir = str(save_dir)
    order_num = int(order_num) if order_num.isnumeric() else ''
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    #===== configure for video format, flv, MP4, etc...=======#
    if save_mp4:  # save_format : mp4
        fourcc, save_file = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), Path(save_dir) / f'video{order_num}.mp4'
    else:
        fourcc, save_file = cv2.VideoWriter_fourcc('F', 'L', 'V', '1'), Path(save_dir) / f'video{order_num}.flv'
    save_size, save_fps,  = save_size, save_fps
    Writer = cv2.VideoWriter(str(save_file), fourcc, save_fps, save_size)

    #===========Configure color streams for D455 realsense camera======#
    pipeline = rs.pipeline()
    config = rs.config()
    # Get device product line for setting a supporting resolution
    pipeline_wrapper = rs.pipeline_wrapper(pipeline)
    pipeline_profile = config.resolve(pipeline_wrapper)
    device = pipeline_profile.get_device()
    device_product_line = str(device.get_info(rs.camera_info.product_line))

    found_rgb = False

    for s in device.sensors:
        if s.get_info(rs.camera_info.name) == 'RGB Camera':
            found_rgb = True
            break
    if not found_rgb:
        print("The demo requires Depth camera with Color sensor")
        exit(0)

    if device_product_line == 'L500':
        config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
    else:
        config.enable_stream(rs.stream.color, dcam_size[0], dcam_size[1], rs.format.bgr8, dcam_fps)

    pipeline.start(config)
    print('Depth Camera init OK!!!')
    writer_flag = True
    try:
        print('Start processing, press k to pause or continue')
        while True:
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            if not color_frame:
                continue
            # convert to numpy array
            color_image = np.asanyarray(color_frame.get_data())

            if writer_flag:
                Writer.write(color_image)
            else:
                paused_warning = 'Capture is paused,  k to continue.....'
                cv2.putText(color_image, paused_warning, (int(color_image.shape[0]/10), int(color_image.shape[1]/12)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)
                print(paused_warning)

            cv2.namedWindow('RGB_video', cv2.WINDOW_NORMAL)
            cv2.imshow('RGB_video', color_image)

            # ====== input waiting====== #
            k = cv2.waitKey(1)
            if k == ord('q'): # input 'q' , close the windows,exit
                cv2.destroyAllWindows()
                break

            # pause capturing , and continue
            if k == ord('k') and writer_flag is True:
                writer_flag = False
                print('Now is pause')
            elif k == ord('k') and writer_flag is False:
                writer_flag = True
                print('continue capturing')

    finally:
        # Stop streaming
        print('the video save to :', save_file)
        Writer.release()
        pipeline.stop()
        print('pipeline Stop, Writer release success.')
';';';';';';';'''''''';'
if __name__ == '__main__':
    # video save parameters, save_format: mp4 or flv
    save_size, save_fps, save_mp4 = (640, 480),30 , True
    # config Depth camera parameters
    # RBGsize recommand: (1280, 800), (1280,720), (848, 480), (640, 480), (640, 360), (480,270), (424, 240)
    # for 32x downsampling --- (1280, 800), (640, 480)
    # D455fps recommand: 30, 15, 10, 5
    D455_RGBsize, D455_fps = (640, 480),30 # recommand same as save_size, save_fps

    save_RGBvideo_D455(save_size=save_size, save_fps=save_fps, save_mp4=save_mp4,
                       dcam_size=D455_RGBsize, dcam_fps=D455_fps)
