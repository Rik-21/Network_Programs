import socket

# Client configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print("1. Echo message")
    print("2. Perform mathematical operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS)")
    print("3. Get date and time with greeting")
    print("4. Exit")
    choice = input("Enter your choice: ")
    # print("Your choice:", choice)+
    
    if choice == "1":
        message = input("Enter message to echo: ")
        client_socket.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))
        data, _ = client_socket.recvfrom(1024)
        print("Echoed message:", data.decode('utf-8'))
    elif choice == "2":
        operation = input("Enter operation (ADD, SUBTRACT, MULTIPLY, DIVISION, MODULUS): ")
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        client_socket.sendto(f"{operation},{num1},{num2}".encode('utf-8'), (UDP_IP, UDP_PORT))
        response, _ = client_socket.recvfrom(1024)
        print("Result:", response.decode())
    elif choice == "3":
        client_socket.sendto("DAYTIME".encode('utf-8'), (UDP_IP, UDP_PORT))
        data, _ = client_socket.recvfrom(1024)
        print("Result:", data.decode('utf-8'))
    elif choice == "4":
        break
    else:
        print("Invalid choice")

# Close the socket
client_socket.close()
