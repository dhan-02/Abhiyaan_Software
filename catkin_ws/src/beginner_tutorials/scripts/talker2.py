import rospy
from std_msgs.msg import String

def talker():

    # talker2 node to publish String to the topic /autonomy

    pub = rospy.Publisher('/autonomy', String, queue_size = 10)
    rospy.init_node('talker2', anonymous = True)
    rate = rospy.Rate(3) # 3Hz Frequency
    
    while not rospy.is_shutdown():
        message = "Fueled By Autonomy"
        pub.publish(message)
        rate.sleep() # Maintains Rate

if __name__ == '__main__':

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
