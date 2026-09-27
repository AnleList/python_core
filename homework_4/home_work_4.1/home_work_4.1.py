# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку.

file_data = open('file.txt', 'r')
number_data = []

content = file_data.read().split()
file_data.close()
    
last_all_data_element_index = len(content) - 1
    
print(f"Первый элемент: {content[0]}")
print(f"Второй элемент: {content[1]}")
print(f"Предпоследний элемент: {content[last_all_data_element_index - 1]}")
print(f"Последний элемент: {content[last_all_data_element_index]}")

for element in content:
    try:
        number_data.append(float(element))
    except ValueError:
        pass

last_digits_data_element_index = len(number_data) - 1

if last_digits_data_element_index < 3:
    print("Ошибка: в файле меньше 4 чисел.")
