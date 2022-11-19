import string
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def support_TLS(address):
    if address.find('[') != -1:
        if check_abba(address[address.index('[')+1:address.index(']')]):
            return False
        else:
            return support_TLS(remove_brackets(address))
    else:
        return check_abba(address)

def check_abba(address_without_brackets):
    for i in range(1,len(address_without_brackets)-2):
        if address_without_brackets[i]==address_without_brackets[i+1] and \
           address_without_brackets[i-1] == address_without_brackets[i+2] and \
           address_without_brackets[i-1] != address_without_brackets[i]:
            return True 
    return False

def remove_brackets(address):
    new_address = address
    if new_address.find('[') != -1:
        new_address = new_address.replace(new_address[new_address.index('['):new_address.index(']')+1], ' ')
    return new_address

answer = 0

for each in data:
    if support_TLS(each):
        answer += 1
    else: 
        pass

print(answer)
