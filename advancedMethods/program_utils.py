import string
import random

class ProgramUtils:
    def generate_secret_key(self):
        letters, digits, spl_chr = string.ascii_letters, string.digits, string.punctuation
        secret_key = ''.join(random.choices(letters+digits+spl_chr, k=32))
        return secret_key