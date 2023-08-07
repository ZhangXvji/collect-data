# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.23

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ztr/ros/catkin_ws/src/usb_cam

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ztr/ros/catkin_ws/src/usb_cam/build

# Include any dependencies generated for this target.
include CMakeFiles/v4l_driver.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/v4l_driver.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/v4l_driver.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/v4l_driver.dir/flags.make

CMakeFiles/v4l_driver.dir/src/util.cpp.o: CMakeFiles/v4l_driver.dir/flags.make
CMakeFiles/v4l_driver.dir/src/util.cpp.o: ../src/util.cpp
CMakeFiles/v4l_driver.dir/src/util.cpp.o: CMakeFiles/v4l_driver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ztr/ros/catkin_ws/src/usb_cam/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/v4l_driver.dir/src/util.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/v4l_driver.dir/src/util.cpp.o -MF CMakeFiles/v4l_driver.dir/src/util.cpp.o.d -o CMakeFiles/v4l_driver.dir/src/util.cpp.o -c /home/ztr/ros/catkin_ws/src/usb_cam/src/util.cpp

CMakeFiles/v4l_driver.dir/src/util.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/v4l_driver.dir/src/util.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ztr/ros/catkin_ws/src/usb_cam/src/util.cpp > CMakeFiles/v4l_driver.dir/src/util.cpp.i

CMakeFiles/v4l_driver.dir/src/util.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/v4l_driver.dir/src/util.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ztr/ros/catkin_ws/src/usb_cam/src/util.cpp -o CMakeFiles/v4l_driver.dir/src/util.cpp.s

CMakeFiles/v4l_driver.dir/src/converters.cpp.o: CMakeFiles/v4l_driver.dir/flags.make
CMakeFiles/v4l_driver.dir/src/converters.cpp.o: ../src/converters.cpp
CMakeFiles/v4l_driver.dir/src/converters.cpp.o: CMakeFiles/v4l_driver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ztr/ros/catkin_ws/src/usb_cam/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/v4l_driver.dir/src/converters.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/v4l_driver.dir/src/converters.cpp.o -MF CMakeFiles/v4l_driver.dir/src/converters.cpp.o.d -o CMakeFiles/v4l_driver.dir/src/converters.cpp.o -c /home/ztr/ros/catkin_ws/src/usb_cam/src/converters.cpp

CMakeFiles/v4l_driver.dir/src/converters.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/v4l_driver.dir/src/converters.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ztr/ros/catkin_ws/src/usb_cam/src/converters.cpp > CMakeFiles/v4l_driver.dir/src/converters.cpp.i

CMakeFiles/v4l_driver.dir/src/converters.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/v4l_driver.dir/src/converters.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ztr/ros/catkin_ws/src/usb_cam/src/converters.cpp -o CMakeFiles/v4l_driver.dir/src/converters.cpp.s

CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o: CMakeFiles/v4l_driver.dir/flags.make
CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o: ../src/camera_driver.cpp
CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o: CMakeFiles/v4l_driver.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ztr/ros/catkin_ws/src/usb_cam/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o -MF CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o.d -o CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o -c /home/ztr/ros/catkin_ws/src/usb_cam/src/camera_driver.cpp

CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ztr/ros/catkin_ws/src/usb_cam/src/camera_driver.cpp > CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.i

CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ztr/ros/catkin_ws/src/usb_cam/src/camera_driver.cpp -o CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.s

# Object files for target v4l_driver
v4l_driver_OBJECTS = \
"CMakeFiles/v4l_driver.dir/src/util.cpp.o" \
"CMakeFiles/v4l_driver.dir/src/converters.cpp.o" \
"CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o"

# External object files for target v4l_driver
v4l_driver_EXTERNAL_OBJECTS =

devel/lib/libv4l_driver.so: CMakeFiles/v4l_driver.dir/src/util.cpp.o
devel/lib/libv4l_driver.so: CMakeFiles/v4l_driver.dir/src/converters.cpp.o
devel/lib/libv4l_driver.so: CMakeFiles/v4l_driver.dir/src/camera_driver.cpp.o
devel/lib/libv4l_driver.so: CMakeFiles/v4l_driver.dir/build.make
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_highgui.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_ml.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_objdetect.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_photo.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_stitching.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_video.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_videoio.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_imgcodecs.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_calib3d.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_dnn.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_features2d.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_flann.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_imgproc.so.4.8.0
devel/lib/libv4l_driver.so: /usr/local/lib/x86_64-linux-gnu/libopencv_core.so.4.8.0
devel/lib/libv4l_driver.so: CMakeFiles/v4l_driver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ztr/ros/catkin_ws/src/usb_cam/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library devel/lib/libv4l_driver.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/v4l_driver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/v4l_driver.dir/build: devel/lib/libv4l_driver.so
.PHONY : CMakeFiles/v4l_driver.dir/build

CMakeFiles/v4l_driver.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/v4l_driver.dir/cmake_clean.cmake
.PHONY : CMakeFiles/v4l_driver.dir/clean

CMakeFiles/v4l_driver.dir/depend:
	cd /home/ztr/ros/catkin_ws/src/usb_cam/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ztr/ros/catkin_ws/src/usb_cam /home/ztr/ros/catkin_ws/src/usb_cam /home/ztr/ros/catkin_ws/src/usb_cam/build /home/ztr/ros/catkin_ws/src/usb_cam/build /home/ztr/ros/catkin_ws/src/usb_cam/build/CMakeFiles/v4l_driver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/v4l_driver.dir/depend

