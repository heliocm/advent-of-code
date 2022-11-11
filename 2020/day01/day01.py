target_input = open("input.txt" , "r")
data = target_input.read().split("\n")

sum_result = 2020
threshold = sum_result // 2

greater_than = list()
lesser_than = list()

for number in data:
    if number != '':
        if int(number) >= threshold:
            greater_than.append(number)
        else:
            lesser_than.append(number)


for number in greater_than:
    number_to_find = sum_result - int(number)
    for candidate in lesser_than:
        if int(candidate) == number_to_find:
            print("Numbers are: {0} and {1}".format(number,candidate))
            print(int(number) * int(candidate))
            break

