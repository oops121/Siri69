def rail_fence_encrypt(text):
    even_chars = []  
    odd_chars = []   
    
    for i, char in enumerate(text):
        if i % 2 == 0:
            even_chars.append(char)
        else:
            odd_chars.append(char)
    
    cipher = ''.join(even_chars + odd_chars)
    
    print("Cipher Text     :", cipher)
    
    return cipher, len(even_chars), len(odd_chars)

def rail_fence_decrypt(cipher, len_even, len_odd):
    even_chars = list(cipher[:len_even])
    odd_chars = list(cipher[len_even:])
    
    decrypted = []  
    
    for i in range(len(cipher)):
        if i % 2 == 0:
            decrypted.append(even_chars.pop(0))
        else:
            decrypted.append(odd_chars.pop(0))
    
    print("Decrypted Text  :", ''.join(decrypted))
    return ''.join(decrypted)



plain_text = "Meet Me After Toga Party"
print("Original Text    :", plain_text)

cipher_text, even_len, odd_len = rail_fence_encrypt(plain_text)

decrypted_text = rail_fence_decrypt(cipher_text, even_len, odd_len)



