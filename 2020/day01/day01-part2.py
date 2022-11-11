target_input = open("input.txt" , "r")
data = target_input.read().split("\n")

sum_result = 2020


greater_than = list()
lesser_than = list()

for pivot in data:
    if pivot != '':
        new_sum = sum_result - int(pivot)
        threshold = new_sum // 2
        for number in data:
            if number != '':
                if int(number) >= threshold:
                    greater_than.append(number)
                else:
                    lesser_than.append(number)


        for number in greater_than:
            number_to_find = new_sum - int(number)
            for candidate in lesser_than:
                if int(candidate) == number_to_find:
                    print("Numbers are: {0} ,{1} ,{2}".format(pivot,number,candidate))
                    print(int(pivot) * int(number) * int(candidate))
                    break

