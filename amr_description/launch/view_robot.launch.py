from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    urdf_path = os.path.join(
        get_package_share_directory('amr_description'),
        'urdf',
        'amr.urdf.xacro'
    )

    robot_description = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': os.popen(f'xacro {urdf_path}').read()
        }]
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher'
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2'
    )

    return LaunchDescription([
        joint_state_publisher,
        robot_description,
        rviz
    ])
