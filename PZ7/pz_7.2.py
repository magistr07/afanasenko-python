...
Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
расставлены правильно (то есть каждой открывающей соответствует одна
закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
в которой расположена первая ошибочная закрывающая скобка, или, если
закрывающих скобок не хватает, число —1.
...


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
