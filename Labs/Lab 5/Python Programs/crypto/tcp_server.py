import socket
from Crypto.Random.random import getrandbits
from Crypto.PublicKey import DSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Hash import SHA256
p = 25822498780869085896559191720030118743297057928292235128306593565406476220168
41194629645353280137831435903171972747559779
g = 2


def compute_shared_key(private_key, other_public_key):
	return pow(other_public_key, private_key, p)

def hash_shared_key(shared_key):
	return SHA256.new(long_to_bytes(shared_key)).digest()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
	server_socket.bind(('127.0.0.1', 12345))
	server_socket.listen()
	print("Server is listening...")
	conn, addr = server_socket.accept()
	with conn:
		print("Connected by", addr)
		y = getrandbits(400)
		server_public_key = pow(g, y, p)
		conn.sendall(long_to_bytes(server_public_key))
		client_public_key = bytes_to_long(conn.recv(1024))
		shared_key = compute_shared_key(y, client_public_key)
		sk = hash_shared_key(shared_key)
		print("Secret Key:", sk)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			print("Client:", data.decode('utf-8'))
			message = input("Server: ")
			conn.sendall(message.encode('utf-8'))
