#!/usr/bin/env python
import rospy
#import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from std_msgs.msg import String
from geometry_msgs.msg import Point
from ros_igtl_bridge.msg import igtlpoint
from time import sleep
#outPin="P9_12"
outPWM="P9_14"
def callback(data):
        #GPIO.setup(outPin,GPIO.OUT)
        PWM.start(outPWM, 0, 1000)
        for i in range(0,3):
        #GPIO.output(outPin, GPIO.LOW)
                #sleep(3)
                print data.pointdata.x
                V=data.pointdata.x
                DC=V/3.365*10
                if DC>100:
                        DC=100
                PWM.set_duty_cycle(outPWM, DC)
                sleep(3)
                #GPIO.output(outPin, GPIO.HIGH)
                #sleep(3)
        PWM.stop(outPWM)
        PWM.cleanup()
        #GPIO.cleanup()

def main():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('led')

    rospy.Subscriber("IGTL_POINT_IN", igtlpoint, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()

