import socket
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





def encodeData(data, divisor):
    l_key = len(divisor)
    append_data = data + '0'*(l_key-1)
    remainder = crc(append_data, divisor)
    codeword = data + remainder
    print("Remainder: ", remainder)
    print("Data: ", codeword)
    return codeword






 
   
    



def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. CRC\n6. Get Daytime\n0. Exit")
        option = input("Enter your choice: ")

        if option == '0':
            break

        if option == '6':
            data = "DAYTIME"
        elif option == '5':
            data = input("Enter a bit string: ")
            divisor="10101"
            data=encodeData(data,divisor)
            choice = input("Do you want to change any bit: (yes/no):").lower()
            if choice == "yes":
                data = data[:-1] + ('1' if data[-1] == '0' else '0')
    
        else:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            data = f"{option};{num1};{num2}"
           

        client_socket.send(data.encode())
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

    client_socket.close()

if __name__ == "__main__":
    main()