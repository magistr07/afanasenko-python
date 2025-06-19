with open('text18-2.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("Содержимое файла:")
print(content)

punctuation_marks = ['.', ',', ';', ':', '!', '?', '—', '-', '(', ')', '"', "'"]
count = sum(content.count(mark) for mark in punctuation_marks)
print(f"\nКоличество знаков препинания: {count}")

lines = content.split('\n')
reversed_lines = [line for line in reversed(lines) if line.strip() != '']

with open('reversed_poem.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(reversed_lines))

print("\nФайл 'reversed_poem.txt' с обратным порядком строк успешно создан")
