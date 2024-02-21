#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def min_moves(nums):
    if not nums:
        return 0
    
    average_num = sum(nums) // len(nums)  # Находим среднее значение
    moves = 0
    
    for num in nums:
        moves += abs(num - average_num)  # Считаем количество ходов
    
    return moves

if __name__ == "__main__":
    # Проверка, что передан файл в аргументах командной строки
    if len(sys.argv) != 2:
        print("Usage: python program.py input_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Чтение чисел из файла
    with open(input_file, 'r') as file:
        # Прочитать все строки из файла
        lines = file.readlines()
        
        # Преобразовать каждую строку в целое число и добавить в список nums
        nums = [int(num) for num in lines]
    
    # Вывод результата
    print("Минимальное количество ходов:", min_moves(nums))

