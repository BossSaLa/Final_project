#!/usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def Go_to_kitchen_server_callback(req):
    #print("Doing something..")
    Do = " “Going to kitchen.” "
    rospy.loginfo(Do)
    #time.sleep(2)
    for i in range(0, 2) :
        print(i)
        time.sleep(1)
    Done = " “Arrived.” "
    rospy.loginfo(Done)
    return EmptyResponse()

def Go_to_home_server_callback(req):
    #print("Doing something..")
    Do = " “Going to home.” "
    rospy.loginfo(Do)
    #time.sleep(2)
    for i in range(0, 2) :
        print(i)
        time.sleep(1)
    Done = " “Arrived.” "
    rospy.loginfo(Done)
    return EmptyResponse()

def stop_server_callback(req):
    #print("Doing something..")
    Done = " Stop!!!!.” "
    rospy.loginfo(Done)
    return EmptyResponse()


def Robot_server():
    rospy.init_node('Robot_server')
    service = rospy.Service('/go_to_kitchen', Empty, Go_to_kitchen_server_callback)
    print("Go to kitchen is Ready!!!")
    service2 = rospy.Service('/stop', Empty, stop_server_callback)
    print("stop is Ready!!!")
    service3 = rospy.Service('/go_home', Empty, Go_to_home_server_callback)
    print("Go to home is Ready!!!")
    #service.spin()
    #service.shutdown("shutdown")
    rospy.spin()



if __name__ == "__main__":
    Robot_server()
    

