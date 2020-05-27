#Еще не сделана. В работе.

def palindrome(data):
    data = data.replace(' ','').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'
    # print(data[::-1])

data = input()
palindrome(data)