from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    slam = Node(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=['/home/aayush/amr_ws/src/amr_slam/config/slam_toolbox.yaml']
    )

    return LaunchDescription([slam])
