
#переменная1 = input("How are you?")
#переменная2 = input("How long you ran?")
#print("Ti molodecs")

# print("Hello World", 5 * 5)


# number = 5

# print(number)


# haip1 = int(input("Введите первое число: "))

# haip2 = int(input("Введите второе число: "))


# print("Rezult:", haip1 + haip2)
# print("Rezult:", haip1 - haip2)
# print("Rezult:", haip1 / haip2)
# print("Rezult:", haip1 * haip2)
# print("Rezult:", haip1 ** haip2)
# print("Rezult:", haip1 // haip2)


# user_data = int(input("Введите свой возраст: "))

# if user_data > 18:
#     print("Успешно! ")
# if user_data < 18:
#     print("Не успешно! ")

# isHeppi = True

# if isHeppi:
#     print("Я счаслив! ")
# else: 
#     print("Я не счаслив! ")


# age = int(input("Введите свой возраст: "))

# if age >= 18:
#     print("Ура проходи! ")
# elif age >= 14:
#     print("Только в разрешением родителей! ")
# else:
#     print("Не подходишь по возрасту! ")



# grade = int(input("Какую оценку ты получил сегодня (от 2 до 5)?"))
# if grade == 5:
#     print("Ты супер-гений!")
# elif grade == 4:
#     print("Хорош! Чуть-чуть до пятерки не хватило.")
# else:
#     print("Надо бы подтянуть учебу...")




# age = int(input("Сколько тебе лет?"))
# if age < 10 or age > 80:
#     print("Вам полагается бесплатный билет!")
# else:
#     print("Обычный билет стоит 500 рублей.")
    



# counter = 1

# while counter <=5:
#     print("Ура!", counter)
#     counter = counter + 1

   

# password = ""

# while password != "1234":
#     password = input("Введите пароль: ")
# print("Доступ разрешен!")
    


# Food = ["Яблуко", "Груша", "Дыня"]
# Food[0]
# Food[1]
# Food[2]

# print(Food[1])

    


# for age in range(3,10):
#     print(age)


# o = 2
# while o <=15:
#     print(o)
#     o += 2
    



# age = True

# while age:
#     if input("Введите свой возраст: ") == "Stop":
#         age = False

# mani = None 

# for i in "nsbsnvshiruirhbdnbdklbklnskursjogjbsglmlkhlkjrgkmr;s;ng;lsng;sg":
#     if i == "k":
#         mani = True
#         break
# else:
#     mani = False

# print(mani)



# for i in range(1,5):
#     print("Приседание номер", i )
    




# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break






# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)



# correct_password = "77"
# user_password = None

# for i in range(1, 4):
#     user_password = input(f"Попытка №{i}. Введите код: ")
    
#     if user_password == correct_password:
#         print("Доступ разрешен! Двигатели запущены!")
#         break

#     elif user_password == "Чит" or user_password == "hack":
#         print("Система взломана! Сейф открылся сам!")
#         break

#     else:
#         if i == 3:
#             print("Попытки кончились! Включена блокировка.")
#         else:
#             print("Неверный код. Попробуй еще раз.")

         
             
        
    
# nums = [4, 5, 7, True, False, 0.5, [9, 5]]

# nums[3] = 50
# nums[4] = 12
# nums[5] = False


# print(nums[-1] [0])

    

# numbers = [1, 6, 9]

# numbers.append(100)
# numbers.insert(1, False)

# a = [1, 5, 3]

# numbers.extend(a)

# numbers.pop()
# numbers.remove(3)
# numbers.clear()



# print(numbers.count(5))
# print(len(numbers))



# num = [1, 5, 9, "19", True]

# for el in num:
#     el *= 2
#     print(el)



# a = int(input("Введите значения: "))

# user_list = []

# i = 0

# while i < a:
#     string = "Номер елемента №" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1 

# print(user_list)




# word = "wordhab"

# print(word.upper())
 







# sport = "football, basketball, skate"

# game = sport.split(', ')

# for i in range(len(game)):
#     game[i] = game[i].capitalize()

# rezultat = ", ".join(game)
# print(rezultat)





# word = "Football"

# print(word[0:4])

# lis = [4, 0, 34, "Hello", False , -1]

# print(lis[0:])

# print(lis[1:-1])


