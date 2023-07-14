from secrets import token_bytes

from Cryptodome.Cipher import DES

key = token_bytes(8)


def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


nonce, ciphertext, tag = encrypt(input('Введите ваш текст: '))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Ваш полученный шифрованный текст: {ciphertext}')

if not plaintext:
    print('Сообщение повреждено!')
else:
    print(f'Исходный текст: {plaintext}')



