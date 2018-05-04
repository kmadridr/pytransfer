import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
data = input()
s.send(data)

if data == 'ls':
    respond = s.recv(1024)
    print(respond)
else:

    f = open(data, 'wb')
    respond = s.recv(1024)
    while respond:
        f.write(s.recv(1024))
        respond = s.recv(1024)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')
