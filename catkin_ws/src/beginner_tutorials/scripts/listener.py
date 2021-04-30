import rospy
from std_msgs.msg import String

msg1 = ""

def callback1(data):

    #/team_abhiyaan

    global msg1
    msg1 = data.data

def callback2(data):

    #/autonomy

    message = msg1+" "+data.data #Combining the msgs obtained in both topics
    print(message)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/team_abhiyaan', String, callback1)
    rospy.Subscriber('/autonomy', String, callback2)
    rospy.spin()

if __name__ == '__main__':
    listener()