# user = ["Владислав", "Александр", "Константин"]

# for i in user:
#     short_name = i[0:3]
#     print(short_name + "***")


# cods = ["987654321", "111122223333", "55556666"]

# for i in cods:
#     cod = i[-4:]
#     print("***" + cod)


# words = ["Радар", "Шалаш", "Питон", "Довод", "Юнити"]

# for w in words:
#     clean_word = w.lower()
#     if clean_word == clean_word[::-1]:
#         print(f"{w} — это палиндром!")

#     else:
#         print(f"{w} — обычное слово.")


# loot = ["Меч", "Щит", "Зелье", "Монета", "Кристалл", "Топор"]

# last_items = loot[-3:]
# backpack = last_items[::-1]
# print(backpack)



# banned = ["чит", "бот", "взлом"]
# user_words = ["Привет", "я", "не", "ЧИТ", "честно"]
# for w in user_words:
#     clean_word = w.lower()

#     if clean_word in banned:
#         print(w[0] + "***")

#     else:
#         print(w)

        
# players = ["алекс", "ДАНЯ", "вЛАД", "макс"]

# for i in range(len(players)):
#     name = players[i]

#     players[i] = name[0].upper() + name[1:].lower()
# print(players)



# scores = [1500, 1250, 1100, 950, 800, 700, 500, 300]

# top_3 = scores[:3]

# for i in range(len(top_3)):
#     print(f"{i+1} место: {top_3[i]} ")




# name = "Владислав"
# surname = "Иванов"

# part1  = name[:3].lower()
# part2 = surname[:3].lower()
# nickname = part1 + part2 + "99"

# print(nickname)




# online_players = ["Diana", "Bogdan", "Nikita"]
# banned_words = ["чит", 'бот']

# new_name = input()

# if len(new_name) < 3:
#     print("Ошибка: ник слишком короткий!")
# else:
#     print("Длина никнейма подходит.")

#     clean_name = new_name.lower()
#     if clean_name in banned_words:
#         print("Ошибка: такой ник запрещен!")
#     else:
#         if new_name in online_players:
#             print("Ошибка: этот ник уже занят!")
#         else:
#             online_players.append(new_name)
#             print("Вы успешно зарегистрированы!")

# print(online_players)

     



# donators = ["Alex", "Max", "Danya", "Vova"]

# for i in donators:
#     promo = i[::-1].upper()
    
#     if i == "Max":
#         promo = promo + "VIP"

#     print(f"Игрок: {i}, Промокод: {promo}")
    
    
# cite = {1: 4} - словарь

# print(cite[1])




# person = {
#     'user_1': {
#         'first_name': 'Alex',
#         'last_name': 'Graf',
#         'age': 23,
#         'adress': ('г. Украина', 'ул. Никитина', '21'),
#         }
# }

# print(person['user_1']['age'])



# shop_position = (15, 42)
# shop_items = {
# "зелье": 50,
# "щит": 150,
# "меч" : 250,
# "лук": 300
# }

# print(f"Добро пожаловать в лавку!")
# print(f"Лавка находится на координатах: {shop_position}")

# shield_price = shop_items["щит"]

# print(f"Цена щита в лавке: {shield_price} золотых.")

# print(shop_items)



# boss = {
#     "name": "Дракон Сверкающий Скверны",
#     "hp": 5000,
#     "loot": ["золото", "кристалл", "чешуя", "ключ"]
# }
# dragon = boss["name"]
# items = boss["loot"]

# print(f"Босс: {dragon} побежден!") 
# print(f"Из него выпадает предметов: {len(items)}")

# for el in items:
#     print(f"- Награда: {el}")



# def name():
#     print("papa", 5, False)

# name()

# def name(world):
#     print(world, end="")
#     print("!")

# name("hi")
# name("Popa")

# def suma(a, b):
#     res = a + b
#     print("Rezultat: ", res)

# suma(7, 9)
# suma("h", "i")




# num = [5, 6, 9, 3]

# min = num[0]
# for el in num:
#     if el < min:
#         min = el

# print(min)

# num2 = [5.1, 6.5, 9.8, 3.1, 2.1]

# min1 = num2[0]
# for el in num2:
#     if el < min1:
#         min1 = el

# print(min1)


