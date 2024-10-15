# Function to encode a message by shifting letters
def encode_msg(msg, key):
    encoded_msg = ""
    for i in msg:
        # Check if the character is a letter
        if i.isalpha():
            # Determine if it's uppercase or lowercase
            if i.isupper():
                start = ord('A')
            else:
                start=ord('a')
            # Shift the letter and wrap around using modulo 26
            encoded_char = chr((ord(i) - start + key) % 26 + start)
            encoded_msg += encoded_char
        else:
            # If it's not a letter, leave it as it is
            encoded_msg += i
    return encoded_msg

# Function to decode a message by reversing the shift
def decode_msg(msg, key):
    return encode_msg(msg, -key)  # Decoding is simply encoding with a negative shift

# Function to handle user input and menu
def secret_code_generator():
    while True:
        # Display menu
        print("\nSecret Code Generator Menu:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Choose an option : ").strip()
        
        if choice == "1":
            msg = input("Enter the message to encode: ")
            key = int(input("Enter the shift number: "))
            print(f"Encoded message: {encode_msg(msg, key)}")
        
        elif choice == "2":
            msg = input("Enter the message to decode: ")
            key = int(input("Enter the shift number: "))
            print(f"Decoded message: {decode_msg(msg, key)}")
        
        elif choice == "3":
            print("Exiting program.")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

# Start the secret code generator
secret_code_generator()




























'''


def encode(x,k):
    en=""
    for char in x:
        if char.isalpha():
            en=chr((ord(char)+k)%26)
            en_code=+en
        else:
            en_code+=char
    return chr(en_code)
def decode(x,k):
    de=""
    for char in x:
        if char.isalpha():
            de=chr((ord(char)-k)%26)
            de_code=+de
        else:
            de_code+=char
    return chr(de_code)
def fun():
    while True:
        print("choose a option menu:")
        print("1.encode the msg")
        print("2.decode the msg")
        print("3.exit the code")
        choice=int(input("select a option:"))
        if choice==1:
            x=input("enter a text:")
            k=int(input("enter your shiftkey:"))
            print(f"encoded_msg:{encode(x,k)}")
        elif choice==2:
            x=input("enter a text:")
            k=int(input("enter your shiftkey:"))
            print(f"decoded_msg:{decode(x,k)}")
        elif choice==3:
            print("exiting code.")
            break
        else:
            print("invalid input,please choose option from 1 or 2 or 3.")

fun()
'''