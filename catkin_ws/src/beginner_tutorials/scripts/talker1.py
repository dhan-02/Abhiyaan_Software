import rospy
from std_msgs.msg import String

def talker():

    #talker1 node publishing a String to the topic /team_abhiyaan

    pub = rospy.Publisher('/team_abhiyaan', String, queue_size = 10)
    rospy.init_node('talker1', anonymous = True)
    rate = rospy.Rate(3) #3 Hz frequency
    
    while not rospy.is_shutdown():
        message = "Team Abhiyaan:"
        pub.publish(message)
        rate.sleep() # Maintains rate

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
