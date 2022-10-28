def cipher(text, shift):
    result = ""
    for character in text:
        if character == " ":
            result = result + character
        elif character.isupper():
            character = ord(character)
            if character >= 90:
                character = character - 26
            character = character + shift
            character = chr(character)
            result = result + character
        else:
            character = ord(character)
            if character >= 122:
                character = character - 26
            character = character + shift
            character = chr(character)
            result = result + character

    return result


def decipher(text, shifter):
    pass

