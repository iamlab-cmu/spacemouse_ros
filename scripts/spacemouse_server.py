import pyspacemouse
import time
from spacemouse_ros.msg import SpaceMouseState
import sys
import rospy

def main(args):
  rospy.init_node("spacemouse_server", anonymous=True)
  frequency = 100
  rate = rospy.Rate(frequency)
  success = pyspacemouse.open()
  spacemouse_pub = rospy.Publisher('/spacemouse/state', SpaceMouseState, queue_size=10)
  if success:
    while not rospy.is_shutdown():
        spacemouse_state = pyspacemouse.read()
        sms = SpaceMouseState()
        sms.header.stamp = rospy.Time.now()
        sms.x = spacemouse_state.x
        sms.y = spacemouse_state.y
        sms.z = spacemouse_state.z
        sms.roll = spacemouse_state.roll
        sms.pitch = spacemouse_state.pitch
        sms.yaw = spacemouse_state.yaw
        sms.buttons = spacemouse_state.buttons
        spacemouse_pub.publish(sms)
        rate.sleep()

if __name__ == '__main__':
    main(sys.argv)