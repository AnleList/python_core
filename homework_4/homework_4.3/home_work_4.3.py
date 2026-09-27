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
            if char in string.whitespace:
                if current_word:
                    parts.append(('word', current_word))
                    current_word = ''
                current_delimiter += char
            else:
                if current_delimiter:
                    parts.append(('delimiter', current_delimiter))
                    current_delimiter = ''
                current_word += char
        # после выхода из цикла надо сохранить последние полученные элементы в наш словарь parts
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
