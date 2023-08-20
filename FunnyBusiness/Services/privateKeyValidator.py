from Crypto.PublicKey import RSA
from base64 import b64decode, b64encode
from binascii import Error as BinasciiError
from Crypto.PublicKey import RSA
import base64

def is_valid_rsa_key(key_string):
    
        try:
            return base64.b64encode(base64.b64decode(key_string)) == key_string.encode()
        except Exception:
            return False






























    # try:
    #     def wrap(text, width=64):
    #         return '\n'.join(text[i:i+width] for i in range(0, len(text), width))

    #     def convert_key(base64_key):
    #         pem_key = '-----BEGIN RSA PRIVATE KEY-----\n'
    #         pem_key += wrap(base64_key)
    #         pem_key += '\n-----END RSA PRIVATE KEY-----'
    #         return RSA.import_key(pem_key)

    #     rsa_key = convert_key(key_string)

    #     # Now you can use rsa_key with the pycryptodome library.
    #     # Requirement 1: It should be a valid base64 string
    #     decoded_string = b64decode(rsa_key)
    #     # Requirement 2: It should represent a valid RSAParameters structure
    #     key = RSA.import_key(decoded_string)
    
    # except BinasciiError or ValueError:
    #     print("Provided key is invalid")
    #     return False

    # # Requirement 3: It should match a valid public key
    # # In this case, we're assuming that the corresponding public key
    # # is derived from the private key and that the private key is therefore valid.
    # # In a real-world scenario, you would need to check the private key against a known public key.

    # # Requirement 4: It should meet security requirements
    # if key.size_in_bits() < 2048:
    #     print("Provided key is invalid")
    #     return False

    # print("Key meets all requirements.")
    # return True

