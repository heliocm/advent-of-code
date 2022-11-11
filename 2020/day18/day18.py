target_input = open("input.txt" , "r")
expressions = target_input.read().split("\n")
del expressions[-1]

def find_subs(expression):
    subexpressions = []
    for i, character in reversed(list(enumerate(expression))):
        if character == ")":
            count = 1
            for k in range(i-1, -1, -1):
                if expression[k] == ")":
                    count = count + 1
                elif expression[k] == "(":
                    count = count - 1
                else: continue

                if count == 0:
                    subexpressions.append(expression[k:i+1])
                    break
    return subexpressions[::-1]

def calculate(expression):
    final = ""
    for i,character in list(enumerate(expression)):
        if character.isnumeric() and not expression[i+1].isnumeric():
            final = "(" + final + character + ")"
        else:
            final = final + character
    return eval(final)

total = 0
for expression in expressions:
    expression = expression.replace(" ", "")
    expression = "(" + expression + ") "
    previous = {}
    for each in find_subs(expression):
        if not each in previous:
            if len(find_subs(each)) == 1:
                previous[each] = calculate(each)
            else:
                auxiliar = each
                for number in dict(reversed(list(previous.items()))):
                    if number in auxiliar:
                        auxiliar = auxiliar.replace(number, str(previous[number]))
                previous[each] = calculate(auxiliar)
    total = total + previous[expression[:-1]]

print(total)