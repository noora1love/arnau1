import os
import pandas as pd
from your_app.models import Tablecloth, Category  # Замените your_app на имя вашего приложения

# Путь к Excel-файлу
excel_file = '/SamaSite/static/excel/data.xlsx'

# Путь к папке с изображениями (если они уже загружены)
image_folder = '/SamaSite/static/images/'

# Чтение данных из Excel
try:
    data = pd.read_excel(excel_file)
except FileNotFoundError:
    print(f"Файл {excel_file} не найден!")
    exit()

# Перебор строк из Excel
for index, row in data.iterrows():
    # Получаем или создаем категорию
    category_name = row['category']
    category, _ = Category.objects.get_or_create(name=category_name)

    # Создаем запись Tablecloth
    tablecloth = Tablecloth(
        name=f"Клеёнка {index + 1}",
        description=row['description'],
        category=category,
        price=100.00
    )

    # Путь к изображению
    image_name = row['img']
    image_path = os.path.join(image_folder, image_name)

    # Проверяем, существует ли файл изображения
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            tablecloth.image.save(image_name, img_file, save=True)
    else:
        print(f"Изображение {image_name} не найдено. Пропуск.")

    print(f"Загружена запись: {tablecloth.name}")