# def minimal(l):
#     min_namber = l[0]
#     for el in l:
#         if el < min_namber:
#                     min_namber = el
        
         

#     print(min_namber)


# num1 = [5, 6, 9, 3]
# minimal(num1)

# num2 = [5.1, 6.5, 9.8, 3.1, 2.1]
# minimal(num2)


# func = lambda x, y: x * y

# res = func (5, 2)
# print(res)

# def count_discount(price):
#     final_price = price * 0.9
#     print(final_price)

# count_discount(100)
# count_discount(500)



# count_lambda_discount = lambda price: price * 0.9
#
# print(count_lambda_discount(100))
# print(count_lambda_discount(500))



# def say_hello(name):
#     text = f"[{name}] говорит: Привет, путник!"
#     print(text)


# say_hello("Рыцарь")   
# say_hello("Маг")





# def hello(name):
#     text = f"[{name}] говорит: Привет Булка!"
#     print(text)

# hello("Sasha")





# def check_level(player_dict):

#     name = player_dict["name"]
#     lvl = player_dict["lvl"]

#     if lvl >= 10:
#         print(f"Игрок {name} готов к рейду! (Уровень: {lvl})")
#     else:
#         print(f"Игрок {name} еще слишком слаб. (Уровень: {lvl})")


# players = [
#     {"name": "Warrior_Alex", "lvl": 15},
#     {"name": "Warrior_Boris", "lvl": 9},
#     {"name": "Warrior_Nike", "lvl": 23}
# ]

# shout_name = lambda text: text.upper()

# for i in players:
#     i["name"] = shout_name(i["name"])
#     check_level(i)




# zelya = [20, 50, 110, 15]

# def check_price(price):

#         if price > 100:
#             print("Это дорогое зелье")
#         else:
#             print("Это дешевое зелье")
            
# for i in zelya:
#     check_price(i)



# krit = [40, 15, 60, 25]

# def apply_damage(damage):

#     if damage >= 50:
#             print(f"КРИТ! Нанесено уронa: {damage * 2}")
#     else:
#           print(f"Обычный удар. Нанесено урона: {damage}")
        
# for i in krit:
#       apply_damage(i)
           




# lut = ["Меч", "Хлам", "Зелье", "Хлам", "Щит"]


# def clean_inventory(pridmet):

#     if pridmet == "Хлам":
#         print("Вы выбросили хлам")
#     else:
#         print(f"Предмет {pridmet} оставлен в рюкзаке")

# for i in lut:
#     clean_inventory(i)

        


# data = input("Введите текст: ")


# file = open('text.txt', "w")

# file.write('hello')

# file.close()


# data = input("Введите текст: ")

# file = open('User/alex/Desktop/Proga/text.txt', "w")

# file.write(data)

# file.close()




# x = 0 
# while x == 0:
#     try: 
#         x = int(input("Введите число: "))
#         x += 5
#         print(x)
#     except ValueError:
#         print("Введите лучше число!")




# while  True:
#     try:
#         age = int(input("Введите свой возраст: "))

#         if age < 0 or age > 120:
#             raise Exception
        
#         print(f"Отлично, твой возраст: {age}")
#         break
#     except ValueError:
#         print("Ошибка! Нужно вводить только цифры!")
#     except Exception:
#         print("Попробуй еще раз!")





# def greet_user(personag):
#     print(f"Добро пожаловать в игру, {personag}")
    


# greet_user("Leon")



# def get_crit_damage(base_damage):
#     return base_damage * 1.5
    

# final_damage = get_crit_damage(100)
# print(final_damage)






# try:
#     with open('text.txt', 'r', encoding='utf8') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('Фаил не найден')




# text = input("Что сделал персонаж? ")
# with open("log.txt", "a", encoding='utf8') as file:
#     file.write(text + '\n')






# def save_player_age():
#     while True:
#         try:
#             age = int(input("Сколько вам лет?"))

#             if age == 0 or age > 120:
#                 raise Exception

#             with open("age.txt", "w") as file:
#                 file.write(str(age))

#             break

#         except ValueError:
#             print("Ошибка: Нужно вводить только цифры!")
#         except Exception:
#             print("Ошибка: Невероятный возраст!")


# save_player_age()



# import random

# dice = random.randint(1, 6)
# print(f"На кубике выпало: {dice}")



