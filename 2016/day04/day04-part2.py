target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def decrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        result += chr((ord(char) + s - 97) % 26 + 97)
    return result

for each in data:
    decrypted = ''
    encrypted_name = each.split('-')
    sector_id = int(encrypted_name[-1].split('[')[0])
    check_sum = encrypted_name[-1].split('[')[1][:-1]
    del encrypted_name[-1]
    for name in encrypted_name:
        decrypted += decrypt(name, sector_id) + ' '
    if 'northpole' in decrypted or 'north pole' in decrypted:
        print(decrypted, sector_id)
    else:
        pass
