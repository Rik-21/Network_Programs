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

def reciverSide(data, divisor):
    print("Received Message:", data)
    r = crc(data, divisor)
    size = len(divisor)
    print("Remainder at Reciever Side: ", r)
    if int(r) == 0:
        print("No Error")
    else:
        print("Error")


def main():
    # message = "110001101"
    # divisor = "10101"  # X^4 + X^2 + 1

    message=input("enter your data_stream:")
    divisor=input("enter your divisor:")
    print("Original Message:", message)
    transmitted_message = encodeData(message, divisor)
    print("Transmitted Message:", transmitted_message)

    received_message = transmitted_message

    # Simulating error by flipping a bit
    choice = input("Do you want to change any bit: (yes/no):").lower()
    if choice == "yes":
       received_message = transmitted_message[:-1] + ('1' if transmitted_message[-1] == '0' else '0')
    
    reciverSide(received_message, divisor)




if __name__ == "__main__":
    main()