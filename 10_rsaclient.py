import socket
import random
import math

# Function to encrypt a message using RSA algorithm
def encrypt(message, public_key):
    e, n = public_key
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5000

    client_socket.connect((host, port))
    public_key_str = client_socket.recv(1024).decode()
    public_key = eval(public_key_str)
    # print(public_key)

    message = input("Enter message to be encrypted: ")
    encrypted_message = encrypt(message, public_key)
    encrypted_message_str = ','.join(map(str, encrypted_message))
    print("Encrypted message:", encrypted_message_str)
    client_socket.send(encrypted_message_str.encode())

    client_socket.close()

if __name__ == '__main__':
    client_program()