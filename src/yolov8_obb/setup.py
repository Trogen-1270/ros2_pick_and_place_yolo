from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'yolov8_obb'

setup(
    name=package_name,
    version='0.0.0',
    # find_packages() will find the 'yolov8_obb' directory as a package
    packages=find_packages(exclude=['test']),
    data_files=[
        # Standard file to identify the package
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Installs the package.xml file
        ('share/' + package_name, ['package.xml']),
        # Installs all files from the 'launch' directory
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        # Installs the model file(s) into a 'models' folder for clarity
        # If you add best.pt back to scripts/, this line will install it correctly.
        (os.path.join('share', package_name, 'models'), glob(os.path.join('scripts', '*.pt'))),
        # Installs the .ui file needed by the bolt_selector GUI
        (os.path.join('share', package_name, 'resource'), glob(os.path.join('resource', '*.ui'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='YOLOv8 OBB detection and publishing package',
    license='Apache-2.0',
    tests_require=['pytest'],
    # This section creates the executables that ros2 launch can find
    entry_points={
        'console_scripts': [
            # Creates an executable named 'yolov8_obb_publisher'
            # It runs the 'main' function from 'yolov8_obb_publisher.py'
            'yolov8_obb_publisher = yolov8_obb.yolov8_obb_publisher:main',

            # Creates an executable for the subscriber
            'yolov8_obb_subscriber = yolov8_obb.yolov8_obb_subscriber:main',
        ],
    },
)