# import time
# print("Маг кастует заклинание...")

# time.sleep(3)
# print("Бум! Заклинание сработало через 3 секунды!")



# import math
# damage = 125.3

# final_damage = math.ceil(damage)
# print(f"Критичекий урон: {final_damage}")




# class People:
#     name = None
#     age = None
#     isHeppy = None

# People1 = People()
# People1.name = "Mary"
# People1.age = 24
# People1.isHeppy = True

# People2 = People()
# People2.name = "Alex"
# People2.age = 23
# People2.isHeppy = False

# print(People1.name, People1.age, People1.isHeppy)
# print(People2.name, People2.age, People2.isHeppy)






# class People:
#      name = None
#      age = None
#      isHeppy = None

#      def set_data(self, name, age, isHeppy):
#           self.name = name
#           self.age = age
#           self.isHeppy = isHeppy

#      def get_date(self):
#         print(self.name, "age:", self.age, ". Heppy:", self.isHeppy)


# People1 = People()
# People1.set_data("Mary", 24, True)

# People2 = People()
# People2.set_data("Alex", 23, False)


# People1.get_date()
# People2.get_date()








# class People:
#      name = None
#      age = None
#      isHeppy = None

#      def __init__(self, name, age, isHeppy):
#          self.name = name
#          self.age = age
#          self.isHeppy = isHeppy
    
#      def set_data(self, name, age, isHeppy):
#           self.name = name
#           self.age = age
#           self.isHeppy = isHeppy

#      def get_date(self):
#         print(self.name, "age:", self.age, ". Heppy:", self.isHeppy)


# People1 = People("Mary", 24, True)

# People2 = People("Alex", 23, False)



# People1.get_date()
# People2.get_date()




# class Hero:
#      def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

# leon = Hero("Leon", 100)

# jessica = Hero("Jessica", 120)

# print(f"Имя героя: {leon.name}, Здоровье: {leon.hp}")
# print(f"Имя героя: {jessica.name}, Здоровье: {jessica.hp}")







# class Hero:
#      def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#      def attack(self, enemy):
#          enemy.hp = enemy.hp - 20
#          print(f"⚔️ {self.name} атаковал {enemy.name}!")

# leon = Hero("Leon", 100)
# jessica = Hero("Jessica", 120)

# leon.attack(jessica)
# jessica.attack(leon)



# print(f"У {jessica.name} осталось {jessica.hp} ХП")
# print(f"У {leon.name} осталось {leon.hp} ХП")






# import random


# class Hero:

#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp

#     def attack(self, enemy):
#         damage = random.randint(10, 30)
#         enemy.hp = enemy.hp - damage
        
#         print(f"⚔️ {self.name} нанес {damage} урона {enemy.name}!")

# leon = Hero("Leon", 100)
# jessica = Hero("Jessica", 120)


# while True:

#     leon.attack(jessica)

#     if jessica.hp <= 0:
#         print("Джессика погибла! Леон победил!")
#         with open("battel_log.txt", "a", encoding="utf-8") as file:
#             file.write("В этой битве победил Леон!\n")
#         break 

#     jessica.attack(leon)

#     if leon.hp <= 0:
#         print("Леон погибл! Джесика победила!")
#         with open("battel_log.txt", "a", encoding="utf-8") as file:
#             file.write("В этой битве победила Джессика!\n")
#         break


# print(f"У {jessica.name} осталось {jessica.hp} ХП")



# class Building:

#     year = None
#     city = None

#     def __init__(self, year, city):
#         self.year = year
#         self.city = city


#     def get_info (self):
#         print("Years:", self.year, ". City:", self.city)


# class School(Building):
#     pupils = 0

#     def __init__(self, pupils, year, city):
#         super().__init__(year, city)
#         self.pupils = pupils


# class House(Building):
#     pass

# class Shop(Building):
#     pass



# school = School(100, 2000, "Ukrain")
# house = Building(2000, "Ukrain")
# shop = Building(2000, "Ukrain")

# school.get_info()
# house.get_info()
# shop.get_info()




# import webbrowser

# def open_url(url):
#     webbrowser.open(url)

# open_url("https://animevost.org/tip/tv/3324-shangri-la-frontier-kusoge-hunter-kamige-ni-idoman-to-su-2nd-season.html")

