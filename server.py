import socket
import threading
import sys

server = "192.168.1.72"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)
print("Waiting for a connection, server has started")


def threaded_client(conn) :
	reply = ""

	while True:
		try:
			data = conn.recv(2048)
			reply = data.decode("utf-8")

			if not data : 
				print("Disconnected")
				break

			else :
				print("Received: ", reply)
				print("Sending: ", reply)

			conn.sendall(str.encode(reply))

		except:
			break

while True:
	conn, addr = s.accept()
	print("connection to:", addr)

	th = threading.Thread(target=threaded_client, args=(conn,))
	th.start()