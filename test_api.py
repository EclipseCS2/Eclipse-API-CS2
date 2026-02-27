from include.Api.parser import parse_offsets

# Вызываем парсер. 
# Так как локального файла нет, он ДОЛЖЕН пойти на GitHub.
offsets = parse_offsets()

if offsets:
    print("✅ Проверка пройдена!")
    print(f"Данные из GitHub: {offsets}")
else:
    print("❌ Ошибка: файл не скачался и не прочитался.")