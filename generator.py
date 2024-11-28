# generator.py

import random
import string

class PasswordGenerator:
    def __init__(self, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
        self.use_uppercase = use_uppercase
        self.use_lowercase = use_lowercase
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def generate(self, length):
        character_pool = ''
        if self.use_uppercase:
            character_pool += string.ascii_uppercase
        if self.use_lowercase:
            character_pool += string.ascii_lowercase
        if self.use_digits:
            character_pool += string.digits
        if self.use_symbols:
            character_pool += string.punctuation

        if not character_pool:
            raise ValueError("Trebuie să selectați cel puțin un tip de caractere.")

        password = ''.join(random.choice(character_pool) for _ in range(length))
        return password
