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
