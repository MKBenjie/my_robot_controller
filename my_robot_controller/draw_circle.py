#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        # creating a publisher with datatype, topic name and queue size
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) 
        # creaating a timer that sends msg after 0.5 seconds
        self.timer = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw circle node has been started")

    def send_velocity_command(self):
        # create a message
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        # publish the message
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args= args)
    node = DrawCircleNode()     # create node instance
    rclpy.spin(node)            # spin node, it keeps it alive
    rclpy.shutdown()