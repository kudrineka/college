import zlib 
message = b'this is repetitious' * 42
checksum = zlib.crc32(message)
compressed = zlib.compress(message)
decompressed = zlib.decompress(compressed)
print (zlib.crc32(decompressed) == checksum)