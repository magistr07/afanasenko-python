...
Из текстового файла (writer.txt) выбрать фамилии писателей и годы жизни, а также
произведения ими написанные. Посчитать общее количество произведений в данном
файле.
...

import re

def parse_writers(file_path):
    writers = []
    total_works = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
    
           match = re.match(r"^([^()]+)\((\d{4}-\d{4})\):\s*(.+)$", line.strip())
            if not match:
                continue
            
            full_name = match.group(1).strip()
            surname = full_name.split()[-1] 
            years = match.group(2)
            works = [work.strip() for work in match.group(3).split(',')]
            
            writers.append({
                'surname': surname,
                'years': years,
                'works': works
            })
            total_works += len(works)
    
    return writers, total_works

file_path = 'writer.txt'
writers, total_works = parse_writers(file_path)

for writer in writers:
    print(f"{writer['surname']} ({writer['years']}): {', '.join(writer['works'])}")

print(f"\nОбщее количество произведений: {total_works}")
