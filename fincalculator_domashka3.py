# Калькулятор из 1 задания к 3 уроку. Файл fin_dz
filep = '../clone_mnog/files/'
filen = input("введите название файла из папки с данными: ")
# print(filen)
with open(filep+filen.strip()+'.txt') as f:
    lines = f.readlines()
    print(lines)
