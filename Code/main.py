#!/usr/bin/env python3

from std_srvs.srv import Empty
import rospy


def kitchen():
    rospy.wait_for_service('/go_to_kitchen')
    try:
        trigger = rospy.ServiceProxy('/go_to_kitchen', Empty)
        print("Robot will be go to kitchen.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def home():
    rospy.wait_for_service('/go_home')
    try:
        trigger = rospy.ServiceProxy('/go_home', Empty)
        print("Robot will go to home.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def stop():
    rospy.wait_for_service('/stop')
    try:
        trigger = rospy.ServiceProxy('/stop', Empty)
        print("Robot will be stop.")
        resp1 = trigger()
        print("Done")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    kitchen()
    stop()
    home()
    stop()




