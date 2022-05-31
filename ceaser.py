alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def encript(text):
    coded_text = ""
    for char in text:
        index = alphabet.index(char)
        if index + shift > len(alphabet)-1:
            index = index - len(alphabet)
        coded_text += alphabet[index + shift]
    return coded_text

def decript(text):
    encoded_text = ""
    for char in text:
        index = alphabet.index(char)
        encoded_text += alphabet[index - shift]
    return encoded_text

text = input("type your text here: ").lower()
shift = int(input("Give me the shift amount: "))
print(encript(text))
print(decript(encript(text)))