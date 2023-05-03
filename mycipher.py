import sys

def caesar_cipher_encode(key:int, message: str) -> str:
    message = message.upper()
    ciphertext = ""
    count = 0
    
    for char in message:
        char_code = ord(char)
        if char_code < 65 or char_code > 90:
            continue
        
        if count % 50 == 0 and len(ciphertext) != 0:
            ciphertext += "\n"
        elif count % 5 == 0 and len(ciphertext) != 0:
            ciphertext += " "
            
        ciphertext += chr(65 + (char_code - 65 + key) % 26)
        count += 1
    
    return ciphertext

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide <key> and optionally <message>/Format: python3 mycipher.py <key> [<message>] < input_file")
        sys.exit(1)
    
    key = int(sys.argv[1])
    
    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        message = sys.stdin.read()
    
    print(caesar_cipher_encode(key, message))
    sys.exit(0)