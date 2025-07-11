...
2. Составить список, в который будут включены только согласные буквы и
привести их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль',
'Дели', 'Каир'].
...


def filter_consonants(word):
    consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    return ''.join([c.upper() for c in word if c.upper() in consonants])

words = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
result = [filter_consonants(word) for word in words]

print(result)  # ['ТТВ', 'МСКВ', 'ПКН', 'ПЛЦК', 'ВРСЛ', 'ДЛ', 'КР']
