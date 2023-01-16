# В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»


def Open_File(nameFile, i):
     data = open('Icecream.txt', mode='r', encoding='utf-8')
     phrase = data.readlines()
     data.close()
     phrase = [i.strip() for i in phrase]
     list = phrase[i].split(', ')
     return set(list)

 stock = Open_File('Icecream.txt', 0)
 in_stock = Open_File('Icecream.txt', 1)

 print(*list(stock), sep=', ')
 print(*list(in_stock), sep=', ')
 diff = stock.difference(in_stock)

 print(f'Закончилось: ', *list(diff))