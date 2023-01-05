list_input = eval(input())
print(list_input)
operators = ['+', '-', '/', '*']
array = []
r = 0
for j in list_input:
    if j not in operators:
        array += [j]
    else:
        b = int(array.pop())
        a = int(array.pop())
        match j:
            case "+": r = (a+b)
            case "-": r = (a-b)
            case "/": r = (int(a / b))
            case "*": r = (a * b)
        array.append(r)
print(array[0])



