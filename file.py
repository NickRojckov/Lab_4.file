import os
# -*- coding: utf-8 -*-
my_file = open('F1.txt', 'w')
my_file2 = open('snake.txt', 'w')
text_for_file = 'Hello World!!!\n'
text_for_file1 = 'I am Nick\n'
text_for_file2 = 'I am a programmer\n'
text_for_file3 = 'I like this work)'
my_file.write(text_for_file)
my_file.write(text_for_file1)
my_file.write(text_for_file2)
my_file.write(text_for_file3)
my_file2.write(text_for_file1)
my_file2.write(text_for_file3)
try:
    my_file = open('F1.txt', "rb")
    b = my_file.read(1)
    str = ""
    while True:
        b = my_file.read(1)
        if b == b'':
            break
        str += b.hex()
    print(str)
    my_file.close()
except IOError:
    print('error')

# Закрываем файл
my_file.close()