import cmd
from src.translator import encrypt, decrypt

class MorseCodeCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MorseCode Translator. Type "help" for available commands.\n\nEnter the test without quotes. e.g. encode hello world'


    def do_encode(self, line):
        """Encode the text to Morse code."""
        encoded_message = encrypt(line)
        print(f"Morse Code: {encoded_message}")

    def do_decode(self, line):
        """Decode the Morse code to text."""
        decoded_message = decrypt(line)
        print(f"Decoded Text : {decoded_message}")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MorseCodeCLI().cmdloop()
