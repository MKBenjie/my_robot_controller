#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

# creating a node class
class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello there " +str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)   # initializing ros2 communications
    node = MyNode()
    rclpy.spin(node)        #keeping the node alive
    rclpy.shutdown()        #stop communications

if __name__=='__main__':
    main()