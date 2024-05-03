import socket
import datetime

addx = ""

def perform_operation(operation, num1, num2):
    if operation == 'ADD':
        return num1 + num2
    elif operation == 'SUBTRACT':
        return num1 - num2
    elif operation == 'MULTIPLY':
        return num1 * num2
    elif operation == 'DIVISION':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    elif operation == 'MODULUS':
        return num1 % num2
    else:
        return "Invalid operation"

# Function to get current date and time along with appropriate greeting
def get_date_time_greeting():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Good Afternoon"
    elif 18 <= current_time.hour < 20:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
    return f"{greeting}, the current date and time is {current_time}"

# Server configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port
server_socket.bind((UDP_IP, UDP_PORT))

print("Server is running...")
# print(f"Accepted connection from {address}")

while True:
    # Receive message from client
    data, addr = server_socket.recvfrom(1024)
    data = data.decode('utf-8')
    addx = addr
    print(f"Accepted connection from {addx}")
    print(f"client request {data}")
    # Check the received message
    response = None
    if data == "DAYTIME":
        print("Received DAYTIME request")
        response = get_date_time_greeting()
        print()

    elif data.startswith(("ADD", "SUBTRACT", "MULTIPLY", "DIVISION", "MODULUS")):
            print("Received MATH request")
            print(f"Accepted connection from {addx}")
            operation, num1, num2 = data.split(',')
            num1 = float(num1)
            num2 = float(num2)
            
            operation = operation.strip()
            response = perform_operation(operation, num1, num2)
    else:
        response = data
        print("Received message from client:", data)


    # Send response back to client
    server_socket.sendto(str(response).encode('utf-8'), addr)
