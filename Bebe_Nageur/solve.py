from sympy import mod_inverse

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-!"

def decrypt(encrypted, a, b, len_charset):
    decrypted = ""
    a_inverse = mod_inverse(a, len_charset)
    for char in encrypted:
        x = charset.index(char)
        x = a_inverse * (x - b) % len_charset
        decrypted += charset[x]
    return decrypted

encrypted_flag = "-4-c57T5fUq9UdO0lOqiMqS4Hy0lqM4ekq-0vqwiNoqzUq5O9tyYoUq2_"
target_prefix = "404CTF"
len_charset = len(charset)


for a in range(2, len_charset):
    for b in range(1, len_charset):
        decrypted_flag = decrypt(encrypted_flag, a, b, len_charset)
        if decrypted_flag.startswith(target_prefix):
            print("FLAG:", decrypted_flag)
            break
