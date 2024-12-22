cipher = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

def main():
    while True:
        option = input("Do you want to encrypt or decrypt? ")

        if option == "encrypt":
            encrypt_list = [char for char in input("What do you want to encrypt? ").upper()]
            encrypt(encrypt_list)
            break
        elif option == "decrypt":
            num_list = []

            while True:
                decrypt_num = input("Input number for decryption (enter for space): ")

                if decrypt_num.isdigit():
                    num_list.append(int(decrypt_num))
                elif decrypt_num == '':
                    num_list.append(' ')
                elif decrypt_num == "exit":
                    break
                else:
                    print("Invalid input. Please type an integer.")

            decrypt(num_list)
            break
        else:
            print("Invalid option, please choose from encrypt or decrypt")

def encrypt(encrypt_list):
    nums = []

    for char in encrypt_list:
        if char == ' ':
            nums.append(' ')
        elif char in cipher:
            nums.append(cipher[char])

    print(f"Your encrypted string: {nums}")

def decrypt(num_list):
    decrypted_list = []

    reverse_cipher = {value: key for key, value in cipher.items()}

    for num in num_list:
        if num == ' ':
            decrypted_list.append(' ')
        elif num in reverse_cipher:
            decrypted_list.append(reverse_cipher[num])

    print(f"Your decrypted string: {''.join(decrypted_list)}")


main()