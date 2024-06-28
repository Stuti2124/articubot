import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='ydlidar_ros2_driver',
            executable='ydlidar_ros2_driver_node',
            name='ydlidar_ros2_driver_node',
            output='screen',
            emulate_tty=True,
            parameters=[{
                'port': '/dev/ttyUSB0',
                'frame_id': 'laser_frame',
                'ignore_array': '',
                'baudrate': 115200,
                'lidar_type': 1,
                'device_type': 0,
                'sample_rate': 3,
                'intensity_bit': 0,
                'abnormal_check_count': 4,
                'fixed_resolution': True,
                'reversion': True,
                'inverted': True,
                'auto_reconnect': True,
                'isSingleChannel': True,
                'intensity': False,
                'support_motor_dtr': True,
                'angle_max': 180.0,
                'angle_min': -180.0,
                'range_max': 12.0,
                'range_min': 0.1,
                'frequency': 10.0,
                'invalid_range_is_inf': False,
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])
