import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Random.random import getrandbits
from Crypto.Hash import SHA256

#Using below Diffie-Hellman parameters
p = 25822498780869085896559191720030118743297057928292235128306593565406476220168
41194629645353280137831435903171972747559779
g = 2

def generate_dh_key():
	private_key = getrandbits(400)
	public_key = pow(g, private_key, p)
	return private_key, public_key

def compute_shared_key(private_key, other_public_key):
	return pow(other_public_key, private_key, p)

def main():
	server_ip = '127.0.0.1'
	server_port = 12349
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((server_ip, server_port))
	server_socket.listen(1)
	print("Server listening on {}:{}".format(server_ip, server_port))
	conn, addr = server_socket.accept()
	print("Connected to client:", addr)
	private_key, public_key = generate_dh_key()
	# sending the public key
	conn.send(str(public_key).encode())
	# receive the clients public key
	client_public_key = int(conn.recv(4096).decode())
	# create a shared key on both the sides
	shared_key = compute_shared_key(private_key, client_public_key)
	print(f"Key:{shared_key}")
	secret_key = SHA256.new(str(shared_key).encode()).digest()
	aes_cipher = AES.new(secret_key, AES.MODE_EAX,nonce=b'\x00' * 16)
	while True:
		data = conn.recv(4096)
		ciphertext_length = int.from_bytes(data[:4], 'big')
		tag_length = int.from_bytes(data[4:8], 'big')
		ciphertext = data[8:8+ciphertext_length]
		print(f"Cipher Text (C): {ciphertext}")
		received_tag = data[8+ciphertext_length:8+ciphertext_length+tag_length]
		print(f"Tag: {received_tag}")
		nonce=data[8+ciphertext_length+tag_length:]
		print(f"secret_key (sk): {secret_key}")
		aes_cipher = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
		decrypted_message = aes_cipher.decrypt(ciphertext)
		print(f"Decrypted Message: {decrypted_message}")
		# Verify the tag
		new_tag = SHA256.new(ciphertext).digest()
		if new_tag != received_tag:
			print("Tag verification failed. Message might be tampered.")
		else:
			print("Client:", decrypted_message.decode()) # Convert to string for display

if __name__ == "__main__":
	main()
