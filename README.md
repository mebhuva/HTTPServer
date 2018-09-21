
This is a simple multithreded http server developed in python

-> This server accepts the multiple client request and sends resopnse

-> If server has file then client will receive 200 ok response and if not then 404 not found

-> To send request and resopnse server creates tcp socket connection where server runs on randomly assigned port by the operating system

-> Whenhen client request come to the server it accept it and using multithreding it assign thread to the every individual client

-> Then Server looks into the WWW directory and reads the file content and send resopnse 200 with proper header and file conent

-> Server Also maintains counter to know how many time each file accessed by multiple clients

Steps to run multithreded http server

1. open terminal and run using command ->  python server.py, when you run this command server will print ip address and port number where server is running right now

2. then open another terminal and type command-> wget http://remote02.cs.binghamton.edu:47590/bar.html here change the ip address and port number where server is running

3. Now we will receive following output

on server terminal ->

mbhuva1@remote02:~/DS/cs457-cs557-pa1-mbhuva1$ python server.py
Starting server on remote02:53411
Recieved connection from clientaddress ('128.226.114.206', 40352)
/index.html|128.226.114.206|40352|1
Recieved connection from clientaddress ('128.226.114.206', 40354)
/index.html|128.226.114.206|40354|2
Recieved connection from clientaddress ('128.226.114.206', 40356)
/index.html|128.226.114.206|40356|3
Recieved connection from clientaddress ('128.226.114.206', 40358)
/index.html|128.226.114.206|40358|4
Recieved connection from clientaddress ('128.226.114.206', 40360)
/index.html|128.226.114.206|40360|5
Recieved connection from clientaddress ('128.226.114.206', 40362)
/index.html|128.226.114.206|40362|6


on another terminal ->

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:39--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.1’

index.html.1        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:39 (9.45 MB/s) - ‘index.html.1’ saved [209/209]

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:45--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.2’

index.html.2        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:45 (25.8 MB/s) - ‘index.html.2’ saved [209/209]

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:46--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.3’

index.html.3        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:46 (24.9 MB/s) - ‘index.html.3’ saved [209/209]

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:46--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.4’

index.html.4        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:46 (26.4 MB/s) - ‘index.html.4’ saved [209/209]

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:47--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.5’

index.html.5        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:47 (11.1 MB/s) - ‘index.html.5’ saved [209/209]

mbhuva1@remote06:~$ wget remote02.cs.binghamton.edu:53411/index.html
--2018-09-20 20:56:47--  http://remote02.cs.binghamton.edu:53411/index.html
Resolving remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)... 128.226.114                                                                                        .202
Connecting to remote02.cs.binghamton.edu (remote02.cs.binghamton.edu)|128.226.11                                                                                        4.202|:53411... connected.
HTTP request sent, awaiting response... 200 OK
Length: 209 [text/html]
Saving to: ‘index.html.6’

index.html.6        100%[===================>]     209  --.-KB/s    in 0s

2018-09-20 20:56:47 (14.7 MB/s) - ‘index.html.6’ saved [209/209]




