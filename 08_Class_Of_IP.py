def identify_ip_class(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')

    # Convert each octet to integer
    octets = [int(octet) for octet in octets]

    # Check if the IP address is valid
    if len(octets) != 4 or any(octet < 0 or octet > 255 for octet in octets):
        print("Invalid IP address")
        return

    # Identify the class of the IP address
    first_octet = octets[0]
    if 1 <= first_octet <= 126:
        print("Class A")
    elif 128 <= first_octet <= 191:
        print("Class B")
    elif 192 <= first_octet <= 223:
        print("Class C")
    elif 224 <= first_octet <= 239:
        print("Class D (Multicast)")
    elif 240 <= first_octet <= 255:
        print("Class E (Reserved)")
    else:
        print("Unknown")


def main():
    ip_address = input("Enter the IP address in dotted decimal format: ")
    identify_ip_class(ip_address)


if __name__ == "__main__":
    main()
