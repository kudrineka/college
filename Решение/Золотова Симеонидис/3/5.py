from hashlib import blake2b
m = b'same message'
x = b'key x'
y = b'key y'
print ( blake2b(m, key=x).digest() == blake2b(m, key=y).digest())