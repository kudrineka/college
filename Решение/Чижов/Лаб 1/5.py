from hashlib import sha256
message = b'message'
hash_function = sha256(message)
print (hash_function.hexdigest())