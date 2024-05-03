def calculate_redundant_bits(m):
    r = 0
    while 2 ** r < m + r + 1:
        r += 1
    return r

def generate_hamming_code(message):
    # print(message)
    m = len(message)
    r = calculate_redundant_bits(m)
    n = m + r
    hamming_code = ['0'] * n

    j = 0
    k = 0
    for i in range(1, n + 1):
        k = n - i + 1
        if (k & (k - 1)) != 0:  # Check if i is not a power of 2
            hamming_code[i - 1] = message[j]
            j += 1

    # print("hamming ocde: ", hamming_code)

    for i in range(r):
        parity_bit_pos = 2 ** i - 1  # Position of the parity bit
        hamming_code[n - parity_bit_pos - 1] = calculate_parity(hamming_code, parity_bit_pos)

    return hamming_code

def calculate_parity(code, parity_bit_pos):
    n = len(code)
    parity = 0
    for i in range(parity_bit_pos, len(code), 2 * (parity_bit_pos + 1)):
        for j in range(min(n - i - 1 - parity_bit_pos, len(code)), n - i):
            parity ^= int(code[j])

    return str(parity)

def introduce_error(code):
    error_pos = int(input(f"Enter the position to introduce error (1-{len(code)}): ")) - 1
    code[error_pos] = str(1 - int(code[error_pos]))  # Flip the bit to introduce error

def detect_and_correct_error(code):
    n = len(code)
    r = calculate_redundant_bits(n - 1)
    error_pos = 0
    for i in range(r):
        parity_bit_pos = 2 ** i - 1
        parity = calculate_parity(code, parity_bit_pos)
        if parity != '0':
            error_pos += parity_bit_pos + 1

    if error_pos > 0:
        print("Error detected at position:", n - error_pos + 1)
        code[n - error_pos] = str(1 - int(code[n - error_pos]))  # Correct the error

def main():
    message = input("Enter the message to transmit: ")
    hamming_code = generate_hamming_code(message)
    print("Transmitting stream of bits:", ''.join(hamming_code))

    introduce_error(hamming_code)
    print("Error introduced.")
    print("Received stream of bits:", ''.join(hamming_code))

    detect_and_correct_error(hamming_code)
    print("Error detected and corrected.")
    print("Corrected message:", ''.join(hamming_code))

if __name__ == "__main__":
    main()