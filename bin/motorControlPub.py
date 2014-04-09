#!/usr/bin/env python

import sys
import time
import zmq

def pub_motor_control():
    port = "5556"
    topic = "motor"
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:%s" % port)
	#while True:
    messagedata = 'forward'
    print "{0} {1}".format(topic, messagedata)
    socket.send("{0} {1}".format(topic, messagedata))
    #time.sleep(10)

if __name__ == "__main__":
    pub_motor_control()
