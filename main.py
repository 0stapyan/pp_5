def encryption(inputText, key):

    result = []
    for c in inputText:
        if 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + key) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + key) % 26 + ord('a')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') + key) % 10 + ord('0')))
        else:
            result.append(c)

    return ''.join(result)

def decryption(inputText, key):

    result = []
    for c in inputText:
        if 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') - key + 26) % 26 + ord('A')))
        elif 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') - key + 26) % 26 + ord('a')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') - key + 10) % 10 + ord('0')))
        else:
            result.append(c)

    return ''.join(result)


while True:

    operation = input("Do you want to encrypt text or decrypt? ((e) or (d))")

    if operation == 'e':
        inputText = input("Please enter a text to encrypt: ")
        key = int(input("Please enter a key: "))
        answer = encryption(inputText, key)
        print(f"Your encrypted message is: {answer}")

    elif operation == 'd':
        inputText = input("Please enter a text to decrypt: ")
        key = int(input("Please enter a key: "))
        answer = decryption(inputText, key)
        print(f"Your decrypted message is: {answer}")
