import hashlib

input = "ojvtpuvg"
#input = "abc"
index = 0
password = '--------'
while password.find('-') != -1:
    prehash = input + str(index)
    md5hash = hashlib.md5(prehash.encode())
    if md5hash.hexdigest()[:5] == '00000':
        if md5hash.hexdigest()[5].isnumeric():
            if int(md5hash.hexdigest()[5]) <= 7 and password[int(md5hash.hexdigest()[5])] == '-':
                temp = list(password)
                temp[int(md5hash.hexdigest()[5])] = md5hash.hexdigest()[6]
                password = ''.join(temp)
    index += 1

print(password)