from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main():
    data = "blablablabla".encode()
    aes_key = get_random_bytes(16)

    cipher = AES.new(aes_key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(data)
    print(ciphertext)

    cipher = AES.new(aes_key, AES.MODE_CTR, nonce=cipher.nonce)
    message = cipher.decrypt(ciphertext)
    print("Message:", message.decode())


if __name__ == '__main__':
    main()