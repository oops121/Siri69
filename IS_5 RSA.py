import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    
    public, private = generate_keypair(p, q)
    
    print("Public key: ", public)
    print("Private key: ", private)
    
    message = input("Enter a message to encrypt: ")
    
    encrypted_message = encrypt(public, message)
    print("Encrypted message: ", ''.join(map(lambda x: str(x), encrypted_message)))
    
    decrypted_message = decrypt(private, encrypted_message)
    print("Decrypted message: ", decrypted_message)


