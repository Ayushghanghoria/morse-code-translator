from constants import MORSE_CODE_DICT, MORSE_TO_CHAR_DICT

def encrypt(message):
    """
    Encrypts a plain text message to morse code
    Add a space between letters to identify the morse code
    """
    encoded_message = ""
    message = message.upper()

    for letter in message:
        if letter != " ":
            encoded_message += MORSE_CODE_DICT[letter] + " "
        else:
            encoded_message += " "
    return encoded_message.strip()


def decrypt(message):
    """
    Decrypts a morse code message to plain text
    """
    decoded_message = ""
    # Each encoded letter is space seprated
    message = message.strip().split(" ")

    for codes in message:
        if codes:
            decoded_message += MORSE_TO_CHAR_DICT[codes]
        else:
            decoded_message += " "
    
    return decoded_message.strip()