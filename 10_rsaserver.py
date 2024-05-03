import socket
import random
import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to find modular inverse
def find_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Generate two large prime numbers
def generate_prime():
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

# Generate public and private keys
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)
    d = find_inverse(e, phi)
    return ((e, n), (d, n))

# Decrypt a message
def decrypt(encrypted, private_key):
    d, n = private_key
    decrypted = [chr(pow(char, d, n)) for char in encrypted]
    return ''.join(decrypted)

def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5000
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("RSA Server started")
    print("Waiting for connections...")

    client_socket, addr = server_socket.accept()
    print('Got connection from', addr)

    public_key, private_key = generate_keys()
    # print(public_key)
    client_socket.send(str(public_key).encode())

    while True:
        
        data = client_socket.recv(1024)
        
        data=data.decode()

        print("encoded data: ",data)

        if not data:
            break

        encrypted_data = [int(x) for x in data.split(',')]
        decrypted_data = decrypt(encrypted_data, private_key)
        print('Received:', decrypted_data)

    client_socket.close()

if __name__ == '__main__':
    server_program()