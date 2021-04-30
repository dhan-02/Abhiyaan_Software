#!/usr/bin/env python3
#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
from math import fabs

class TurtleBot:


    def __init__(self):
        rospy.init_node('Turtle_Mover',anonymous=True)
        self.vel_pub = rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=10)
        rospy.Subscriber('/turtle1/pose', Pose, self.update_pose1)
        rospy.Subscriber('/turtle2/pose', Pose, self.update_pose2)
        self.pose1 = Pose() # Turtle 1 pose
        self.pose2 = Pose() # Turtle 2 pose
        self.rate = rospy.Rate(10) #Frequency 10Hz

    def update_pose1(self,data):
        self.pose1 = data
        self.pose1.x = round(self.pose1.x, 4)
        self.pose1.y = round(self.pose1.y, 4)

    def update_pose2(self,data):
        self.pose2 = data
        self.pose2.x = round(self.pose2.x, 4)
        self.pose2.y = round(self.pose2.x, 4)

    def movement(self):
        vel_msg = Twist()
        time.sleep(1) #Pause Execution for a second

        # Move Straight until turtle 2 is 2 units away
        while(abs(self.pose1.x-self.pose2.x)>=2):
            vel_msg.linear.x = 1
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x  = 0

        #START OF MANUEVER
        #CIRCULAR MANUEVER
        while(self.pose2.x-self.pose1.x<=2):
            vel_msg.angular.z = 1
            vel_msg.linear.y = -2
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.angular.z = 0
        vel_msg.linear.y = 0
        self.vel_pub.publish(vel_msg)

        #Turn to face away from turtle 1
        while(self.pose2.theta>0.05):
            vel_msg.angular.z = -2
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.angular.z = 0
        self.vel_pub.publish(vel_msg)

        while(self.pose2.x-self.pose1.x<=5): #Safe distance chosen as 5
            vel_msg.linear.x = 1
            self.vel_pub.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        self.vel_pub.publish(vel_msg)
        rospy.spin()

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.movement()
    except rospy.ROSInterruptException:
        pass
