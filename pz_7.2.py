def check_brackets(s):
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  
        elif char == ')':
            if not stack:
                return i + 1  
            stack.pop()  
    if not stack:
        return 0  
    else:
        return -1
s = input("Введите строку: ")
result = check_brackets(s)
print(result)
