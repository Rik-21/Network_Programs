import socket

def main():
    # Set up the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    while True:
        # Menu driven options
        print("Menu:")
        print("1. Echo message")
        print("2. Perform mathematical operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS)")
        print("3. Get daytime greeting")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter message to echo: ")
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print("Echoed message:", response)
        elif choice == '2':
            operation = input("Enter operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS): ")
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            client_socket.send(f"{operation},{num1},{num2}".encode())
            response = client_socket.recv(1024).decode()
            print("Result:", response)
        
        elif choice == '3':
            client_socket.send("DAYTIME".encode())
            response = client_socket.recv(1024).decode()
            print("Server response:", response)
        else:
            print("Existing...")
            break

    client_socket.close()


if __name__ == "__main__":
    main()