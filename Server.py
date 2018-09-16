#!/usr/bin/python

import socket
import thread
import sys
import datetime
import os
CounterList = []

		
try:
	PORT = int(sys.argv[1]) 
except:
	print "Port number should be a valid integer"


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Starting server on {host}:{port}".format(host=socket.gethostname().split('.')[0], port=PORT))
try:
        serversocket.bind(('',PORT))
except socket.error, msg:
        print "please enter different port number " + str(PORT) + " is already in use" 
        sys.exit(0)
print("Server on port {port} started.".format(port=PORT))
serversocket.listen(1)

while 1:
	(client, clientaddress) = serversocket.accept()
	print("Recieved connection from clientaddress {clientaddr}".format(clientaddr=clientaddress))
    	thread.start_new_thread(responseclient,(client, clientaddress))
	
