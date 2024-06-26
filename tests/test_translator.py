import unittest
from src.translator import encrypt, decrypt

class TestTranslator(unittest.TestCase):

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(""), "")
    
    def test_encrypt_single_letter(self):
        self.assertEqual(encrypt("a"), ".-")
    
    def test_encrypt_multiple_letters(self):
        self.assertEqual(encrypt("hello"), ".... . .-.. .-.. ---")

    def test_encrypt_with_spaces(self):
        self.assertEqual(encrypt("hello world"), ".... . .-.. .-.. ---  .-- --- .-. .-.. -..")

    def test_decrypt_empty_string(self):
        self.assertEqual(decrypt(""), "")
    
    def test_decrypt_single_letter(self):
        self.assertEqual(decrypt(".-"), "A")
    
    def test_decrypt_multiple_letters(self):
        self.assertEqual(decrypt(".... . .-.. .-.. ---"), "HELLO")

    def test_decrypt_with_spaces(self):
        self.assertEqual(decrypt(".... . .-.. .-.. ---  .-- --- .-. .-.. -.."), "HELLO WORLD")
    
    def test_decrypt_invalid_code(self):
        self.assertNotEqual(decrypt(".... . .-.. .-.. ---   .-- --- .-. .-.. -..  ..."), "HELLO WORLD ")


if __name__ == '__main__':
    unittest.main()