	
#!/usr/bin/python

import socket
import thread
import sys
import os.path
from os import path

def readFile(requestedfilepath):
	with open(requestedfilepath, "r") as filereader:
        	filedetail = filereader.read()
	return filedetail 

def responseclient(client, clientaddress):
	clientrequest = client.recv(MAX_PACKET_SIZE)
        #print clientrequest 
	requestmethod = clientrequest.split(' ')[0]
        #print requestmethod
	if requestmethod == "GET":
		requestedfile = clientrequest.split()[1]
		#requestedfile = requestedfile[1:].strip()
	#print requestedfile
		filedetail = readFile(os.getcwd() + "/www/" + requestedfile)
               	#print filedetail 
		client.send(filedetail)
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
	
