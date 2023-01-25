# Вариант 1 - через переменную
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")

print("Вас зовут: " + last_name + " " + first_name)

# Вариант 2 - через функцию
def greet(first_name, last_name):
    print("Вас зовут: " + last_name + " " + first_name)

greet("Татьяна", "Мохначева")