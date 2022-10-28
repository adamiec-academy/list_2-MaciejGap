def cipher(text, shift):
    result = ""
    for character in text:
        if character == " ":
            result = result + character
        elif character.isupper():
            character = ord(character)
            character = character + shift
            if character > 90:
                character = character - 26
            character = chr(character)
            result = result + character
        else:
            character = ord(character)
            character = character + shift
            if character > 122:
                character = character - 26
            character = chr(character)
            result = result + character

    return result


def decipher(text, shift):
    pass
