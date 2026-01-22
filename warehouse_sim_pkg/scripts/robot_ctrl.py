#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def run():
    rospy.init_node('ctrl', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.3
        pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass