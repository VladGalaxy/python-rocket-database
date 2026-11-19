# ==========================================
# Проект: База данных ракет (Rocket Database)
# Автор: VladGalaxy
# Описание: Консольное приложение для управления 
# списком ракет с использованием методов списков.
# ==========================================

# Инициализируем пустой список для хранения базы ракет
rocket_db = ["Союз", "Протон", "Ангара", "Восток"]
print("База данных инициализирована. Добро пожаловать!")

while True:
    print("\n--- МЕНЮ УПРАВЛЕНИЯ ---")
    print("1. Показать все ракеты")
    print("2. Добавить ракету в конец")
    print("3. Вставить ракету на позицию")
    print("4. Удалить ракету по имени")
    print("5. Удалить последнюю ракету")
    print("6. Отсортировать по алфавиту")
    print("7. Фильтр по первой букве")
    print("8. Очистить базу")
    print("0. Выход")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        if len(rocket_db) == 0:
            print("База пуста.")
        else:
            print(f"В базе {len(rocket_db)} ракет(ы):")
            # Используем метод join для красивого вывода через стрелочку
            print(" -> ".join(rocket_db))
            
    elif choice == "2":
        new_rocket = input("Введите название ракеты: ").strip().capitalize()
        if new_rocket:
            rocket_db.append(new_rocket) # Добавляем в конец
            print(f"Ракета '{new_rocket}' добавлена.")
            
    elif choice == "3":
        new_rocket = input("Введите название: ").strip().capitalize()
        try:
            pos = int(input(f"На какую позицию вставить (от 0 до {len(rocket_db)})? "))
            rocket_db.insert(pos, new_rocket) # Вставляем на позицию
            print(f"Ракета '{new_rocket}' вставлена на позицию {pos}.")
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            
    elif choice == "4":
        rem_rocket = input("Какую ракету удалить? ").strip().capitalize()
        if rem_rocket in rocket_db: # Проверка наличия через in
            rocket_db.remove(rem_rocket) # Удаляем по значению
            print(f"Ракета '{rem_rocket}' удалена.")
        else:
            print("Такая ракета не найдена.")
            
    elif choice == "5":
        if len(rocket_db) > 0:
            popped = rocket_db.pop() # Удаляем и возвращаем последний элемент
            print(f"Удалена последняя ракета: {popped}")
        else:
            print("База пуста, нечего удалять.")
            
    elif choice == "6":
        rocket_db.sort() # Сортируем по алфавиту
        print("База отсортирована по алфавиту.")
        
    elif choice == "7":
        letter = input("Введите первую букву для поиска: ").strip().upper()
        # Используем списочное выражение (List Comprehension) для фильтрации
        filtered = [r for r in rocket_db if r.startswith(letter)]
        
        if filtered:
            print(f"Найдено {len(filtered)} совпадений:")
            print(*filtered, sep="\n") # Вывод каждого с новой строки
        else:
            print("Ничего не найдено.")
            
    elif choice == "8":
        rocket_db.clear() # Полная очистка списка
        print("База данных очищена.")
        
    elif choice == "0":
        print("Завершение работы. Удачи!")
        break # Выходим из цикла while
        
    else:
        print("Неверный ввод, попробуйте снова.")
