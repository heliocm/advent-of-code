import hashlib

input = "ojvtpuvg"

result = hashlib.md5(input.encode())

print(result.hexdigest())