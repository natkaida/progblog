import os

# Указываем шаблоны для поиска и замены
replacements = {
    'static': 'progblog/static',
    'media': 'progblog/media'
}

# Получаем текущую директорию
current_dir = os.getcwd()

# Проходим по всем файлам в текущей директории и ее поддиректориях
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # Проверяем, является ли файл HTML-файлом
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            # Открываем HTML-файл и считываем его содержимое
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Проверяем, есть ли в файле строки для замены
            updated_content = content
            for old_string, new_string in replacements.items():
                if old_string in updated_content:
                    # Заменяем все вхождения old_string на new_string
                    updated_content = updated_content.replace(old_string, new_string)

            # Если были изменения, перезаписываем файл с обновленным содержимым
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Изменения внесены в файл: {file_path}")
