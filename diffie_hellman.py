def encrypt_integer(base, modulo, secret_integer):
    return pow(base, secret_integer) % modulo
