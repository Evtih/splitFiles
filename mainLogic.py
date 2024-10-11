import os
import chardet

def split_and_process_files(input_directory, output_directory, part_size):
    # Создание выходной папки, если она не существует
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Перебор файлов в папке
    for file_name in os.listdir(input_directory):
        if os.path.isfile(os.path.join(input_directory, file_name)):
            input_file_path = os.path.join(input_directory, file_name)

            # Определение кодировки файла
            with open(input_file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                encoding = result['encoding']

            # Чтение файла с определенной кодировкой
            with open(input_file_path, 'r', encoding=encoding) as f:
                content = f.readlines()  # Читаем построчно

            # Получаем базовое имя и расширение файла
            base_name = os.path.splitext(file_name)[0]
            ext = os.path.splitext(file_name)[1].lower()  # Получаем расширение

            # Разделение содержимого на части
            part_number = 1
            part_content = ""
            for line in content:
                part_content += line  # Добавляем строку к текущей части

                # Если размер текущей части превышает заданный размер, сохраняем
                if len(part_content.encode('utf-8')) >= part_size:
                    save_part(base_name, ext, part_number, part_content, output_directory)
                    part_number += 1
                    part_content = ""  # Сбрасываем текущую часть

            # Записываем оставшуюся часть, если она не пустая
            if part_content:
                save_part(base_name, ext, part_number, part_content, output_directory, is_last=True)

def save_part(base_name, ext, part_number, part_content, output_directory, is_last=False):
    if is_last and part_number == 1:
        part_file_name = f"{base_name}{ext}.txt"  # Нет номера части
    else:
        part_file_name = f"{base_name}{ext}Part{part_number}.txt"  # С номером части

    part_file_path = os.path.join(output_directory, part_file_name)
    
    # Записываем в файл
    with open(part_file_path, 'w', encoding='utf-8') as part_file:
        if not is_last or part_number > 1:
            part_file.write(f"{base_name}{ext} | {part_number} часть\n")
        else:
            part_file.write(f"{base_name}{ext}\n")  # Без номера части
        part_file.write("```vb\n")
        part_file.write(part_content)
        part_file.write("\n```\n")
        
        # Добавляем строку
        part_file.write("Какие последние 3 строки вы видите?\n")
