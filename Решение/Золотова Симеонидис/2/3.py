import hashlib
from hashlib import sha256 
message = b'message' 
hash_function = hashlib.sha256()  
hash_function.update(message)
print (hash_function.digest() == hashlib.sha256(message).digest())