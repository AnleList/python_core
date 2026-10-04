# Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку.

with open('file.txt', 'r') as input_file:
    number_data = []

    content = input_file.read().split()
    for element in content:
        try:
            number_data.append(float(element))
        except ValueError:
            pass
    if len(number_data) < 3:
        print("Ошибка: в файле меньше 4 чисел.")
    else:
        last_all_data_element_index = len(content) - 1

        print(f"Первый элемент: {content[0]}")
        print(f"Второй элемент: {content[1]}")
        print(f"Предпоследний элемент: {content[last_all_data_element_index - 1]}")
        print(f"Последний элемент: {content[last_all_data_element_index]}")

