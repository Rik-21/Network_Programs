import socket

def manchester_encoding(data):
    encoded_data = ''
    for bit in data:
        if bit == '0':
            encoded_data += '01'
        else:
            encoded_data += '10'
    return encoded_data

def differential_manchester_encoding(data):
    encoded_data = ''
    last_bit = '0'  # Initialize the last bit to any value
    for bit in data:
        if bit == '0':
            if last_bit == '0':
                encoded_data += '10'
                last_bit = '0'
            else:
                encoded_data += '01'
                last_bit = '1'
        else:
            if last_bit == '0':
                encoded_data += '01'
                last_bit = '1'
            else:
                encoded_data += '10'
                last_bit = '0'
    return encoded_data


# Function to handle client requests
def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        print(f"Received data from client: {data}")
        manchester_encoded_data = manchester_encoding(data)
        differential_manchester_encoded_data = differential_manchester_encoding(data)

        print("Sending Manchester Encoded Data to client...")
        client_socket.send(str(manchester_encoded_data).encode())

        print("------------------------------------")

        print("Sending Differential Manchester Encoded Data to client...")
        client_socket.send(str(differential_manchester_encoded_data).encode())

    client_socket.close()


def main():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        handle_client_connection(client_socket)


if __name__ == "__main__":
    main()
