import random


size1 = int(input("укажите размер первого массива: "))
size2 = int(input("укажите размер второго массива: "))

def create_new_array(size):
    new_array = []
    for i in range(size):
        array = random.randint(1,10)
        new_array.append(array)
    return new_array

first_array = create_new_array(size1)
second_array = create_new_array(size2)

def digits_in_both_arrays(a: list, b: list):
    first_list = set(a)
    second_list = set(b)
    both = []

    for i in first_list:
        for j in second_list:
            if i == j:
                both.append(i)

    return f'в массивах {a} и {b} содержатся одинаковые числа {both}'

print(digits_in_both_arrays(first_array, second_array))