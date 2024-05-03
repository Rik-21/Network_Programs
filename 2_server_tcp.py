import socket
import datetime

addr=""

# Function to perform mathematical operations
def perform_operation(operation, num1, num2):
    if operation == "ADD":
        return num1 + num2
    elif operation == "SUBTRACT":
        return num1 - num2
    elif operation == "MULTIPLY":
        return num1 * num2
    elif operation == "DIVISION":
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    elif operation == "MODULUS":
        return num1 % num2
    else:
        return "Invalid operation"


# Function to get the current time and greet accordingly
def get_time_greeting():
    current_time = datetime.datetime.now()
    if 6 <= current_time.hour < 12:
        return "Good Morning, it's " + str(current_time)
    elif 12 <= current_time.hour < 18:
        return "Good Afternoon, it's " + str(current_time)
    elif 18 <= current_time.hour < 20:
        return "Good Evening, it's " + str(current_time)
    else:
        return "Good Night, it's " + str(current_time)


# Function to handle client requests
def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"request for client {data}")
        if data == "DAYTIME":
            print("Received DAYTIME request")
            response = get_time_greeting()
        elif data.startswith(("ADD", "SUBTRACT", "MULTIPLY", "DIVISION", "MODULUS")):
            print("Received mathematical operation request")
            operation, num1, num2 = data.split(",")
            num1 = float(num1)
            num2 = float(num2)
            operation = operation.strip()
            response = perform_operation(operation, num1, num2)
        else:
            print("Received message from client:", data)
            
            response = data

        client_socket.send(str(response).encode())

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
