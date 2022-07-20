cook_book = {}
with open ('cook_book.txt', encoding = 'utf-8') as book:
  for dish in book:
      dishes = dish.strip()
      ingredient = int(book.readline())
      ing_list = []
      for ing in range(ingredient):
          ingredient_name, quantity, measure = book.readline().split("|")
          quantity = int(quantity)
          ing_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure.strip()})
      cook_book[dishes] = ing_list
      book.readline()

print(cook_book)

# cook_book = {
#     'Омлет': [
#         {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#         {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#         {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#     'Утка по-пекински': [
#         {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#         {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#         {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#         {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#     'Запеченный картофель': [
#         {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#         {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#         {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
# }

def get_shop_list_by_dishes(dishes, person_count):
    ing = {}
    for key,values in cook_book.items():
        if key in dishes:
            for value in values:
                if value['ingredient_name'] in ing:
                    for a, b in ing.items():
                        b['quantity']+=value['quantity']*person_count
                else:
                    ing [value['ingredient_name']] = {'measure': value['measure'] , 'quantity': value['quantity']*person_count}
    print(ing)

get_shop_list_by_dishes(['Омлет','Запеченный картофель'] , 2)