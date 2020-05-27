# Таблица умножения
arr1 = (1,2,3,4,5,6,7,8,9)
arr2 = arr1
i=0
while (i <=8):
    j=0
    while (j <=8):
        print(str(arr1[j]) + ' * ' + str(arr2[i]) + ' = ' + str(arr1[j]*arr2[i]),
              end=' '*(20-len(str(arr1[j]) + ' * ' + str(arr2[i]) + ' = ' + str(arr1[j]*arr2[i]))))
        j +=1
    i += 1
    print(end='\n')