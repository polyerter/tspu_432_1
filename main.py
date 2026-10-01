# print("Hello World!")
"""
текст комента
"""
a = "Hello World!"
print(a)

b = 54
c = 46
d = b + c

print(d)

f = 5.5
print(f)

print(type(a))
print(type(d))
print(type(f))

e: bool = True
print(e, type(e))

# создание списка
arr = [1, 2, 3, 4, 5]
print(arr, type(arr))

# получение элемента по индексу
print(arr[0] + arr[1])

# замена элемента по индексу
arr[4] = 6
print(arr)

# добавление в конец списка
arr.append(7)
print(arr)

# длина списка
print(len(arr))

arr_sum = 0
for i in arr:
    arr_sum += i
    print(f"Число: {i}")

print(arr_sum)
# n = 10
# n = n + 1
# n += 1
# print(n)