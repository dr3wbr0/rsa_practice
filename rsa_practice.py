#!/usr/bin/env  python3
"""
This is a custom python module made to demonstrate the math behind basic RSA implementation. Here is how to use it:
1. Choose 2 prime numbers. If needed use the gen_primes() function
2. Use gen_keypair(p1, p2) with two primes (arguments) and assign the returned public/private keypair to a variable
3. Use encrypt_msg(public_key, message) with keypair[0] and any three character string (bit size is limited)
4. Use decrypt_msg(private_key, cypher_text) with keypair[1] (second tuple from keypair) and encrypted message

Example:
    >> keypair = gen_keypair(929, 19697)
    >> print(my_keypair)
    [(18298513, 345669), (18298513, 1100397)]
    >> pubkey, privkey = keypair[0], keypair[1]
    >> cypher_text = encrypt_msg(pub_key, 'dog')
    >> print(cypher_text)
    15864656
    >> message = decrypt_msg(privkey, cypher_text)
    >> print(message)
    dog
"""

from math import sqrt
from random import randint


def str_to_int(m):
    my_msg = m.encode('utf-8')
    my_int = int.from_bytes(my_msg, 'little')
    return my_int


def int_to_str(b):
    my_int = b.to_bytes((b.bit_length() + 7) // 8, 'little')
    my_msg = my_int.decode('utf-8')
    return my_msg


def gcd(a, b) -> int:
    """Greatest common denominator for a and b"""
    while b != 0:
        t = b
        b = a % b
        a = t
    return int(a)


def lcm(a, b) -> int:
    """Least common multiple for a and b"""
    return int(abs(a*b)/gcd(a, b))


def is_coprime(a, b) -> bool:
    if gcd(a, b) == 1:
        return True
    return False


def gen_coprime(n) -> int:
    e = randint(3, int(n/2))
    while not is_coprime(e, n):
        e += 1
    return int(e)


def is_prime(n) -> bool:
    if n == 1:
        return False
    elif n == 2:
        return True
    for f in range(2, round(sqrt(n)) + 1):
        if n % f == 0:
            return False
    return True


def isprime(n: int) -> bool:
    """Primality test using 6k+-1 optimization"""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gen_primes(a, b):
    """Generate list of all primes between a and b"""
    prm = []
    for i in range(a, b):
        if isprime(i):
            prm.append(i)
    return prm


def mmi(e, ctf) -> int:
    """Modular multiplicative inverse for coprime e and
       Carmichael's totient function value"""
    i = 1
    while (ctf * i + 1) % e != 0:
        i += 1
    return int((ctf*i + 1) / e)


def gen_keypair(p, q):
    """Returns a list with two tuples"""
    if not isprime(p) or not isprime(q):
        raise ValueError("Numbers not prime")
    n = p*q
    ctf = lcm(p-1, q-1)
    e = gen_coprime(ctf)
    d = mmi(e, ctf)
    pubkey = (n, e)
    privkey = (n, d)
    return [pubkey, privkey]


def encrypt_msg(key, m):
    return (str_to_int(m)**key[1]) % key[0]


def decrypt_msg(key, c):
    return int_to_str((c**key[1]) % key[0])
