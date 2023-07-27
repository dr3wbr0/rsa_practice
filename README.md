# RSA Practice Python Module
(This is for demonstration purposes **ONLY**. You should never roll your own crypto!)
#### This is a custom python module made to demonstrate the math behind basic RSA implementation. Here is how to use it:
1. Choose 2 prime numbers. If needed use the gen_primes() function
2. Use gen_keypair(p1, p2) with two primes (arguments) and assign the returned public/private keypair to a variable
3. Use encrypt_msg(public_key, message) with keypair[0] and any three character string (bit size is limited)
4. Use decrypt_msg(private_key, cypher_text) with keypair[1] (second tuple from keypair) and encrypted message

#### Example:
```
    >>> keypair = gen_keypair(929, 19697)
    >>> print(my_keypair)
    [(18298513, 345669), (18298513, 1100397)]
    >>> pubkey, privkey = keypair[0], keypair[1]
    >>> cypher_text = encrypt_msg(pub_key, 'dog')
    >>> print(cypher_text)
    15864656
    >>> message = decrypt_msg(privkey, cypher_text)
    >>> print(message)
    dog
```
If you want to learn more about RSA visit [RSA (cryptosystem) - Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
