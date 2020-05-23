#Лингва-Лео с рандомным запросом слов

import random

amount_of_words = input("Как много слов вы хотите занести в словарь: ")
aow = int(amount_of_words)
slovar = {}

for i in range(aow):
    key = input("Введите слово на английском:  ")
    value = input("Введите слово на русском: "
                  " ")
    slovar[key] = value
print("\n")

randomizer =  [i for i in slovar.keys()]
while len(randomizer)>0:
    random.shuffle(randomizer)
    print("Переведи слово ", randomizer[0], ": ")
    answer = input("Ваш вариант перевода:  ")
    # print(slovar[randomizer[0]])

    if slovar[randomizer[0]]==answer:
        print("Все верно! Лев сыт!  \n")
        randomizer.remove(randomizer[0])
    else:
        print("Не верно! А правильный ответ был", slovar[randomizer[0]],"\n")



# for key in slovar.keys():
#     print("Переведи слово ", key, ": ")
#     answer = input("Ваш вариант перевода: \n ")
#     if slovar[key] == answer:
#         print("Все верно! Лев сыт!")
#     else:
#         print("Не верно! А правильный ответ был", slovar[key])