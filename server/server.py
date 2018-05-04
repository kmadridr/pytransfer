import socket                   # Import socket module
import glob

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(35)                     # Now wait for client connection.

print( 'Server listening....')

conn, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)

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
		f = open(filename,'rb')
		l = f.read(1024)
		conn.send(l)

		f.close()
		print('Done sending')

conn.send('Thank you for connecting')
conn.close()
