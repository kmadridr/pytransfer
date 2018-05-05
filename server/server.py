#Codigo hecho por Kevin Madrid y Felipe Guzman
#basado en la documentacion del siguiente enlace
#https://docs.python.org/2/library/socket.html

import socket                   # Import socket module
import glob
import os.path


port = 8080                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "10.12.36.32"     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(35)                     # Now wait for client connection.

print( 'Server listening....')

conn, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
files = []
while True:
	print("Waiting for input")
	data = conn.recv(1024)
	print('Server received', repr(data))
	if data == 'ls':
		files = glob.glob('files/*')
		filenames = ''
		for a in files:
			filenames += a + '\n'
		conn.send(filenames)
	elif data == 'finito':
		break
	else:
		filename=data
		if os.path.exists(filename) is False:
			conn.send("no")			
			continue
		f = open(filename,'rb')
		l = f.read(1024)
		conn.send(l)
		
		f.close()
		print('Done sending')

conn.send('Thank you for connecting')
conn.close()
