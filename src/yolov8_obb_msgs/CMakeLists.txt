cmake_minimum_required(VERSION 3.8)
project(yolov8_obb_msgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find necessary packages
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED) # <-- Add this line

# Find NumPy headers
find_package(Python3 COMPONENTS Interpreter REQUIRED)
execute_process(
  COMMAND ${Python3_EXECUTABLE} -c "import numpy; print(numpy.get_include())"
  OUTPUT_VARIABLE NumPy_INCLUDE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
include_directories(${NumPy_INCLUDE_DIR})

# Generate the message interfaces
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/InferenceResult.msg"
  "msg/Yolov8Inference.msg"
  DEPENDENCIES std_msgs # <-- Add this line
)

ament_package()