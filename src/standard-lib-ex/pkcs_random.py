from pkcs11 import Mechanism

iv = session.generate_random(128)
ciphertext = key.encrypt(plaintext,
                         mechanism=Mechanism.AES_OFB,
                         mechanism_param=iv)
