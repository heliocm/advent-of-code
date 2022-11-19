import string
target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def extract_hypernet_sequences(address):
    sequences = []
    remanescent = address
    while remanescent.find('[') != -1:
        sequences.append(remanescent[remanescent.index('[')+1:remanescent.index(']')])
        remanescent = remanescent.replace(remanescent[remanescent.index('['):remanescent.index(']')+1], ' ')
    return sequences, remanescent

def check_aba(address_without_brackets):
    abas = []
    for i in range(1,len(address_without_brackets)-1):
        if address_without_brackets[i] != address_without_brackets[i+1] and \
           address_without_brackets[i-1] == address_without_brackets[i+1]:
           abas.append(address_without_brackets[i-1]+address_without_brackets[i]+address_without_brackets[i+1])
    return abas

def check_bab(sequences, abas):
    for each in sequences:
        for aba in abas:
            bab = aba[1]+aba[0]+aba[1]
            if bab in each:
                return True
    return False

def support_SSL(address):
    (sequences, remanescent) = extract_hypernet_sequences(address)
    abas = check_aba(remanescent)
    if abas != []:
        if check_bab(sequences, abas):
            return True
        else:
            return False
    else:
        return False

answer = 0

for each in data:
    if support_SSL(each):
        answer += 1
    else: 
        pass
print(answer)