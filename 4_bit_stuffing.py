def bit_stuffing(data, flag_pattern):
    cnt = flag_pattern.count("1")
    ans = ""
    cnt1 = 0

    for i in range(0, len(data)):
        if data[i] == "1":
            cnt1 += 1
            ans += "1"
            if cnt1 == cnt - 1:
                ans += "0"
                cnt1 = 0
        else:
            cnt1 = 0
            ans += "0"

    return ans


def bit_destuffing(data, flag_pattern):
    cnt = flag_pattern.count("1")
    ans = ""
    cnt1 = 0
    i = 0
    while i < len(data):
        if data[i] == "1":
            cnt1 += 1
            ans += "1"
            if cnt1 == cnt - 1:
                cnt1 = 0
                i += 1
        else:
            cnt1 = 0
            ans += "0"
        i += 1
    return ans


def main():
    data = input("Enter data to be transmitted: ")
    flag_pattern = input("Enter flag pattern: ")

    stuffed_data = bit_stuffing(data, flag_pattern)
    print("Stuffed data:", stuffed_data)

    choice = input("Do you want to de-stuff the data? (yes/no): ").lower()
    if choice == "yes":
        destuffed_data = bit_destuffing(stuffed_data, flag_pattern)
        print("De-stuffed data:", destuffed_data)
    else:
        print("Exiting...")


if __name__ == "__main__":
    main()