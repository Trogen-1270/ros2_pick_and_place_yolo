cmake_minimum_required(VERSION 3.8)
project(yolov8_obb)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(yolov8_obb_msgs REQUIRED)

ament_python_install_package(${PROJECT_NAME})

ament_package()