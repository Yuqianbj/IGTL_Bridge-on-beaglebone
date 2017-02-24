#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Point
import Adafruit_BBIO.ADC as ADC
from ros_igtl_bridge.msg import igtlpoint
from std_msgs.msg import String
from time import sleep
analogPin="P9_33"
def main():
    ADC.setup()
    cmd_pub = rospy.Publisher('IGTL_POINT_OUT', igtlpoint)
    rospy.init_node('cmd', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    Pointmsg = igtlpoint()
#    Pointname = "received"
    while(1):

        Pointmsg.name="received"
        potVal=ADC.read(analogPin)
        Pointmsg.pointdata.x=float(potVal)
        Pointmsg.pointdata.y=float(potVal)
        Pointmsg.pointdata.z=float(potVal)
        cmd_pub.publish(Pointmsg)
        sleep(1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
