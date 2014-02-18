import socket
import threading
import sys
import time

ip_address = sys.argv[1]

class PortConnection(threading.Thread):
	def __init__(self, ip_address, port):
		super(PortConnection, self).__init__()
		self.ip_address = ip_address
		self.port = port

	def run(self):
		try_port(self.ip_address, self.port)

def try_port(ip_address, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(10)
		s.connect((ip_address, port))
		s.send("'ello!\r\n")
		response = s.recv(2048)
		if response:
			print '%s responded with: \n"%s"\n\n' % (port, response)
		result = True
	except KeyboardInterrupt:
		raise KeyboardInterrupt
	except:
		result = False
	finally:
		s.close()

	return result

for port in xrange(65535):
	try:
		conn = PortConnection(ip_address, port)
		conn.setDaemon(True)
		conn.start()
	except KeyboardInterrupt:
		print "\nBye!"
		sys.exit()
