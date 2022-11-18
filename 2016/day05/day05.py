import hashlib

input = "ojvtpuvg"
#input = "abc"
index = 0
password = ''
while len(password) < 8:
    prehash = input + str(index)
    md5hash = hashlib.md5(prehash.encode())
    if md5hash.hexdigest()[:5] == '00000':
        password += md5hash.hexdigest()[5]
    index += 1

print(password)