import datetime


def logger_path(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            func_name = old_function.__name__
            func_result = old_function(*args, **kwargs)
            with open(path, 'w') as f:
                f.write(str(datetime.datetime.now()))
                f.write(func_name)
                f.write(*args, **kwargs)
                f.write(func_result)
            return new_function
        return logger
    return logger_path


def get_dict_from_file():
    with open('cook_book.txt') as f:
        cook_book = {}
        for line in f:
            counter = 0
            meal = line.strip()
            ingredients_num = f.readline().strip()
            ingredients_n = int(ingredients_num)
            cook_book[meal] = []
            while counter < ingredients_n:
                ingredient_list = f.readline().split('|')
                counter += 1
                ingredient_dict = {
                    "ingredient_name": ingredient_list[0].strip(),
                    "quantity": ingredient_list[1].strip(),
                    "measure": ingredient_list[2].strip()
                }
                cook_book[meal].append(ingredient_dict)
            f.readline()
    return cook_book


@logger_path('log.txt')
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_dict_from_file()
    shop_list_dict = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for item in cook_book[dish]:
                ing_name = item['ingredient_name']
                if ing_name not in shop_list_dict.keys():
                    shop_list_dict[ing_name] = {
                        'measure': item['measure'],
                        'quantity': int(item['quantity']) * person_count
                    }
                else:
                    plus_count = int(item['quantity']) * person_count
                    shop_list_dict[ing_name]['quantity'] += plus_count
    return shop_list_dict


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
