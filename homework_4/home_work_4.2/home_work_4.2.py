# Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить пустым.

with open('file.txt', 'r') as input_file:

    even_file = open('even_numbers.txt', 'w')
    odd_file = open('odd_numbers.txt', 'w')

    content = input_file.read().split()

    for element in content:
        try:
            num = int(element)
            if num % 2 == 0:
                even_file.write(f"{num}\n")
            else:
                odd_file.write(f"{num}\n")
        except ValueError:
            pass

    even_file.close()
    odd_file.close()
