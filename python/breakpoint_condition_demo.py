# Пример кода для демонстрации работы с breakpoint condition
# 1. Установите breakpoint здесь
# 2. Откройте настройки breakpoint и укажите условие
# 3. Запустите код в debug режиме
def process_numbers(nums):
    results = []
    for i, num in enumerate(nums):
        if num % 3 == 0 and num % 5 != 0:  # установите breakpoint здесь
            squared = num ** 2
            results.append(squared)
        else:
            print(f"Число {num} не подходит под условия.")
    return results


# Список чисел для обработки
numbers = [12, 15, 9, 25, 18, 30, 21, 10, 24, 33]

# Вызываем функцию обработки
processed_results = process_numbers(numbers)

# Печатаем результаты
print("Обработанные результаты:", processed_results)
