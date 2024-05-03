def calculate_checksum(message_slices):
    checksum = 0
    for slice in message_slices:
        checksum += int(slice, 2)
    checksum = bin(checksum)[2:]  # Convert to binary and remove '0b'
    # If checksum is more than 4 bits, wrap around
    while len(checksum) > 4:
        overflow = checksum[:-4]
        remaining = checksum[-4:]
        checksum = bin(int(overflow, 2) + int(remaining, 2))[2:].zfill(4)
    # Complement the checksum
    checksum = ''.join('1' if bit == '0' else '0' for bit in checksum)
    return checksum

def introduce_error(message):
    error_bit = input("Enter the position of the bit to flip (1-indexed): ")
    error_bit = int(error_bit) - 1  # Convert to 0-indexed
    message = list(message)  # Convert to list for mutability
    message[error_bit] = '1' if message[error_bit] == '0' else '0'  # Flip the bit
    return ''.join(message)

def main():
    message = input("Enter a binary message (length multiple of 4): ")
    if len(message) % 4 != 0:
        print("Error: Message length must be a multiple of 4.")
        return

    # Divide the message into slices of 4 bits
    message_slices = [message[i:i+4] for i in range(0, len(message), 4)]

    print("\nTransmitting Message Slices:")
    for slice in message_slices:
        print(slice)

    checksum = calculate_checksum(message_slices)
    print("Checksum:", checksum)

    # Add checksum to the message
    message += checksum

    # Introduce error
    if input("Do you want to introduce an error? (y/n) ") == 'y':
        message = introduce_error(message)

    # Receiver side
    print("\nReceived Message:", message)
    received_slices = [message[i:i+4] for i in range(0, len(message), 4)]
    received_checksum = calculate_checksum(received_slices)  # Exclude the received checksum
    print("Calculated Checksum:", received_checksum)

    if received_checksum == '0000':
        print("No error detected.")
    else:
        print("Error detected.")

if __name__ == "__main__":
    main()