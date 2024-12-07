import random

def print_forty_random_characters():
    
    characters = (
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '0123456789'
        '!@#$%^&*()_+-=[]{}|;:,.<>?'
    )
    
    
    random_characters = ''.join(random.choice(characters) for _ in range(40))
    
   
    print(random_characters)


print_forty_random_characters()
