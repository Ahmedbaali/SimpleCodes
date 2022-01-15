import socket	#for sockets
import sys	#for exit

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()

host = 'localhost'
port = 8888

while(1) :
	msg = input('Enter message to send : ')
	#msg.encode()
	try :
		#Set the whole string
        
		s.sendto(msg.encode(), (host, port))
		
		# receive data from client (data, addr)
		d = s.recvfrom(1024)
		reply = d[0].decode()
		addr = d[1]
		
		print ('Server reply : ' + reply)
	
	except (socket.error):
		print ('Error Code : ')
		sys.exit()