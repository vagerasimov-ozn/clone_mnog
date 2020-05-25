# Калькулятор из 1 задания к 3 уроку. Файл fin_dz Результат fin_dz_rezult
filep = '../clone_mnog/files/'
filen = input("введите название файла из папки с данными: ")

with open(filep+filen.strip()+'.txt') as f:
    lines = f.readlines()
    dl = len(lines)

sum = 0
for line in lines:
    sum += int(line)

average = sum / dl
minimum = min(lines)
maximum = max(lines)

print(f" В этом файле сумма значений: {sum}\n среднее значение: {round(average,2)}\n \
минимальное значение: {minimum} максимальное значение: {maximum}")

rezultname = input("Введите название файла для сохранения результата: ")

with open(filep+rezultname.strip()+'.txt') as fr:
    file = open(filep+rezultname+".txt", "w")
    file.write(f" В этом файле сумма значений: {sum}\n среднее значение: {round(average,2)}\n \
минимальное значение: {minimum} максимальное значение: {maximum}")
# file.close()