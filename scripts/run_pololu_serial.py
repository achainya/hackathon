#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import UInt16

ser = serial.Serial("/dev/ttyACM0")

def setAngle(angle_in_ms,channel):
    commandByte = chr(0x84)
    channelByte = chr(channel)
    lowTargetByte = chr(angle_in_ms*4 & 0x7F)
    highTargetByte = chr((angle_in_ms*4 >> 7) & 0x7F)
    command = commandByte + channelByte + lowTargetByte + highTargetByte
    ser.write(command)    

def listener():
    #rospy.init_node('run_pololu_serial',anonymous=True)
    rospy.init_node('listener',anonymous=True)
    print "Listener 2"
    rospy.loginfo("Listener node")
    rospy.Subscriber('angle_h',UInt16,adjustAngleH)
    rospy.Subscriber('angle_v',UInt16,adjustAngleV)
    rospy.spin()

def adjustAngleH(angle_in_ms):
    #rospy.loginfo("Call heard %d", angle_in_ms)
    channel = 0x01   
    commandByte = chr(0x84)
    channelByte = chr(channel)
    lowTargetByte = chr(angle_in_ms.data*4 & 0x7F)
    highTargetByte = chr((angle_in_ms.data*4 >> 7) & 0x7F)
    command = commandByte + channelByte + lowTargetByte + highTargetByte
    ser.write(command)
    
def adjustAngleV(angle_in_ms): 
   # rospy.loginfo("Call heard %d", angle_in_ms)
    channel = 0x04  
    commandByte = chr(0x84)
    channelByte = chr(channel)
    lowTargetByte = chr(angle_in_ms.data*4 & 0x7F)
    highTargetByte = chr((angle_in_ms.data*4 >> 7) & 0x7F)
    command = commandByte + channelByte + lowTargetByte + highTargetByte
    ser.write(command)
        
if __name__ == "__main__":
    listener()
    
