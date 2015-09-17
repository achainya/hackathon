#!/usr/bin/python
import rospy
from std_msgs.msg import UInt16
def publisher():
     pub_h = rospy.Publisher('angle_h', UInt16, queue_size=10)
     pub_v = rospy.Publisher('angle_v', UInt16, queue_size=10)
     rospy.init_node('input', anonymous=True)
     rate = rospy.Rate(10)
     angle_h=1500
     angle_v=1500
     while not rospy.is_shutdown():
        str = raw_input("Enter w-s for tilt, a-d for pan: ")
        if (str=='a' and angle_h>1000):
            angle_h-=200
        if(str=='d' and angle_h<2000):
            angle_h+=200
        if(str=='w' and angle_v<2000):
            angle_v+=200
        if(str=='s' and angle_h>1000):
            angle_v-=200
        v_msg = UInt16()
        v_msg.data = angle_v
        h_msg = UInt16()
        h_msg.data = angle_h
        pub_v.publish(v_msg)
        pub_h.publish(h_msg)
        #rate.sleep()
   
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
