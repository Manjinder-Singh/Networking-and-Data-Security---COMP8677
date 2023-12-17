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
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect((server_ip, server_port))
	private_key, public_key = generate_dh_key()
	client_socket.send(str(public_key).encode())
	server_public_key = int(client_socket.recv(4096).decode())
	shared_key = compute_shared_key(private_key, server_public_key)
	print(f"Secret Key: {shared_key}")
	secret_key = SHA256.new(str(shared_key).encode()).digest()
	aes_cipher = AES.new(secret_key, AES.MODE_EAX)
	while True:
		message = input("You: ")
		# Encrypt the message and compute the tag
		ciphertext = aes_cipher.encrypt(message.encode('utf-8'))
		print(f"Cipher Text (C): {ciphertext}")
		tag=SHA256.new(ciphertext).digest()
		message_to_send = len(ciphertext).to_bytes(4, 'big') + len(tag).to_bytes(4, 'big') + ciphertext + tag+aes_cipher.nonce
		print(f"Tag: {tag}")
		client_socket.send(message_to_send)
		print(f"Message: {message_to_send}")
		data = client_socket.recv(4096)
		ciphertext_length = int.from_bytes(data[:4], 'big')
		tag_length = int.from_bytes(data[4:8], 'big')
		ciphertext = data[8:8+ciphertext_length]
		received_tag = data[8+ciphertext_length:]
		aes_cipher = AES.new(secret_key, AES.MODE_EAX,
		nonce=aes_cipher.nonce)
		decrypted_message = aes_cipher.decrypt(ciphertext)
		# Verify the tag
		new_tag = SHA256.new(ciphertext).digest()
		if new_tag != received_tag:
			print("Tag verification failed. Message might be tampered.")
		else:
			print("Server:", decrypted_message.decode()) # Convert to string for display
if __name__ == "__main__":
	main()
