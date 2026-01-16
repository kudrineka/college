import hashlib
hash_function = hashlib.sha256(b'message') 
print (hash_function.digest_size) 

print (len(hash_function.digest()) * 8 )