cmake_minimum_required(VERSION 3.0.2)
project(warehouse_sim_pkg)
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs geometry_msgs gazebo_ros)
catkin_package(CATKIN_DEPENDS roscpp rospy std_msgs geometry_msgs gazebo_ros)
include_directories(${catkin_INCLUDE_DIRS})
install(DIRECTORY launch worlds models scripts
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        USE_SOURCE_PERMISSIONS)