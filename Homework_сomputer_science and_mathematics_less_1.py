import math
# Задача 1
alphabet = 64
message = 1000
size_of_one_simbol = math.log(alphabet, 2)
size = size_of_one_simbol * message
print(f"Задача №1 ответ: Объем информации = {int(size)} bite")

#Задача 2
message = 1024
mg = 1024*1024*8
size = mg/128
size_of_one_simbol = size/message
alphabet = 2**size_of_one_simbol
print(f"Задача №2 ответ: Алфавит  = 2 ^{int(size_of_one_simbol)} или {alphabet}" )

# Задача 3
message = 128 * 5
size_of_one_simbol = 16
size = size_of_one_simbol * message
kbite = 1024
bite = 8
sizeText = size/kbite/bite
print(f"Задача №3 ответ: Количество кбайт = {sizeText}")

# Задача 4
#         28|3
#         27|9|3
#         1 -9|3|3
#           0 -3|1
#              0
# 28 в троичной системе = 1001

# Задача 5
size = 72*1024*8
pixel = 24
imageSize = size/pixel
print(f"Задача №4 ответ: Размер изображения = {int(imageSize)} пикселей")
