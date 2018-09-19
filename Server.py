#!/usr/bin/python

import socket
import threading
import thread
import sys
import datetime
import os
from mimetools import Message
import mimetypes 
import os.path
from os import path
MAX_PACKET_SIZE = 1024
def Responseheader(responsecode,requestedfile):
	if responsecode == 200: 
		responseheaderok = "HTTP/1.0 200 OK "
		mimetype = mimetypes.guess_type(requestedfile)[0]
		todaysdate = datetime.datetime.today().strftime('%a, %d %b %Y %H:%M:%S GMT')
		modificationtime = datetime.datetime.fromtimestamp(os.path.getmtime(requestedfile)).strftime('%a, %d %b %Y %H:%M:%S GMT')
            	responsecontent = responseheaderok +"\nDate:" + todaysdate + " \nServer:Python0.0 \nLast-Modified:" + modificationtime + " \nContent-Length:" + str(os.path.getsize(requestedfile)) + " \nContent-Type:" + mimetype + "\r\n\n"
	else:
		responsecontent = """HTTP/1.0 404 ERR
Content-Type: text/html

<html>
<head>
</head>
<body>
<h1>file not found</h1>
</body>
</html>
"""
	return responsecontent
def readFile(requestedfilepath):
	with open(requestedfilepath, "r") as filereader:
        	filedetail = filereader.read()
	return filedetail 

def responseclient(client, clientaddress):
	clientrequest = client.recv(MAX_PACKET_SIZE)
        #print clientrequest 
	requestmethod = clientrequest.split(' ')[0]
        #print requestmethod
	#if requestmethod == "GET":
	requestedfile = clientrequest.split()[1]
		#requestedfile = requestedfile[1:].strip()
	#print requestedfile
	if os.path.isfile(os.getcwd() + "/www/" + requestedfile) :
		filedetail = readFile(os.getcwd() + "/www/" + requestedfile)
               	#print filedetail 
		responsefile  = Responseheader(200,os.getcwd() + "/www/" + requestedfile)
		#print responsefile
		responsefile  = responsefile  + filedetail
		#print responsefile
		client.send(responsefile)
		client.close()
	else:
		requestedfile = ""
		responsefile = Responseheader(404,os.getcwd() + "/www/" + requestedfile)
		client.send(responsefile)
		client.close()

if not path.exists('www'):
	print "We couldn't found directory www inside your current directory please create directory www"
	sys.exit(0)	
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
        serversocket.bind(('',0))
except socket.error, msg: 
        sys.exit(0)
print("Starting server on {host}:{port}".format(host=socket.gethostname().split('.')[0], port=serversocket.getsockname()[1]))
serversocket.listen(5) #telling library that listen to 5 client in queue

while 1:
	(client, clientaddress) = serversocket.accept()
	print("Recieved connection from clientaddress {clientaddr}".format(clientaddr=clientaddress))
    	thread.start_new_thread(responseclient,(client, clientaddress))
	
