import socket
import datetime
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def crc(message, divisor):
    pick = len(divisor)
    tmp = message[:pick]

    while pick < len(message):
        if tmp[0] == '1':
            # print("Remainder at this step: ", xor(divisor, tmp))
            tmp = xor(divisor, tmp) + message[pick]
        else:
            # print("Remainder at this step: ", xor(divisor, tmp))
            tmp = xor('0'*pick, tmp) + message[pick]
        pick += 1

    if tmp[0] == "1":
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword

def crc_checksum(data):
    # CRC checksum calculation (dummy implementation for demonstration)
    divisor = "10101"
    

    print("Received Message:", data)    
    r = crc(data, divisor)
    size = len(divisor)
    
    if int(r) == 0:
        return "No error"
    else:
        return f'error detected {r}'

def handle_menu_option(option, num1, num2):
    if option == '1':
        return f'{num1 + num2}'
    elif option == '2':
        return f'{num1 - num2}'
    elif option == '3':
        return f'{num1 * num2}'
    elif option == '4':
        if num2 != 0:
            return f'{num1 / num2}'
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid option"

def handle_daytime_request():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    greeting = "Good Morning" if now.hour < 12 else "Good Evening"
    return f"{current_time}, {greeting}"

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected to client: {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        

        if data == "DAYTIME":
            response = handle_daytime_request()
        elif ";" in data:
            try:
                # Assuming data format: option;num1;num2
                option, num1, num2 = data.split(';')
                num1, num2 = int(num1), int(num2)
                response = handle_menu_option(option, num1, num2)
            except Exception as e:
                response = f"Error: {str(e)}"
        else:  # CRC
            crc = crc_checksum(data)
            response = f"CRC checksum: {crc}"

        conn.send(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()