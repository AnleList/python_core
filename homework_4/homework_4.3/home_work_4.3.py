# Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

import string

with open('file.txt', 'r+') as file:
    content = file.read()


    def split_with_delimiters(text):
        parts = []
        current_word = ''
        current_delimiter = ''

        for char in text:
            if char in string.whitespace:  # если символ является делителем
                if current_word:  # и слово не пусто
                    parts.append(('word', current_word))  # кладём наше слово в словарь
                    current_word = ''  # слово сохранено в словарь - переменную очищаем
                current_delimiter += char  # сивол (делитель) сохраняем/добавляем как продолжение в переменную в любом случае
            else:  # если символ не является делителем, т е является частью слова
                if current_delimiter:  # и делитель уже есть
                    parts.append(('delimiter', current_delimiter))  # кладём наш делитель в словарь
                    current_delimiter = ''  # делитель сохранён в словарь - переменную очищаем
                current_word += char  # сивол, как часть слова, сохраняем в переменную в любом случае
        # после выхода из цикла надо сохранить последние полученные элементы в наш словарь
        if current_word:
            parts.append(('word', current_word))
        if current_delimiter:
            parts.append('delimiter', current_delimiter)

        return parts


    typified_parts = split_with_delimiters(content)

    result_parts = []
    for part_type, part_value in typified_parts:
        if part_type == 'word':
            try:
                result_parts.append(str(float(part_value) ** 2))
            except ValueError:
                result_parts.append(part_value)
        else:  # если part_type == 'delimiter'
            result_parts.append(part_value)

    result = ''.join(result_parts)

    file.seek(0)
    file.truncate()
    file.write(result)
