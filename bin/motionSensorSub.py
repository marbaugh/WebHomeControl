#!/usr/bin/env python

import sys
import time
import zmq

port = "5556"
# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

def sub_motion_sensor_status():
	print "Listening for status of motion sensor"
	socket.connect ("tcp://localhost:{0}".format(port))
	topicfilter = "motion"
	while True:
		socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
		string = socket.recv()
		topic, messagedata = string.split()
		print topic, messagedata

if __name__ == "__main__":
	sub_motion_sensor_status()
