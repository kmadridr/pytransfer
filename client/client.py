# Codigo hecho por Felipe Guzman 21168 y Kevin Madrid 24568
# nos basamos en la documentacio oficial
# https://docs.python.org/2/howto/sockets.html

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "10.12.36.32"     # Get local machine name
port = 8080                    # Reserve a port for your service.

s.connect((host, port))
while(True):
	data = raw_input()
	s.send(data)

	if data == 'ls':
		respond = s.recv(1024)
		print(respond)
	elif data == 'finito':
		break
	else:
		
		respond = s.recv(1024)
		if(respond == "no"):
			continue		
		f = open(data, 'w+')		
		f.write(respond)	
		f.close()
		print('Successfully get the file')
s.close()
print('connection closed')
