# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

raw = input('Insert numbers with a space:  ').split()
unique = []
for i in raw: 
        if raw.count(i) == 1: unique.append(i)
# print(f'Unique element: {unique}')
print ('Unique element(s): ',','.join(unique))